#!/usr/bin/env python
# -*- coding: utf-8 -*-
# from flask.helpers import url_for
from evotomasyon import app, db
# from flask import Flask
# from flask import request
from flask import render_template, redirect, request, url_for
import os
import datetime
# from evotomasyon.sr import speech_to_text
from evotomasyon.sr import CommandExecuter
from evotomasyon.models import Service



@app.route("/", methods=['POST', 'GET'])
def index(extra_info=None):
    service_list = Service.query.all()
    return render_template("index.html", service_list=service_list, extra_info= extra_info)



@app.route("/save-audio", methods=['POST', 'GET'])
def save_audio():
    if request.method == "POST":
        f = request.files['audio_data']
        now_date = datetime.datetime.now()
        filename  = now_date.strftime("%d_%m_%Y_%H_%M_%S_%f")+".wav"
        fullpath = os.path.join(os.getcwd(), "evotomasyon", "static", "uploads", filename)
        try:
            with open(fullpath, 'wb') as audio:
                f.save(audio)
            print(f'{filename} dosyası kaydedildi!')
        except:
            print("Dosya kaydedilirken 'save_audio' fonksiyonu içerisinde bir hata oluştu.")
        ce = CommandExecuter(fullpath)
        id_and_command_list = ce.id_and_list
        if len(id_and_command_list) > 1:
            s_id = id_and_command_list[0]
            s_command = id_and_command_list[1]
            return redirect(url_for('update_service_state', service_id=s_id, command=s_command))

        return f"Hata! Komut bulunamadı: {id_and_command_list}. Lütfen tekrar deneyin."


@app.route("/change-service/<int:service_id>", methods=['POST', 'GET'])
def change_service_state(service_id):
    service = Service.query.get(service_id)
    service.change_state()
    db.session.commit()
    print("State değişti!: ", str(service.state))
    return  redirect(url_for('index'))


@app.route("/update-service/<int:service_id>/<string:command>", methods=['POST', 'GET'])
def update_service_state(service_id, command):
    do_commit=False
    extra_info ="Hata! Bu servis zaten açık!"
    try:
        service_id = int(service_id)
    except:
        return  redirect(url_for('index', extra_info="service_id parse edilirken beklenmedik bir hata oluştu."))
    service = Service.query.get(service_id)
    if command =="enable":
        if service.state !=True:
            service.state =True
            extra_info =f"{service.service_name} servisi başarılı bir şekilde etkinleştirildi."
            do_commit=True
    elif command=="disable":
        if service.state !=False:
            service.state =False
            extra_info =f"{service.service_name} servisi kapatıldı."
            do_commit=True
        else:
            extra_info ="Hata! Bu servis zaten kapalı!"

    if do_commit:
        db.session.commit()
        print("State güncellendi!: ", str(service.state))
    return  extra_info



@app.context_processor
def example():
    return dict(myexample='This is an example')
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='home'),
    path("about", views.about, name='about'),
    path("trans", views.trans, name='trans'),
    path("tpos", views.tpos, name='tpos'),
    path("blogtext", views.blogtext, name='blogtext'),
    path("paraphrase", views.paraphrase, name='paraphrase'),
    path("textspeech", views.textspeech, name='textspeech'),
    path("speechtext", views.speechtext, name='speechtext'),
    path("services", views.services, name='services'),
    path("contact", views.contact, name='contact'),
    path("test", views.test, name='test'),
    path("senti", views.senti, name='senti'),
    path("keyw", views.keyw, name='keyw'),
    path("keyf", views.keyf, name='keyf'),
    path("publish", views.publish, name='publish'),
    path("subject", views.subject, name='subject'),
    path("spell", views.spell, name='spell'),
    path("pars", views.pars, name='pars'),
    path("dictonary", views.dictonary, name='dictonary'),
    path("external", views.external), 
    path("sentiment", views.sentiment),
    path("sent", views.sent),
    path("keyword", views.keyword),
    path("wordkey", views.wordkey),
    path("date", views.date),
    path("subj", views.subj),
    path("subjectivity", views.subjectivity),
    path("txtcor", views.txtcor),
    path("parse", views.parse),
    path("txtsumm", views.txtsumm),
    path("txtkeyf", views.txtkeyf),
    path("keyfurl", views.keyfurl),
    path("tts", views.tts),
    path("stt", views.stt),
    path("para", views.para),
    path("translate", views.translate),
    path("strans", views.strans),
    path("pos", views.pos),
    path("blog", views.blog),
    path("dict", views.dict),
]
# -*- coding: utf-8 -*-

from odoo import models, fields, api


class informacion(models.Model):
     _name = 'odoo_basico.informacion'
     _description = 'Exemplo proxecto odoo basico'

     name = fields.Char(string="Titulo")
     descripcion = fields.Text(string="A Descripción")
     alto_en_cms = fields.Integer(string="Alto en centímetros");
     longo_en_cms = fields.Integer(string="Longo en centímetros");
     ancho_en_cms = fields.Integer(string="Ancho en centímetros");
     peso = fields.Float(string="Peso en Kgs", default=2.5, digits=(6,2))
     autorizado = fields.Boolean(string="Autorizado?", default=True)
     sexo_traducido = fields.Selection([('Hombre','Home'),('Mujer','Muller'),('Otros','Outros')], string="Sexo")



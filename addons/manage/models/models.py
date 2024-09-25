# -*- coding: utf-8 -*-

from odoo import models, fields, api


class task(models.Model):
    _name = 'manage.task'
    _description = 'manage.task'

    name = fields.Char(string="Nombre", readonly=False, required=True, help="Introduzca el nombre") #Name
    description = fields.Text()
    creation_date = fields.Date()
    start_date = fields.Datetime()
    end_date = fields.Datetime()
    is_paused = fields.Boolean()
    sprint = fields.Many2one("manage.sprint", ondelete="set null", help="Sprint relacionado")


class sprint(models.Model):
    _name = 'manage.sprint'
    _description = 'manage.sprint'

    name = fields.Char() #Name
    description = fields.Text()
    creation_date = fields.Date()
    start_date = fields.Datetime()
    end_date = fields.Datetime()
    task = fields.One2many(string="Tareas", comodel_name="manage.task",inverse_name='sprint')
    


#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

from odoo import api , models , fields

class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _description = "Hospital Patient"

    name = fields.Char(string="Name")
    age = fields.Integer(string="Age")
    gender = fields.Selection([('male','Male'),('female','Female')] , string="Gender")
    active = fields.Boolean(string="Active" , default=True)


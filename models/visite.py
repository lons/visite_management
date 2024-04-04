from odoo import models, fields

class Visite(models.Model):
    _name = 'visite_management.visite'
    _description = 'Gestion des visites'

    date_visite = fields.Date(string='Date de la visite', required=True)
    heure_visite = fields.Float(string='Heure de la visite')
    visiteur = fields.Many2one('res.partner', string='Visiteur', required=True)
    entreprise = fields.Many2one('res.partner', string='Entreprise', required=True)
    objet_visite = fields.Text(string='Objet de la visite')

from odoo import models, fields, api


class HelloWorld(models.Model):
    _name = 'hello.world'
    _description = 'Hello World Model'
    _order = 'create_date desc'

    name = fields.Char('Name', required=True, help='Enter your name')
    message = fields.Text('Message', compute='_compute_message', store=True)
    greeting_type = fields.Selection([
        ('hello', 'Hello'),
        ('hi', 'Hi'),
        ('greetings', 'Greetings'),
        ('welcome', 'Welcome'),
    ], string='Greeting Type', default='hello', required=True)
    is_active = fields.Boolean('Active', default=True)
    created_date = fields.Datetime('Created Date', default=fields.Datetime.now)

    @api.depends('name', 'greeting_type')
    def _compute_message(self):
        for record in self:
            if record.name and record.greeting_type:
                greeting_map = {
                    'hello': 'Hello',
                    'hi': 'Hi',
                    'greetings': 'Greetings',
                    'welcome': 'Welcome',
                }
                greeting = greeting_map.get(record.greeting_type, 'Hello')
                record.message = f"{greeting}, {record.name}! Welcome to the Hello World App!"
            else:
                record.message = False

    def action_toggle_active(self):
        for record in self:
            record.is_active = not record.is_active
        return True
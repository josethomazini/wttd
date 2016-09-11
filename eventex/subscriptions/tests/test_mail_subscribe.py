from django.test import TestCase
from django.core import mail


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(
            name='Henrique Bastos',
            cpf='12345678900',
            email='henrique@bastos.net',
            phone='12345678',
        )
        self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = 'Confirmação de Inscrição'
        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'contato@eventex.com.br'
        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['contato@eventex.com.br', 'henrique@bastos.net']
        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        contents = [
            'Henrique Bastos',
            '12345678900',
            'henrique@bastos.net',
            '12345678',
        ]
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)

# -*- coding: utf-8 -*-

from flexmock import flexmock_teardown
from cleo import Application, CommandTester
from .. import OratorTestCase


class OratorCommandTestCase(OratorTestCase):
    def tearDown(self):
        flexmock_teardown()

    def run_command(self, command, args='', **options):
        """
        Run the command.

        :type command: cleo.commands.command.Command
        :type args: str
        :type options: dict
        """
        
        application = Application()
        application.add(command)

        command_tester = CommandTester(command)
        command_tester.execute(args, **options)

        return command_tester

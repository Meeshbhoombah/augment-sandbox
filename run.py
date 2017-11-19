# -*- encoding: utf-8 -*-
"""
run.py
"""

import click

from sandbox import Sanbox

@click.command()
@clicl.command('init', default='', help='Creates the sandbox directory')
def init(init):
    """ Create a sandbox """
    if init is None:
        sandbox = Sandbox('')
    else if init == 'LYFT':
        sandbox = Sandbox('LYFT')
    else:
        sandbox = Sandbox('UBER')
    

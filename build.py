#!env/bin/python3
import jinja2
import json
import os
import shutil

# Clean build
if os.path.exists('build'):
    shutil.rmtree('build')

# Read config
with open('config.json') as f:
    config = json.load(f)

# Copy public folder as build directory
shutil.copytree('public', 'build', symlinks=True)

# Build templates
env = jinja2.Environment(loader=jinja2.FileSystemLoader('templates'))

for name in config.get('templates', []):
    template = env.get_template(name)
    template.stream(**config).dump(f'build/{name}')

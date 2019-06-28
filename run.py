#!/usr/bin/env/python

import os
from jinja2 import Environment, FileSystemLoader

def build_from_templates():
	THIS_DIR = os.path.dirname(os.path.abspath(__file__))
	j2_env = Environment(loader=FileSystemLoader(THIS_DIR), trim_blocks=True)
	
	for file in os.listdir():
		if file.endswith(".html") and file != "base.html":
			f=open(THIS_DIR+"\\dist\\"+file,"w+")
			f.write(j2_env.get_template(file).render())
			f.close()

if __name__ == '__main__':
	build_from_templates()

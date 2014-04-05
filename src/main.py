#!/usr/bin/python3

import yaml
import aptools.jinja.html as html

def getdoc(filename):
  with open(filename, 'r') as f:
    return yaml.load(f)

def main():
  template = html.Templates("tmpl")
  category = template["category"]
  data = getdoc("data/raw.yaml")
  with open("../out/index.html","w") as f:
    f.write(category.render(data))
main()

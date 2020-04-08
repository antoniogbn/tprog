import sys
import argparse
import pyangbind
import os

parser = argparse.ArgumentParser()
parser.add_argument('model', default='', help="YANG model name")
args = parser.parse_args()

model = args.model

cmd_line = 'pyang -f tree mdl/' + model + '.yang'
print(cmd_line)
os.system(cmd_line)

var = '%s/plugin' % (os.path.dirname(pyangbind.__file__))

#cmd_line = 'export PYBINDPLUGIN="%s"' % (var)
#print(cmd_line)
#os.system(cmd_line)

os.environ['PYBINDPLUGIN'] = "%s"%(var)

cmd_line = 'pyang --plugindir $PYBINDPLUGIN -f pybind mdl/{model}.yang > obj/{model}.py'.format(model=model)
print(cmd_line)
os.system(cmd_line)


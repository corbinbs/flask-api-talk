from __future__ import absolute_import
import importlib
import os

from hubology.views import FlaskAPI

for i in os.listdir(os.path.dirname(__file__)):
    if os.path.isdir(i) or i == '__init__.py' or not i.endswith('.py'):
        continue
    importlib.import_module(__name__ + '.' + i.split('.')[0])


def inheritors(klass):
    subclasses = set()
    work = [klass]
    while work:
        parent = work.pop()
        for child in parent.__subclasses__():
            if child not in subclasses:
                subclasses.add(child)
                work.append(child)
    return subclasses

api_views = inheritors(FlaskAPI)
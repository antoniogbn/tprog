# -*- coding: utf-8 -*-
from operator import attrgetter
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType
from pyangbind.lib.yangtypes import RestrictedClassType
from pyangbind.lib.yangtypes import TypedListType
from pyangbind.lib.yangtypes import YANGBool
from pyangbind.lib.yangtypes import YANGListType
from pyangbind.lib.yangtypes import YANGDynClass
from pyangbind.lib.yangtypes import ReferenceType
from pyangbind.lib.base import PybindBase
from collections import OrderedDict
from decimal import Decimal
from bitarray import bitarray
import six

# PY3 support of some PY2 keywords (needs improved)
if six.PY3:
  import builtins as __builtin__
  long = int
elif six.PY2:
  import __builtin__

class yc_line____addLine__line___(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module addLine - based on the path /line___. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_path_helper', '_extmethods', '__pattern___','__description___','__routePartitionName___',)

  _yang_name = 'line___'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__pattern___ = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="pattern___", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='https://readthedocs.org/projects/hulkbuster/', defining_module='addLine', yang_type='data', is_config=True)
    self.__description___ = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="description___", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='https://readthedocs.org/projects/hulkbuster/', defining_module='addLine', yang_type='data', is_config=True)
    self.__routePartitionName___ = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="routePartitionName___", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='https://readthedocs.org/projects/hulkbuster/', defining_module='addLine', yang_type='data', is_config=True)

    load = kwargs.pop("load", None)
    if args:
      if len(args) > 1:
        raise TypeError("cannot create a YANG container with >1 argument")
      all_attr = True
      for e in self._pyangbind_elements:
        if not hasattr(args[0], e):
          all_attr = False
          break
      if not all_attr:
        raise ValueError("Supplied object did not have the correct attributes")
      for e in self._pyangbind_elements:
        nobj = getattr(args[0], e)
        if nobj._changed() is False:
          continue
        setmethod = getattr(self, "_set_%s" % e)
        if load is None:
          setmethod(getattr(args[0], e))
        else:
          setmethod(getattr(args[0], e), load=load)

  def _path(self):
    if hasattr(self, "_parent"):
      return self._parent._path()+[self._yang_name]
    else:
      return ['line___']

  def _get_pattern___(self):
    """
    Getter method for pattern___, mapped from YANG variable /line___/pattern___ (data)
    """
    return self.__pattern___
      
  def _set_pattern___(self, v, load=False):
    """
    Setter method for pattern___, mapped from YANG variable /line___/pattern___ (data)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_pattern___ is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_pattern___() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=six.text_type, is_leaf=True, yang_name="pattern___", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='https://readthedocs.org/projects/hulkbuster/', defining_module='addLine', yang_type='data', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """pattern___ must be of a type compatible with data""",
          'defined-type': "addLine:data",
          'generated-type': """YANGDynClass(base=six.text_type, is_leaf=True, yang_name="pattern___", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='https://readthedocs.org/projects/hulkbuster/', defining_module='addLine', yang_type='data', is_config=True)""",
        })

    self.__pattern___ = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_pattern___(self):
    self.__pattern___ = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="pattern___", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='https://readthedocs.org/projects/hulkbuster/', defining_module='addLine', yang_type='data', is_config=True)


  def _get_description___(self):
    """
    Getter method for description___, mapped from YANG variable /line___/description___ (data)
    """
    return self.__description___
      
  def _set_description___(self, v, load=False):
    """
    Setter method for description___, mapped from YANG variable /line___/description___ (data)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_description___ is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_description___() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=six.text_type, is_leaf=True, yang_name="description___", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='https://readthedocs.org/projects/hulkbuster/', defining_module='addLine', yang_type='data', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """description___ must be of a type compatible with data""",
          'defined-type': "addLine:data",
          'generated-type': """YANGDynClass(base=six.text_type, is_leaf=True, yang_name="description___", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='https://readthedocs.org/projects/hulkbuster/', defining_module='addLine', yang_type='data', is_config=True)""",
        })

    self.__description___ = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_description___(self):
    self.__description___ = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="description___", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='https://readthedocs.org/projects/hulkbuster/', defining_module='addLine', yang_type='data', is_config=True)


  def _get_routePartitionName___(self):
    """
    Getter method for routePartitionName___, mapped from YANG variable /line___/routePartitionName___ (data)
    """
    return self.__routePartitionName___
      
  def _set_routePartitionName___(self, v, load=False):
    """
    Setter method for routePartitionName___, mapped from YANG variable /line___/routePartitionName___ (data)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_routePartitionName___ is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_routePartitionName___() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=six.text_type, is_leaf=True, yang_name="routePartitionName___", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='https://readthedocs.org/projects/hulkbuster/', defining_module='addLine', yang_type='data', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """routePartitionName___ must be of a type compatible with data""",
          'defined-type': "addLine:data",
          'generated-type': """YANGDynClass(base=six.text_type, is_leaf=True, yang_name="routePartitionName___", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='https://readthedocs.org/projects/hulkbuster/', defining_module='addLine', yang_type='data', is_config=True)""",
        })

    self.__routePartitionName___ = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_routePartitionName___(self):
    self.__routePartitionName___ = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="routePartitionName___", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='https://readthedocs.org/projects/hulkbuster/', defining_module='addLine', yang_type='data', is_config=True)

  pattern___ = __builtin__.property(_get_pattern___, _set_pattern___)
  description___ = __builtin__.property(_get_description___, _set_description___)
  routePartitionName___ = __builtin__.property(_get_routePartitionName___, _set_routePartitionName___)


  _pyangbind_elements = OrderedDict([('pattern___', pattern___), ('description___', description___), ('routePartitionName___', routePartitionName___), ])


class addLine(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module addLine - based on the path /addLine. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_path_helper', '_extmethods', '__line___',)

  _yang_name = 'addLine'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__line___ = YANGDynClass(base=yc_line____addLine__line___, is_container='container', yang_name="line___", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='https://readthedocs.org/projects/hulkbuster/', defining_module='addLine', yang_type='container', is_config=True)

    load = kwargs.pop("load", None)
    if args:
      if len(args) > 1:
        raise TypeError("cannot create a YANG container with >1 argument")
      all_attr = True
      for e in self._pyangbind_elements:
        if not hasattr(args[0], e):
          all_attr = False
          break
      if not all_attr:
        raise ValueError("Supplied object did not have the correct attributes")
      for e in self._pyangbind_elements:
        nobj = getattr(args[0], e)
        if nobj._changed() is False:
          continue
        setmethod = getattr(self, "_set_%s" % e)
        if load is None:
          setmethod(getattr(args[0], e))
        else:
          setmethod(getattr(args[0], e), load=load)

  def _path(self):
    if hasattr(self, "_parent"):
      return self._parent._path()+[self._yang_name]
    else:
      return []

  def _get_line___(self):
    """
    Getter method for line___, mapped from YANG variable /line___ (container)
    """
    return self.__line___
      
  def _set_line___(self, v, load=False):
    """
    Setter method for line___, mapped from YANG variable /line___ (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_line___ is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_line___() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=yc_line____addLine__line___, is_container='container', yang_name="line___", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='https://readthedocs.org/projects/hulkbuster/', defining_module='addLine', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """line___ must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=yc_line____addLine__line___, is_container='container', yang_name="line___", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='https://readthedocs.org/projects/hulkbuster/', defining_module='addLine', yang_type='container', is_config=True)""",
        })

    self.__line___ = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_line___(self):
    self.__line___ = YANGDynClass(base=yc_line____addLine__line___, is_container='container', yang_name="line___", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='https://readthedocs.org/projects/hulkbuster/', defining_module='addLine', yang_type='container', is_config=True)

  line___ = __builtin__.property(_get_line___, _set_line___)


  _pyangbind_elements = OrderedDict([('line___', line___), ])


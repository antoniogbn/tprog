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

class yc_dirn____addPhone__phone____lines____line____dirn___(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module addPhone - based on the path /phone___/lines___/line___/dirn___. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_path_helper', '_extmethods', '__pattern___','__routePartitionName___',)

  _yang_name = 'dirn___'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__pattern___ = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="pattern___", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='https://localhost/tprog/', defining_module='addPhone', yang_type='data', is_config=True)
    self.__routePartitionName___ = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="routePartitionName___", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='https://localhost/tprog/', defining_module='addPhone', yang_type='data', is_config=True)

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
      return ['phone___', 'lines___', 'line___', 'dirn___']

  def _get_pattern___(self):
    """
    Getter method for pattern___, mapped from YANG variable /phone___/lines___/line___/dirn___/pattern___ (data)
    """
    return self.__pattern___
      
  def _set_pattern___(self, v, load=False):
    """
    Setter method for pattern___, mapped from YANG variable /phone___/lines___/line___/dirn___/pattern___ (data)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_pattern___ is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_pattern___() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=six.text_type, is_leaf=True, yang_name="pattern___", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='https://localhost/tprog/', defining_module='addPhone', yang_type='data', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """pattern___ must be of a type compatible with data""",
          'defined-type': "addPhone:data",
          'generated-type': """YANGDynClass(base=six.text_type, is_leaf=True, yang_name="pattern___", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='https://localhost/tprog/', defining_module='addPhone', yang_type='data', is_config=True)""",
        })

    self.__pattern___ = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_pattern___(self):
    self.__pattern___ = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="pattern___", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='https://localhost/tprog/', defining_module='addPhone', yang_type='data', is_config=True)


  def _get_routePartitionName___(self):
    """
    Getter method for routePartitionName___, mapped from YANG variable /phone___/lines___/line___/dirn___/routePartitionName___ (data)
    """
    return self.__routePartitionName___
      
  def _set_routePartitionName___(self, v, load=False):
    """
    Setter method for routePartitionName___, mapped from YANG variable /phone___/lines___/line___/dirn___/routePartitionName___ (data)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_routePartitionName___ is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_routePartitionName___() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=six.text_type, is_leaf=True, yang_name="routePartitionName___", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='https://localhost/tprog/', defining_module='addPhone', yang_type='data', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """routePartitionName___ must be of a type compatible with data""",
          'defined-type': "addPhone:data",
          'generated-type': """YANGDynClass(base=six.text_type, is_leaf=True, yang_name="routePartitionName___", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='https://localhost/tprog/', defining_module='addPhone', yang_type='data', is_config=True)""",
        })

    self.__routePartitionName___ = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_routePartitionName___(self):
    self.__routePartitionName___ = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="routePartitionName___", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='https://localhost/tprog/', defining_module='addPhone', yang_type='data', is_config=True)

  pattern___ = __builtin__.property(_get_pattern___, _set_pattern___)
  routePartitionName___ = __builtin__.property(_get_routePartitionName___, _set_routePartitionName___)


  _pyangbind_elements = OrderedDict([('pattern___', pattern___), ('routePartitionName___', routePartitionName___), ])


class yc_line____addPhone__phone____lines____line___(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module addPhone - based on the path /phone___/lines___/line___. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_path_helper', '_extmethods', '__index___','__dirn___',)

  _yang_name = 'line___'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__index___ = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="index___", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='https://localhost/tprog/', defining_module='addPhone', yang_type='data', is_config=True)
    self.__dirn___ = YANGDynClass(base=yc_dirn____addPhone__phone____lines____line____dirn___, is_container='container', yang_name="dirn___", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='https://localhost/tprog/', defining_module='addPhone', yang_type='container', is_config=True)

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
      return ['phone___', 'lines___', 'line___']

  def _get_index___(self):
    """
    Getter method for index___, mapped from YANG variable /phone___/lines___/line___/index___ (data)
    """
    return self.__index___
      
  def _set_index___(self, v, load=False):
    """
    Setter method for index___, mapped from YANG variable /phone___/lines___/line___/index___ (data)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_index___ is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_index___() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=six.text_type, is_leaf=True, yang_name="index___", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='https://localhost/tprog/', defining_module='addPhone', yang_type='data', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """index___ must be of a type compatible with data""",
          'defined-type': "addPhone:data",
          'generated-type': """YANGDynClass(base=six.text_type, is_leaf=True, yang_name="index___", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='https://localhost/tprog/', defining_module='addPhone', yang_type='data', is_config=True)""",
        })

    self.__index___ = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_index___(self):
    self.__index___ = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="index___", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='https://localhost/tprog/', defining_module='addPhone', yang_type='data', is_config=True)


  def _get_dirn___(self):
    """
    Getter method for dirn___, mapped from YANG variable /phone___/lines___/line___/dirn___ (container)
    """
    return self.__dirn___
      
  def _set_dirn___(self, v, load=False):
    """
    Setter method for dirn___, mapped from YANG variable /phone___/lines___/line___/dirn___ (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_dirn___ is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_dirn___() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=yc_dirn____addPhone__phone____lines____line____dirn___, is_container='container', yang_name="dirn___", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='https://localhost/tprog/', defining_module='addPhone', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """dirn___ must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=yc_dirn____addPhone__phone____lines____line____dirn___, is_container='container', yang_name="dirn___", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='https://localhost/tprog/', defining_module='addPhone', yang_type='container', is_config=True)""",
        })

    self.__dirn___ = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_dirn___(self):
    self.__dirn___ = YANGDynClass(base=yc_dirn____addPhone__phone____lines____line____dirn___, is_container='container', yang_name="dirn___", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='https://localhost/tprog/', defining_module='addPhone', yang_type='container', is_config=True)

  index___ = __builtin__.property(_get_index___, _set_index___)
  dirn___ = __builtin__.property(_get_dirn___, _set_dirn___)


  _pyangbind_elements = OrderedDict([('index___', index___), ('dirn___', dirn___), ])


class yc_lines____addPhone__phone____lines___(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module addPhone - based on the path /phone___/lines___. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_path_helper', '_extmethods', '__line___',)

  _yang_name = 'lines___'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__line___ = YANGDynClass(base=yc_line____addPhone__phone____lines____line___, is_container='container', yang_name="line___", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='https://localhost/tprog/', defining_module='addPhone', yang_type='container', is_config=True)

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
      return ['phone___', 'lines___']

  def _get_line___(self):
    """
    Getter method for line___, mapped from YANG variable /phone___/lines___/line___ (container)
    """
    return self.__line___
      
  def _set_line___(self, v, load=False):
    """
    Setter method for line___, mapped from YANG variable /phone___/lines___/line___ (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_line___ is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_line___() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=yc_line____addPhone__phone____lines____line___, is_container='container', yang_name="line___", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='https://localhost/tprog/', defining_module='addPhone', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """line___ must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=yc_line____addPhone__phone____lines____line___, is_container='container', yang_name="line___", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='https://localhost/tprog/', defining_module='addPhone', yang_type='container', is_config=True)""",
        })

    self.__line___ = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_line___(self):
    self.__line___ = YANGDynClass(base=yc_line____addPhone__phone____lines____line___, is_container='container', yang_name="line___", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='https://localhost/tprog/', defining_module='addPhone', yang_type='container', is_config=True)

  line___ = __builtin__.property(_get_line___, _set_line___)


  _pyangbind_elements = OrderedDict([('line___', line___), ])


class yc_phone____addPhone__phone___(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module addPhone - based on the path /phone___. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_path_helper', '_extmethods', '__name___','__description___','__product___','__class___','__protocol___','__devicePoolName___','__lines___',)

  _yang_name = 'phone___'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__name___ = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="name___", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='https://localhost/tprog/', defining_module='addPhone', yang_type='data', is_config=True)
    self.__description___ = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="description___", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='https://localhost/tprog/', defining_module='addPhone', yang_type='data', is_config=True)
    self.__product___ = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="product___", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='https://localhost/tprog/', defining_module='addPhone', yang_type='data', is_config=True)
    self.__class___ = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="class___", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='https://localhost/tprog/', defining_module='addPhone', yang_type='data', is_config=True)
    self.__protocol___ = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="protocol___", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='https://localhost/tprog/', defining_module='addPhone', yang_type='data', is_config=True)
    self.__devicePoolName___ = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="devicePoolName___", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='https://localhost/tprog/', defining_module='addPhone', yang_type='data', is_config=True)
    self.__lines___ = YANGDynClass(base=yc_lines____addPhone__phone____lines___, is_container='container', yang_name="lines___", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='https://localhost/tprog/', defining_module='addPhone', yang_type='container', is_config=True)

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
      return ['phone___']

  def _get_name___(self):
    """
    Getter method for name___, mapped from YANG variable /phone___/name___ (data)
    """
    return self.__name___
      
  def _set_name___(self, v, load=False):
    """
    Setter method for name___, mapped from YANG variable /phone___/name___ (data)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_name___ is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_name___() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=six.text_type, is_leaf=True, yang_name="name___", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='https://localhost/tprog/', defining_module='addPhone', yang_type='data', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """name___ must be of a type compatible with data""",
          'defined-type': "addPhone:data",
          'generated-type': """YANGDynClass(base=six.text_type, is_leaf=True, yang_name="name___", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='https://localhost/tprog/', defining_module='addPhone', yang_type='data', is_config=True)""",
        })

    self.__name___ = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_name___(self):
    self.__name___ = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="name___", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='https://localhost/tprog/', defining_module='addPhone', yang_type='data', is_config=True)


  def _get_description___(self):
    """
    Getter method for description___, mapped from YANG variable /phone___/description___ (data)
    """
    return self.__description___
      
  def _set_description___(self, v, load=False):
    """
    Setter method for description___, mapped from YANG variable /phone___/description___ (data)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_description___ is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_description___() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=six.text_type, is_leaf=True, yang_name="description___", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='https://localhost/tprog/', defining_module='addPhone', yang_type='data', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """description___ must be of a type compatible with data""",
          'defined-type': "addPhone:data",
          'generated-type': """YANGDynClass(base=six.text_type, is_leaf=True, yang_name="description___", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='https://localhost/tprog/', defining_module='addPhone', yang_type='data', is_config=True)""",
        })

    self.__description___ = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_description___(self):
    self.__description___ = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="description___", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='https://localhost/tprog/', defining_module='addPhone', yang_type='data', is_config=True)


  def _get_product___(self):
    """
    Getter method for product___, mapped from YANG variable /phone___/product___ (data)
    """
    return self.__product___
      
  def _set_product___(self, v, load=False):
    """
    Setter method for product___, mapped from YANG variable /phone___/product___ (data)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_product___ is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_product___() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=six.text_type, is_leaf=True, yang_name="product___", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='https://localhost/tprog/', defining_module='addPhone', yang_type='data', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """product___ must be of a type compatible with data""",
          'defined-type': "addPhone:data",
          'generated-type': """YANGDynClass(base=six.text_type, is_leaf=True, yang_name="product___", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='https://localhost/tprog/', defining_module='addPhone', yang_type='data', is_config=True)""",
        })

    self.__product___ = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_product___(self):
    self.__product___ = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="product___", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='https://localhost/tprog/', defining_module='addPhone', yang_type='data', is_config=True)


  def _get_class___(self):
    """
    Getter method for class___, mapped from YANG variable /phone___/class___ (data)
    """
    return self.__class___
      
  def _set_class___(self, v, load=False):
    """
    Setter method for class___, mapped from YANG variable /phone___/class___ (data)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_class___ is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_class___() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=six.text_type, is_leaf=True, yang_name="class___", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='https://localhost/tprog/', defining_module='addPhone', yang_type='data', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """class___ must be of a type compatible with data""",
          'defined-type': "addPhone:data",
          'generated-type': """YANGDynClass(base=six.text_type, is_leaf=True, yang_name="class___", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='https://localhost/tprog/', defining_module='addPhone', yang_type='data', is_config=True)""",
        })

    self.__class___ = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_class___(self):
    self.__class___ = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="class___", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='https://localhost/tprog/', defining_module='addPhone', yang_type='data', is_config=True)


  def _get_protocol___(self):
    """
    Getter method for protocol___, mapped from YANG variable /phone___/protocol___ (data)
    """
    return self.__protocol___
      
  def _set_protocol___(self, v, load=False):
    """
    Setter method for protocol___, mapped from YANG variable /phone___/protocol___ (data)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_protocol___ is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_protocol___() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=six.text_type, is_leaf=True, yang_name="protocol___", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='https://localhost/tprog/', defining_module='addPhone', yang_type='data', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """protocol___ must be of a type compatible with data""",
          'defined-type': "addPhone:data",
          'generated-type': """YANGDynClass(base=six.text_type, is_leaf=True, yang_name="protocol___", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='https://localhost/tprog/', defining_module='addPhone', yang_type='data', is_config=True)""",
        })

    self.__protocol___ = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_protocol___(self):
    self.__protocol___ = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="protocol___", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='https://localhost/tprog/', defining_module='addPhone', yang_type='data', is_config=True)


  def _get_devicePoolName___(self):
    """
    Getter method for devicePoolName___, mapped from YANG variable /phone___/devicePoolName___ (data)
    """
    return self.__devicePoolName___
      
  def _set_devicePoolName___(self, v, load=False):
    """
    Setter method for devicePoolName___, mapped from YANG variable /phone___/devicePoolName___ (data)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_devicePoolName___ is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_devicePoolName___() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=six.text_type, is_leaf=True, yang_name="devicePoolName___", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='https://localhost/tprog/', defining_module='addPhone', yang_type='data', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """devicePoolName___ must be of a type compatible with data""",
          'defined-type': "addPhone:data",
          'generated-type': """YANGDynClass(base=six.text_type, is_leaf=True, yang_name="devicePoolName___", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='https://localhost/tprog/', defining_module='addPhone', yang_type='data', is_config=True)""",
        })

    self.__devicePoolName___ = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_devicePoolName___(self):
    self.__devicePoolName___ = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="devicePoolName___", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='https://localhost/tprog/', defining_module='addPhone', yang_type='data', is_config=True)


  def _get_lines___(self):
    """
    Getter method for lines___, mapped from YANG variable /phone___/lines___ (container)
    """
    return self.__lines___
      
  def _set_lines___(self, v, load=False):
    """
    Setter method for lines___, mapped from YANG variable /phone___/lines___ (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_lines___ is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_lines___() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=yc_lines____addPhone__phone____lines___, is_container='container', yang_name="lines___", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='https://localhost/tprog/', defining_module='addPhone', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """lines___ must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=yc_lines____addPhone__phone____lines___, is_container='container', yang_name="lines___", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='https://localhost/tprog/', defining_module='addPhone', yang_type='container', is_config=True)""",
        })

    self.__lines___ = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_lines___(self):
    self.__lines___ = YANGDynClass(base=yc_lines____addPhone__phone____lines___, is_container='container', yang_name="lines___", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='https://localhost/tprog/', defining_module='addPhone', yang_type='container', is_config=True)

  name___ = __builtin__.property(_get_name___, _set_name___)
  description___ = __builtin__.property(_get_description___, _set_description___)
  product___ = __builtin__.property(_get_product___, _set_product___)
  class___ = __builtin__.property(_get_class___, _set_class___)
  protocol___ = __builtin__.property(_get_protocol___, _set_protocol___)
  devicePoolName___ = __builtin__.property(_get_devicePoolName___, _set_devicePoolName___)
  lines___ = __builtin__.property(_get_lines___, _set_lines___)


  _pyangbind_elements = OrderedDict([('name___', name___), ('description___', description___), ('product___', product___), ('class___', class___), ('protocol___', protocol___), ('devicePoolName___', devicePoolName___), ('lines___', lines___), ])


class addPhone(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module addPhone - based on the path /addPhone. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_path_helper', '_extmethods', '__phone___',)

  _yang_name = 'addPhone'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__phone___ = YANGDynClass(base=yc_phone____addPhone__phone___, is_container='container', yang_name="phone___", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='https://localhost/tprog/', defining_module='addPhone', yang_type='container', is_config=True)

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

  def _get_phone___(self):
    """
    Getter method for phone___, mapped from YANG variable /phone___ (container)
    """
    return self.__phone___
      
  def _set_phone___(self, v, load=False):
    """
    Setter method for phone___, mapped from YANG variable /phone___ (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_phone___ is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_phone___() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=yc_phone____addPhone__phone___, is_container='container', yang_name="phone___", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='https://localhost/tprog/', defining_module='addPhone', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """phone___ must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=yc_phone____addPhone__phone___, is_container='container', yang_name="phone___", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='https://localhost/tprog/', defining_module='addPhone', yang_type='container', is_config=True)""",
        })

    self.__phone___ = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_phone___(self):
    self.__phone___ = YANGDynClass(base=yc_phone____addPhone__phone___, is_container='container', yang_name="phone___", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='https://localhost/tprog/', defining_module='addPhone', yang_type='container', is_config=True)

  phone___ = __builtin__.property(_get_phone___, _set_phone___)


  _pyangbind_elements = OrderedDict([('phone___', phone___), ])


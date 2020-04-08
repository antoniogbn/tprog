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

class yc_auth_info____add_account__auth_info___(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module add_account - based on the path /auth_info___. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_path_helper', '_extmethods', '__login___','__password___',)

  _yang_name = 'auth_info___'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__login___ = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="login___", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='https://readthedocs.org/projects/tprog/', defining_module='add_account', yang_type='data', is_config=True)
    self.__password___ = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="password___", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='https://readthedocs.org/projects/tprog/', defining_module='add_account', yang_type='data', is_config=True)

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
      return ['auth_info___']

  def _get_login___(self):
    """
    Getter method for login___, mapped from YANG variable /auth_info___/login___ (data)
    """
    return self.__login___
      
  def _set_login___(self, v, load=False):
    """
    Setter method for login___, mapped from YANG variable /auth_info___/login___ (data)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_login___ is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_login___() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=six.text_type, is_leaf=True, yang_name="login___", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='https://readthedocs.org/projects/tprog/', defining_module='add_account', yang_type='data', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """login___ must be of a type compatible with data""",
          'defined-type': "add_account:data",
          'generated-type': """YANGDynClass(base=six.text_type, is_leaf=True, yang_name="login___", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='https://readthedocs.org/projects/tprog/', defining_module='add_account', yang_type='data', is_config=True)""",
        })

    self.__login___ = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_login___(self):
    self.__login___ = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="login___", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='https://readthedocs.org/projects/tprog/', defining_module='add_account', yang_type='data', is_config=True)


  def _get_password___(self):
    """
    Getter method for password___, mapped from YANG variable /auth_info___/password___ (data)
    """
    return self.__password___
      
  def _set_password___(self, v, load=False):
    """
    Setter method for password___, mapped from YANG variable /auth_info___/password___ (data)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_password___ is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_password___() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=six.text_type, is_leaf=True, yang_name="password___", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='https://readthedocs.org/projects/tprog/', defining_module='add_account', yang_type='data', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """password___ must be of a type compatible with data""",
          'defined-type': "add_account:data",
          'generated-type': """YANGDynClass(base=six.text_type, is_leaf=True, yang_name="password___", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='https://readthedocs.org/projects/tprog/', defining_module='add_account', yang_type='data', is_config=True)""",
        })

    self.__password___ = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_password___(self):
    self.__password___ = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="password___", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='https://readthedocs.org/projects/tprog/', defining_module='add_account', yang_type='data', is_config=True)

  login___ = __builtin__.property(_get_login___, _set_login___)
  password___ = __builtin__.property(_get_password___, _set_password___)


  _pyangbind_elements = OrderedDict([('login___', login___), ('password___', password___), ])


class yc_account_info____add_account__params____account_info___(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module add_account - based on the path /params___/account_info___. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_path_helper', '_extmethods', '__id___','__billing_model___','__i_product___','__i_customer___','__h323_password___','__batch_name___',)

  _yang_name = 'account_info___'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__id___ = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="id___", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='https://readthedocs.org/projects/tprog/', defining_module='add_account', yang_type='data', is_config=True)
    self.__billing_model___ = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="billing_model___", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='https://readthedocs.org/projects/tprog/', defining_module='add_account', yang_type='data', is_config=True)
    self.__i_product___ = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="i_product___", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='https://readthedocs.org/projects/tprog/', defining_module='add_account', yang_type='data', is_config=True)
    self.__i_customer___ = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="i_customer___", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='https://readthedocs.org/projects/tprog/', defining_module='add_account', yang_type='data', is_config=True)
    self.__h323_password___ = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="h323_password___", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='https://readthedocs.org/projects/tprog/', defining_module='add_account', yang_type='data', is_config=True)
    self.__batch_name___ = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="batch_name___", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='https://readthedocs.org/projects/tprog/', defining_module='add_account', yang_type='data', is_config=True)

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
      return ['params___', 'account_info___']

  def _get_id___(self):
    """
    Getter method for id___, mapped from YANG variable /params___/account_info___/id___ (data)
    """
    return self.__id___
      
  def _set_id___(self, v, load=False):
    """
    Setter method for id___, mapped from YANG variable /params___/account_info___/id___ (data)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_id___ is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_id___() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=six.text_type, is_leaf=True, yang_name="id___", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='https://readthedocs.org/projects/tprog/', defining_module='add_account', yang_type='data', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """id___ must be of a type compatible with data""",
          'defined-type': "add_account:data",
          'generated-type': """YANGDynClass(base=six.text_type, is_leaf=True, yang_name="id___", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='https://readthedocs.org/projects/tprog/', defining_module='add_account', yang_type='data', is_config=True)""",
        })

    self.__id___ = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_id___(self):
    self.__id___ = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="id___", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='https://readthedocs.org/projects/tprog/', defining_module='add_account', yang_type='data', is_config=True)


  def _get_billing_model___(self):
    """
    Getter method for billing_model___, mapped from YANG variable /params___/account_info___/billing_model___ (data)
    """
    return self.__billing_model___
      
  def _set_billing_model___(self, v, load=False):
    """
    Setter method for billing_model___, mapped from YANG variable /params___/account_info___/billing_model___ (data)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_billing_model___ is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_billing_model___() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=six.text_type, is_leaf=True, yang_name="billing_model___", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='https://readthedocs.org/projects/tprog/', defining_module='add_account', yang_type='data', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """billing_model___ must be of a type compatible with data""",
          'defined-type': "add_account:data",
          'generated-type': """YANGDynClass(base=six.text_type, is_leaf=True, yang_name="billing_model___", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='https://readthedocs.org/projects/tprog/', defining_module='add_account', yang_type='data', is_config=True)""",
        })

    self.__billing_model___ = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_billing_model___(self):
    self.__billing_model___ = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="billing_model___", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='https://readthedocs.org/projects/tprog/', defining_module='add_account', yang_type='data', is_config=True)


  def _get_i_product___(self):
    """
    Getter method for i_product___, mapped from YANG variable /params___/account_info___/i_product___ (data)
    """
    return self.__i_product___
      
  def _set_i_product___(self, v, load=False):
    """
    Setter method for i_product___, mapped from YANG variable /params___/account_info___/i_product___ (data)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_i_product___ is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_i_product___() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=six.text_type, is_leaf=True, yang_name="i_product___", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='https://readthedocs.org/projects/tprog/', defining_module='add_account', yang_type='data', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """i_product___ must be of a type compatible with data""",
          'defined-type': "add_account:data",
          'generated-type': """YANGDynClass(base=six.text_type, is_leaf=True, yang_name="i_product___", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='https://readthedocs.org/projects/tprog/', defining_module='add_account', yang_type='data', is_config=True)""",
        })

    self.__i_product___ = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_i_product___(self):
    self.__i_product___ = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="i_product___", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='https://readthedocs.org/projects/tprog/', defining_module='add_account', yang_type='data', is_config=True)


  def _get_i_customer___(self):
    """
    Getter method for i_customer___, mapped from YANG variable /params___/account_info___/i_customer___ (data)
    """
    return self.__i_customer___
      
  def _set_i_customer___(self, v, load=False):
    """
    Setter method for i_customer___, mapped from YANG variable /params___/account_info___/i_customer___ (data)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_i_customer___ is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_i_customer___() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=six.text_type, is_leaf=True, yang_name="i_customer___", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='https://readthedocs.org/projects/tprog/', defining_module='add_account', yang_type='data', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """i_customer___ must be of a type compatible with data""",
          'defined-type': "add_account:data",
          'generated-type': """YANGDynClass(base=six.text_type, is_leaf=True, yang_name="i_customer___", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='https://readthedocs.org/projects/tprog/', defining_module='add_account', yang_type='data', is_config=True)""",
        })

    self.__i_customer___ = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_i_customer___(self):
    self.__i_customer___ = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="i_customer___", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='https://readthedocs.org/projects/tprog/', defining_module='add_account', yang_type='data', is_config=True)


  def _get_h323_password___(self):
    """
    Getter method for h323_password___, mapped from YANG variable /params___/account_info___/h323_password___ (data)
    """
    return self.__h323_password___
      
  def _set_h323_password___(self, v, load=False):
    """
    Setter method for h323_password___, mapped from YANG variable /params___/account_info___/h323_password___ (data)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_h323_password___ is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_h323_password___() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=six.text_type, is_leaf=True, yang_name="h323_password___", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='https://readthedocs.org/projects/tprog/', defining_module='add_account', yang_type='data', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """h323_password___ must be of a type compatible with data""",
          'defined-type': "add_account:data",
          'generated-type': """YANGDynClass(base=six.text_type, is_leaf=True, yang_name="h323_password___", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='https://readthedocs.org/projects/tprog/', defining_module='add_account', yang_type='data', is_config=True)""",
        })

    self.__h323_password___ = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_h323_password___(self):
    self.__h323_password___ = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="h323_password___", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='https://readthedocs.org/projects/tprog/', defining_module='add_account', yang_type='data', is_config=True)


  def _get_batch_name___(self):
    """
    Getter method for batch_name___, mapped from YANG variable /params___/account_info___/batch_name___ (data)
    """
    return self.__batch_name___
      
  def _set_batch_name___(self, v, load=False):
    """
    Setter method for batch_name___, mapped from YANG variable /params___/account_info___/batch_name___ (data)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_batch_name___ is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_batch_name___() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=six.text_type, is_leaf=True, yang_name="batch_name___", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='https://readthedocs.org/projects/tprog/', defining_module='add_account', yang_type='data', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """batch_name___ must be of a type compatible with data""",
          'defined-type': "add_account:data",
          'generated-type': """YANGDynClass(base=six.text_type, is_leaf=True, yang_name="batch_name___", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='https://readthedocs.org/projects/tprog/', defining_module='add_account', yang_type='data', is_config=True)""",
        })

    self.__batch_name___ = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_batch_name___(self):
    self.__batch_name___ = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="batch_name___", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='https://readthedocs.org/projects/tprog/', defining_module='add_account', yang_type='data', is_config=True)

  id___ = __builtin__.property(_get_id___, _set_id___)
  billing_model___ = __builtin__.property(_get_billing_model___, _set_billing_model___)
  i_product___ = __builtin__.property(_get_i_product___, _set_i_product___)
  i_customer___ = __builtin__.property(_get_i_customer___, _set_i_customer___)
  h323_password___ = __builtin__.property(_get_h323_password___, _set_h323_password___)
  batch_name___ = __builtin__.property(_get_batch_name___, _set_batch_name___)


  _pyangbind_elements = OrderedDict([('id___', id___), ('billing_model___', billing_model___), ('i_product___', i_product___), ('i_customer___', i_customer___), ('h323_password___', h323_password___), ('batch_name___', batch_name___), ])


class yc_params____add_account__params___(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module add_account - based on the path /params___. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_path_helper', '_extmethods', '__account_info___',)

  _yang_name = 'params___'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__account_info___ = YANGDynClass(base=yc_account_info____add_account__params____account_info___, is_container='container', yang_name="account_info___", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='https://readthedocs.org/projects/tprog/', defining_module='add_account', yang_type='container', is_config=True)

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
      return ['params___']

  def _get_account_info___(self):
    """
    Getter method for account_info___, mapped from YANG variable /params___/account_info___ (container)
    """
    return self.__account_info___
      
  def _set_account_info___(self, v, load=False):
    """
    Setter method for account_info___, mapped from YANG variable /params___/account_info___ (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_account_info___ is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_account_info___() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=yc_account_info____add_account__params____account_info___, is_container='container', yang_name="account_info___", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='https://readthedocs.org/projects/tprog/', defining_module='add_account', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """account_info___ must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=yc_account_info____add_account__params____account_info___, is_container='container', yang_name="account_info___", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='https://readthedocs.org/projects/tprog/', defining_module='add_account', yang_type='container', is_config=True)""",
        })

    self.__account_info___ = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_account_info___(self):
    self.__account_info___ = YANGDynClass(base=yc_account_info____add_account__params____account_info___, is_container='container', yang_name="account_info___", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='https://readthedocs.org/projects/tprog/', defining_module='add_account', yang_type='container', is_config=True)

  account_info___ = __builtin__.property(_get_account_info___, _set_account_info___)


  _pyangbind_elements = OrderedDict([('account_info___', account_info___), ])


class add_account(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module add_account - based on the path /add_account. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_path_helper', '_extmethods', '__auth_info___','__params___',)

  _yang_name = 'add_account'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__auth_info___ = YANGDynClass(base=yc_auth_info____add_account__auth_info___, is_container='container', yang_name="auth_info___", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='https://readthedocs.org/projects/tprog/', defining_module='add_account', yang_type='container', is_config=True)
    self.__params___ = YANGDynClass(base=yc_params____add_account__params___, is_container='container', yang_name="params___", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='https://readthedocs.org/projects/tprog/', defining_module='add_account', yang_type='container', is_config=True)

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

  def _get_auth_info___(self):
    """
    Getter method for auth_info___, mapped from YANG variable /auth_info___ (container)
    """
    return self.__auth_info___
      
  def _set_auth_info___(self, v, load=False):
    """
    Setter method for auth_info___, mapped from YANG variable /auth_info___ (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_auth_info___ is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_auth_info___() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=yc_auth_info____add_account__auth_info___, is_container='container', yang_name="auth_info___", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='https://readthedocs.org/projects/tprog/', defining_module='add_account', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """auth_info___ must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=yc_auth_info____add_account__auth_info___, is_container='container', yang_name="auth_info___", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='https://readthedocs.org/projects/tprog/', defining_module='add_account', yang_type='container', is_config=True)""",
        })

    self.__auth_info___ = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_auth_info___(self):
    self.__auth_info___ = YANGDynClass(base=yc_auth_info____add_account__auth_info___, is_container='container', yang_name="auth_info___", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='https://readthedocs.org/projects/tprog/', defining_module='add_account', yang_type='container', is_config=True)


  def _get_params___(self):
    """
    Getter method for params___, mapped from YANG variable /params___ (container)
    """
    return self.__params___
      
  def _set_params___(self, v, load=False):
    """
    Setter method for params___, mapped from YANG variable /params___ (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_params___ is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_params___() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=yc_params____add_account__params___, is_container='container', yang_name="params___", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='https://readthedocs.org/projects/tprog/', defining_module='add_account', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """params___ must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=yc_params____add_account__params___, is_container='container', yang_name="params___", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='https://readthedocs.org/projects/tprog/', defining_module='add_account', yang_type='container', is_config=True)""",
        })

    self.__params___ = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_params___(self):
    self.__params___ = YANGDynClass(base=yc_params____add_account__params___, is_container='container', yang_name="params___", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='https://readthedocs.org/projects/tprog/', defining_module='add_account', yang_type='container', is_config=True)

  auth_info___ = __builtin__.property(_get_auth_info___, _set_auth_info___)
  params___ = __builtin__.property(_get_params___, _set_params___)


  _pyangbind_elements = OrderedDict([('auth_info___', auth_info___), ('params___', params___), ])



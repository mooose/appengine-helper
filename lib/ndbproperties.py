# appengine ndb Properties
#

from google.appengine.ext import ndb

import decimal

class DecimalProperty(ndb.StringProperty):
  # data_type = decimal.Decimal
  def _validate(self, value):
    if not isinstance(value, decimal.Decimal):
      if not isinstance(value, str):
        if not isinstance(value, float):
          raise TypeError("expected Decimal or String, got %s." % repr(value))

  def _to_base_type(self, value):
    return str(value)

  # def make_value_from_datastore(self, value):
  def _from_base_type(self, value):
    return decimal.Decimal(value)


class ReferenceProperty(ndb.KeyProperty):
    def _validate(self, value):
        if not isinstance(value, ndb.Model):
            raise TypeError('expected an ndb.Model, got %s' % repr(value))

    def _to_base_type(self, value):
        return value.key

    def _from_base_type(self, value):
        return value.get()


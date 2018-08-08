"""Clean export of other_models.

We manually remove the following symbols from this module to keep tab
completion as clean as possible--even when it doesn't respect `__all__`.
Clean namespaces for those lucid.modelzoo modules that contain models are
enforced by tests in test/modelzoo/test_vision_models.
"""


from lucid.modelzoo.vision_base import Model as _Model

from lucid.modelzoo.other_models.InceptionV1 import InceptionV1


__all__ = [_name for _name, _obj in list(globals().items())
           if isinstance(_obj, type) and issubclass(_obj, _Model)
           and _obj is not _Model]

# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: carla_msgs.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='carla_msgs.proto',
  package='carla_msgs',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x10\x63\x61rla_msgs.proto\x12\ncarla_msgs\"\x87\x01\n\x07\x43trlCmd\x12\x10\n\x08throttle\x18\x01 \x01(\x02\x12\r\n\x05steer\x18\x02 \x01(\x02\x12\r\n\x05\x62rake\x18\x03 \x01(\x02\x12\x12\n\nhand_brake\x18\x04 \x01(\x08\x12\x0f\n\x07reverse\x18\x05 \x01(\x08\x12\x19\n\x11manual_gear_shift\x18\x06 \x01(\x08\x12\x0c\n\x04gear\x18\x07 \x01(\rb\x06proto3')
)




_CTRLCMD = _descriptor.Descriptor(
  name='CtrlCmd',
  full_name='carla_msgs.CtrlCmd',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='throttle', full_name='carla_msgs.CtrlCmd.throttle', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='steer', full_name='carla_msgs.CtrlCmd.steer', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='brake', full_name='carla_msgs.CtrlCmd.brake', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hand_brake', full_name='carla_msgs.CtrlCmd.hand_brake', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='reverse', full_name='carla_msgs.CtrlCmd.reverse', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='manual_gear_shift', full_name='carla_msgs.CtrlCmd.manual_gear_shift', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gear', full_name='carla_msgs.CtrlCmd.gear', index=6,
      number=7, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=33,
  serialized_end=168,
)

DESCRIPTOR.message_types_by_name['CtrlCmd'] = _CTRLCMD
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CtrlCmd = _reflection.GeneratedProtocolMessageType('CtrlCmd', (_message.Message,), {
  'DESCRIPTOR' : _CTRLCMD,
  '__module__' : 'carla_msgs_pb2'
  # @@protoc_insertion_point(class_scope:carla_msgs.CtrlCmd)
  })
_sym_db.RegisterMessage(CtrlCmd)


# @@protoc_insertion_point(module_scope)

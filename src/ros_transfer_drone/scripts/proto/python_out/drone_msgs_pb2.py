# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: drone_msgs.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='drone_msgs.proto',
  package='drone_msgs',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x10\x64rone_msgs.proto\x12\ndrone_msgs\"v\n\x03Gps\x12\x10\n\x08\x61ltitude\x18\x01 \x01(\x01\x12\x10\n\x08latitude\x18\x02 \x01(\x01\x12\x12\n\nlongtitude\x18\x03 \x01(\x01\x12\x11\n\tlin_vel_x\x18\x04 \x01(\x01\x12\x11\n\tlin_vel_y\x18\x05 \x01(\x01\x12\x11\n\tlin_vel_z\x18\x06 \x01(\x01\"~\n\x03Imu\x12\x0e\n\x06orin_x\x18\x01 \x01(\x01\x12\x0e\n\x06orin_y\x18\x02 \x01(\x01\x12\x0e\n\x06orin_z\x18\x03 \x01(\x01\x12\x0e\n\x06orin_w\x18\x04 \x01(\x01\x12\x11\n\tang_vel_x\x18\x05 \x01(\x01\x12\x11\n\tang_vel_y\x18\x06 \x01(\x01\x12\x11\n\tang_vel_z\x18\x07 \x01(\x01\"\xe5\x01\n\x04Odom\x12\x0e\n\x06orin_w\x18\x01 \x01(\x01\x12\x0e\n\x06orin_x\x18\x02 \x01(\x01\x12\x0e\n\x06orin_y\x18\x03 \x01(\x01\x12\x0e\n\x06orin_z\x18\x04 \x01(\x01\x12\r\n\x05pos_x\x18\x05 \x01(\x01\x12\r\n\x05pos_y\x18\x06 \x01(\x01\x12\r\n\x05pos_z\x18\x07 \x01(\x01\x12\x11\n\tang_vel_x\x18\x08 \x01(\x01\x12\x11\n\tang_vel_y\x18\t \x01(\x01\x12\x11\n\tang_vel_z\x18\n \x01(\x01\x12\x11\n\tlin_vel_x\x18\x0b \x01(\x01\x12\x11\n\tlin_vel_y\x18\x0c \x01(\x01\x12\x11\n\tlin_vel_z\x18\r \x01(\x01\".\n\x0c\x42\x61tteryState\x12\x10\n\x08\x63\x65ll_vol\x18\x01 \x01(\x01\x12\x0c\n\x04rate\x18\x02 \x01(\x01\x62\x06proto3')
)




_GPS = _descriptor.Descriptor(
  name='Gps',
  full_name='drone_msgs.Gps',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='altitude', full_name='drone_msgs.Gps.altitude', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='latitude', full_name='drone_msgs.Gps.latitude', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='longtitude', full_name='drone_msgs.Gps.longtitude', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lin_vel_x', full_name='drone_msgs.Gps.lin_vel_x', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lin_vel_y', full_name='drone_msgs.Gps.lin_vel_y', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lin_vel_z', full_name='drone_msgs.Gps.lin_vel_z', index=5,
      number=6, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=32,
  serialized_end=150,
)


_IMU = _descriptor.Descriptor(
  name='Imu',
  full_name='drone_msgs.Imu',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='orin_x', full_name='drone_msgs.Imu.orin_x', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='orin_y', full_name='drone_msgs.Imu.orin_y', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='orin_z', full_name='drone_msgs.Imu.orin_z', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='orin_w', full_name='drone_msgs.Imu.orin_w', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ang_vel_x', full_name='drone_msgs.Imu.ang_vel_x', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ang_vel_y', full_name='drone_msgs.Imu.ang_vel_y', index=5,
      number=6, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ang_vel_z', full_name='drone_msgs.Imu.ang_vel_z', index=6,
      number=7, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=152,
  serialized_end=278,
)


_ODOM = _descriptor.Descriptor(
  name='Odom',
  full_name='drone_msgs.Odom',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='orin_w', full_name='drone_msgs.Odom.orin_w', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='orin_x', full_name='drone_msgs.Odom.orin_x', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='orin_y', full_name='drone_msgs.Odom.orin_y', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='orin_z', full_name='drone_msgs.Odom.orin_z', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pos_x', full_name='drone_msgs.Odom.pos_x', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pos_y', full_name='drone_msgs.Odom.pos_y', index=5,
      number=6, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pos_z', full_name='drone_msgs.Odom.pos_z', index=6,
      number=7, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ang_vel_x', full_name='drone_msgs.Odom.ang_vel_x', index=7,
      number=8, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ang_vel_y', full_name='drone_msgs.Odom.ang_vel_y', index=8,
      number=9, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ang_vel_z', full_name='drone_msgs.Odom.ang_vel_z', index=9,
      number=10, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lin_vel_x', full_name='drone_msgs.Odom.lin_vel_x', index=10,
      number=11, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lin_vel_y', full_name='drone_msgs.Odom.lin_vel_y', index=11,
      number=12, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lin_vel_z', full_name='drone_msgs.Odom.lin_vel_z', index=12,
      number=13, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=281,
  serialized_end=510,
)


_BATTERYSTATE = _descriptor.Descriptor(
  name='BatteryState',
  full_name='drone_msgs.BatteryState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cell_vol', full_name='drone_msgs.BatteryState.cell_vol', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rate', full_name='drone_msgs.BatteryState.rate', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=512,
  serialized_end=558,
)

DESCRIPTOR.message_types_by_name['Gps'] = _GPS
DESCRIPTOR.message_types_by_name['Imu'] = _IMU
DESCRIPTOR.message_types_by_name['Odom'] = _ODOM
DESCRIPTOR.message_types_by_name['BatteryState'] = _BATTERYSTATE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Gps = _reflection.GeneratedProtocolMessageType('Gps', (_message.Message,), {
  'DESCRIPTOR' : _GPS,
  '__module__' : 'drone_msgs_pb2'
  # @@protoc_insertion_point(class_scope:drone_msgs.Gps)
  })
_sym_db.RegisterMessage(Gps)

Imu = _reflection.GeneratedProtocolMessageType('Imu', (_message.Message,), {
  'DESCRIPTOR' : _IMU,
  '__module__' : 'drone_msgs_pb2'
  # @@protoc_insertion_point(class_scope:drone_msgs.Imu)
  })
_sym_db.RegisterMessage(Imu)

Odom = _reflection.GeneratedProtocolMessageType('Odom', (_message.Message,), {
  'DESCRIPTOR' : _ODOM,
  '__module__' : 'drone_msgs_pb2'
  # @@protoc_insertion_point(class_scope:drone_msgs.Odom)
  })
_sym_db.RegisterMessage(Odom)

BatteryState = _reflection.GeneratedProtocolMessageType('BatteryState', (_message.Message,), {
  'DESCRIPTOR' : _BATTERYSTATE,
  '__module__' : 'drone_msgs_pb2'
  # @@protoc_insertion_point(class_scope:drone_msgs.BatteryState)
  })
_sym_db.RegisterMessage(BatteryState)


# @@protoc_insertion_point(module_scope)

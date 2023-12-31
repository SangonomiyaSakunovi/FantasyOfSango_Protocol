# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ResProtocol.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='ResProtocol.proto',
  package='SangoResProtocol',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x11ResProtocol.proto\x12\x10SangoResProtocol\"A\n\x11MissionConfigList\x12,\n\x03Lst\x18\x01 \x03(\x0b\x32\x1f.SangoResProtocol.MissionConfig\"S\n\rMissionConfig\x12\n\n\x02Id\x18\x01 \x01(\x05\x12\x0c\n\x04Name\x18\x02 \x01(\t\x12(\n\x06Reward\x18\x03 \x03(\x0b\x32\x18.SangoResProtocol.Reward\"!\n\x06Reward\x12\n\n\x02Id\x18\x01 \x01(\x05\x12\x0b\n\x03Num\x18\x02 \x01(\x05\x62\x06proto3'
)




_MISSIONCONFIGLIST = _descriptor.Descriptor(
  name='MissionConfigList',
  full_name='SangoResProtocol.MissionConfigList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='Lst', full_name='SangoResProtocol.MissionConfigList.Lst', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=39,
  serialized_end=104,
)


_MISSIONCONFIG = _descriptor.Descriptor(
  name='MissionConfig',
  full_name='SangoResProtocol.MissionConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='Id', full_name='SangoResProtocol.MissionConfig.Id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Name', full_name='SangoResProtocol.MissionConfig.Name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Reward', full_name='SangoResProtocol.MissionConfig.Reward', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=106,
  serialized_end=189,
)


_REWARD = _descriptor.Descriptor(
  name='Reward',
  full_name='SangoResProtocol.Reward',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='Id', full_name='SangoResProtocol.Reward.Id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Num', full_name='SangoResProtocol.Reward.Num', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=191,
  serialized_end=224,
)

_MISSIONCONFIGLIST.fields_by_name['Lst'].message_type = _MISSIONCONFIG
_MISSIONCONFIG.fields_by_name['Reward'].message_type = _REWARD
DESCRIPTOR.message_types_by_name['MissionConfigList'] = _MISSIONCONFIGLIST
DESCRIPTOR.message_types_by_name['MissionConfig'] = _MISSIONCONFIG
DESCRIPTOR.message_types_by_name['Reward'] = _REWARD
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MissionConfigList = _reflection.GeneratedProtocolMessageType('MissionConfigList', (_message.Message,), {
  'DESCRIPTOR' : _MISSIONCONFIGLIST,
  '__module__' : 'ResProtocol_pb2'
  # @@protoc_insertion_point(class_scope:SangoResProtocol.MissionConfigList)
  })
_sym_db.RegisterMessage(MissionConfigList)

MissionConfig = _reflection.GeneratedProtocolMessageType('MissionConfig', (_message.Message,), {
  'DESCRIPTOR' : _MISSIONCONFIG,
  '__module__' : 'ResProtocol_pb2'
  # @@protoc_insertion_point(class_scope:SangoResProtocol.MissionConfig)
  })
_sym_db.RegisterMessage(MissionConfig)

Reward = _reflection.GeneratedProtocolMessageType('Reward', (_message.Message,), {
  'DESCRIPTOR' : _REWARD,
  '__module__' : 'ResProtocol_pb2'
  # @@protoc_insertion_point(class_scope:SangoResProtocol.Reward)
  })
_sym_db.RegisterMessage(Reward)


# @@protoc_insertion_point(module_scope)

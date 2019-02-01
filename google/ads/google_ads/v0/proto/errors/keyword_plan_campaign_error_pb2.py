# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v0/proto/errors/keyword_plan_campaign_error.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v0/proto/errors/keyword_plan_campaign_error.proto',
  package='google.ads.googleads.v0.errors',
  syntax='proto3',
  serialized_options=_b('\n\"com.google.ads.googleads.v0.errorsB\035KeywordPlanCampaignErrorProtoP\001ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v0/errors;errors\242\002\003GAA\252\002\036Google.Ads.GoogleAds.V0.Errors\312\002\036Google\\Ads\\GoogleAds\\V0\\Errors\352\002\"Google::Ads::GoogleAds::V0::Errors'),
  serialized_pb=_b('\nFgoogle/ads/googleads_v0/proto/errors/keyword_plan_campaign_error.proto\x12\x1egoogle.ads.googleads.v0.errors\"\xbf\x01\n\x1cKeywordPlanCampaignErrorEnum\"\x9e\x01\n\x18KeywordPlanCampaignError\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x10\n\x0cINVALID_NAME\x10\x02\x12\x15\n\x11INVALID_LANGUAGES\x10\x03\x12\x10\n\x0cINVALID_GEOS\x10\x04\x12\x12\n\x0e\x44UPLICATE_NAME\x10\x05\x12\x15\n\x11MAX_GEOS_EXCEEDED\x10\x06\x42\xf8\x01\n\"com.google.ads.googleads.v0.errorsB\x1dKeywordPlanCampaignErrorProtoP\x01ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v0/errors;errors\xa2\x02\x03GAA\xaa\x02\x1eGoogle.Ads.GoogleAds.V0.Errors\xca\x02\x1eGoogle\\Ads\\GoogleAds\\V0\\Errors\xea\x02\"Google::Ads::GoogleAds::V0::Errorsb\x06proto3')
)



_KEYWORDPLANCAMPAIGNERRORENUM_KEYWORDPLANCAMPAIGNERROR = _descriptor.EnumDescriptor(
  name='KeywordPlanCampaignError',
  full_name='google.ads.googleads.v0.errors.KeywordPlanCampaignErrorEnum.KeywordPlanCampaignError',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_NAME', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_LANGUAGES', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_GEOS', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DUPLICATE_NAME', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MAX_GEOS_EXCEEDED', index=6, number=6,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=140,
  serialized_end=298,
)
_sym_db.RegisterEnumDescriptor(_KEYWORDPLANCAMPAIGNERRORENUM_KEYWORDPLANCAMPAIGNERROR)


_KEYWORDPLANCAMPAIGNERRORENUM = _descriptor.Descriptor(
  name='KeywordPlanCampaignErrorEnum',
  full_name='google.ads.googleads.v0.errors.KeywordPlanCampaignErrorEnum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _KEYWORDPLANCAMPAIGNERRORENUM_KEYWORDPLANCAMPAIGNERROR,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=107,
  serialized_end=298,
)

_KEYWORDPLANCAMPAIGNERRORENUM_KEYWORDPLANCAMPAIGNERROR.containing_type = _KEYWORDPLANCAMPAIGNERRORENUM
DESCRIPTOR.message_types_by_name['KeywordPlanCampaignErrorEnum'] = _KEYWORDPLANCAMPAIGNERRORENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

KeywordPlanCampaignErrorEnum = _reflection.GeneratedProtocolMessageType('KeywordPlanCampaignErrorEnum', (_message.Message,), dict(
  DESCRIPTOR = _KEYWORDPLANCAMPAIGNERRORENUM,
  __module__ = 'google.ads.googleads_v0.proto.errors.keyword_plan_campaign_error_pb2'
  ,
  __doc__ = """Container for enum describing possible errors from applying a keyword
  plan campaign.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v0.errors.KeywordPlanCampaignErrorEnum)
  ))
_sym_db.RegisterMessage(KeywordPlanCampaignErrorEnum)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
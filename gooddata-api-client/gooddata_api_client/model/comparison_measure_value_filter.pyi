# coding: utf-8

"""
    OpenAPI definition

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v0
    Contact: support@gooddata.com
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from gooddata_api_client import schemas  # noqa: F401


class ComparisonMeasureValueFilter(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Filter the result by comparing specified metric to given constant value, using given comparison operator.
    """


    class MetaOapg:
        required = {
            "comparisonMeasureValueFilter",
        }
        
        class properties:
            
            
            class comparisonMeasureValueFilter(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    required = {
                        "measure",
                        "value",
                        "operator",
                    }
                    
                    class properties:
                        applyOnResult = schemas.BoolSchema
                    
                        @staticmethod
                        def measure() -> typing.Type['AfmIdentifier']:
                            return AfmIdentifier
                        
                        
                        class operator(
                            schemas.EnumBase,
                            schemas.StrSchema
                        ):
                            
                            @schemas.classproperty
                            def GREATER_THAN(cls):
                                return cls("GREATER_THAN")
                            
                            @schemas.classproperty
                            def GREATER_THAN_OR_EQUAL_TO(cls):
                                return cls("GREATER_THAN_OR_EQUAL_TO")
                            
                            @schemas.classproperty
                            def LESS_THAN(cls):
                                return cls("LESS_THAN")
                            
                            @schemas.classproperty
                            def LESS_THAN_OR_EQUAL_TO(cls):
                                return cls("LESS_THAN_OR_EQUAL_TO")
                            
                            @schemas.classproperty
                            def EQUAL_TO(cls):
                                return cls("EQUAL_TO")
                            
                            @schemas.classproperty
                            def NOT_EQUAL_TO(cls):
                                return cls("NOT_EQUAL_TO")
                        treatNullValuesAs = schemas.NumberSchema
                        value = schemas.NumberSchema
                        __annotations__ = {
                            "applyOnResult": applyOnResult,
                            "measure": measure,
                            "operator": operator,
                            "treatNullValuesAs": treatNullValuesAs,
                            "value": value,
                        }
                
                measure: 'AfmIdentifier'
                value: MetaOapg.properties.value
                operator: MetaOapg.properties.operator
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["applyOnResult"]) -> MetaOapg.properties.applyOnResult: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["measure"]) -> 'AfmIdentifier': ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["operator"]) -> MetaOapg.properties.operator: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["treatNullValuesAs"]) -> MetaOapg.properties.treatNullValuesAs: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["value"]) -> MetaOapg.properties.value: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["applyOnResult", "measure", "operator", "treatNullValuesAs", "value", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["applyOnResult"]) -> typing.Union[MetaOapg.properties.applyOnResult, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["measure"]) -> 'AfmIdentifier': ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["operator"]) -> MetaOapg.properties.operator: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["treatNullValuesAs"]) -> typing.Union[MetaOapg.properties.treatNullValuesAs, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["value"]) -> MetaOapg.properties.value: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["applyOnResult", "measure", "operator", "treatNullValuesAs", "value", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, ],
                    measure: 'AfmIdentifier',
                    value: typing.Union[MetaOapg.properties.value, decimal.Decimal, int, float, ],
                    operator: typing.Union[MetaOapg.properties.operator, str, ],
                    applyOnResult: typing.Union[MetaOapg.properties.applyOnResult, bool, schemas.Unset] = schemas.unset,
                    treatNullValuesAs: typing.Union[MetaOapg.properties.treatNullValuesAs, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'comparisonMeasureValueFilter':
                    return super().__new__(
                        cls,
                        *_args,
                        measure=measure,
                        value=value,
                        operator=operator,
                        applyOnResult=applyOnResult,
                        treatNullValuesAs=treatNullValuesAs,
                        _configuration=_configuration,
                        **kwargs,
                    )
            __annotations__ = {
                "comparisonMeasureValueFilter": comparisonMeasureValueFilter,
            }
    
    comparisonMeasureValueFilter: MetaOapg.properties.comparisonMeasureValueFilter
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["comparisonMeasureValueFilter"]) -> MetaOapg.properties.comparisonMeasureValueFilter: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["comparisonMeasureValueFilter", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["comparisonMeasureValueFilter"]) -> MetaOapg.properties.comparisonMeasureValueFilter: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["comparisonMeasureValueFilter", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        comparisonMeasureValueFilter: typing.Union[MetaOapg.properties.comparisonMeasureValueFilter, dict, frozendict.frozendict, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ComparisonMeasureValueFilter':
        return super().__new__(
            cls,
            *_args,
            comparisonMeasureValueFilter=comparisonMeasureValueFilter,
            _configuration=_configuration,
            **kwargs,
        )

from gooddata_api_client.model.afm_identifier import AfmIdentifier
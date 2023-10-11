# Auto generated from monterey_schema.yaml by pythongen.py version: 0.0.1
# Generation date: 2023-10-11T15:00:18
# Schema: monterey-schema
#
# id: https://w3id.org/microbiomedata/monterey-schema
# description: Proving grounds for a refactored nmdc-schema
# license: MIT

import dataclasses
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.linkml_model.types import String, Uriorcurie
from linkml_runtime.utils.metamodelcore import URIorCURIE

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
EXAMPLE = CurieNamespace('example', 'https://example.org/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
MONTEREY_SCHEMA = CurieNamespace('monterey_schema', 'https://w3id.org/microbiomedata/monterey-schema/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
DEFAULT_ = MONTEREY_SCHEMA


# Types

# Class references
class NamedThingId(URIorCURIE):
    pass


class MaterialOrDataId(NamedThingId):
    pass


class MaterialEntityId(MaterialOrDataId):
    pass


class DataEntityId(MaterialOrDataId):
    pass


class PlannedProcessId(NamedThingId):
    pass


class Root(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MONTEREY_SCHEMA.Root
    class_class_curie: ClassVar[str] = "monterey_schema:Root"
    class_name: ClassVar[str] = "Root"
    class_model_uri: ClassVar[URIRef] = MONTEREY_SCHEMA.Root


class AnonymousThing(Root):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MONTEREY_SCHEMA.AnonymousThing
    class_class_curie: ClassVar[str] = "monterey_schema:AnonymousThing"
    class_name: ClassVar[str] = "AnonymousThing"
    class_model_uri: ClassVar[URIRef] = MONTEREY_SCHEMA.AnonymousThing


@dataclass
class NamedThing(Root):
    """
    A generic grouping for any identifiable entity
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA.Thing
    class_class_curie: ClassVar[str] = "schema:Thing"
    class_name: ClassVar[str] = "NamedThing"
    class_model_uri: ClassVar[URIRef] = MONTEREY_SCHEMA.NamedThing

    id: Union[str, NamedThingId] = None
    name: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NamedThingId):
            self.id = NamedThingId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass
class MaterialOrData(NamedThing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MONTEREY_SCHEMA.MaterialOrData
    class_class_curie: ClassVar[str] = "monterey_schema:MaterialOrData"
    class_name: ClassVar[str] = "MaterialOrData"
    class_model_uri: ClassVar[URIRef] = MONTEREY_SCHEMA.MaterialOrData

    id: Union[str, MaterialOrDataId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MaterialOrDataId):
            self.id = MaterialOrDataId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class MaterialEntity(MaterialOrData):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MONTEREY_SCHEMA.MaterialEntity
    class_class_curie: ClassVar[str] = "monterey_schema:MaterialEntity"
    class_name: ClassVar[str] = "MaterialEntity"
    class_model_uri: ClassVar[URIRef] = MONTEREY_SCHEMA.MaterialEntity

    id: Union[str, MaterialEntityId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MaterialEntityId):
            self.id = MaterialEntityId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class DataEntity(MaterialOrData):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MONTEREY_SCHEMA.DataEntity
    class_class_curie: ClassVar[str] = "monterey_schema:DataEntity"
    class_name: ClassVar[str] = "DataEntity"
    class_model_uri: ClassVar[URIRef] = MONTEREY_SCHEMA.DataEntity

    id: Union[str, DataEntityId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DataEntityId):
            self.id = DataEntityId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class PlannedProcess(NamedThing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MONTEREY_SCHEMA.PlannedProcess
    class_class_curie: ClassVar[str] = "monterey_schema:PlannedProcess"
    class_name: ClassVar[str] = "PlannedProcess"
    class_model_uri: ClassVar[URIRef] = MONTEREY_SCHEMA.PlannedProcess

    id: Union[str, PlannedProcessId] = None
    has_inputs: Optional[Union[Union[str, MaterialOrDataId], List[Union[str, MaterialOrDataId]]]] = empty_list()
    has_outputs: Optional[Union[Union[str, MaterialOrDataId], List[Union[str, MaterialOrDataId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PlannedProcessId):
            self.id = PlannedProcessId(self.id)

        if not isinstance(self.has_inputs, list):
            self.has_inputs = [self.has_inputs] if self.has_inputs is not None else []
        self.has_inputs = [v if isinstance(v, MaterialOrDataId) else MaterialOrDataId(v) for v in self.has_inputs]

        if not isinstance(self.has_outputs, list):
            self.has_outputs = [self.has_outputs] if self.has_outputs is not None else []
        self.has_outputs = [v if isinstance(v, MaterialOrDataId) else MaterialOrDataId(v) for v in self.has_outputs]

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.has_inputs = Slot(uri=MONTEREY_SCHEMA.has_inputs, name="has_inputs", curie=MONTEREY_SCHEMA.curie('has_inputs'),
                   model_uri=MONTEREY_SCHEMA.has_inputs, domain=PlannedProcess, range=Optional[Union[Union[str, MaterialOrDataId], List[Union[str, MaterialOrDataId]]]])

slots.has_outputs = Slot(uri=MONTEREY_SCHEMA.has_outputs, name="has_outputs", curie=MONTEREY_SCHEMA.curie('has_outputs'),
                   model_uri=MONTEREY_SCHEMA.has_outputs, domain=PlannedProcess, range=Optional[Union[Union[str, MaterialOrDataId], List[Union[str, MaterialOrDataId]]]])

slots.id = Slot(uri=SCHEMA.identifier, name="id", curie=SCHEMA.curie('identifier'),
                   model_uri=MONTEREY_SCHEMA.id, domain=None, range=URIRef)

slots.name = Slot(uri=SCHEMA.name, name="name", curie=SCHEMA.curie('name'),
                   model_uri=MONTEREY_SCHEMA.name, domain=None, range=Optional[str])

slots.description = Slot(uri=SCHEMA.description, name="description", curie=SCHEMA.curie('description'),
                   model_uri=MONTEREY_SCHEMA.description, domain=None, range=Optional[str])
# Auto generated from monterey_schema.yaml by pythongen.py version: 0.0.1
# Generation date: 2023-10-12T00:47:35
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
RDF = CurieNamespace('rdf', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#')
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


class MaterialProcessingId(PlannedProcessId):
    pass


class DataProcessingId(PlannedProcessId):
    pass


class DataGenerationId(PlannedProcessId):
    pass


class NmdcClass(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MONTEREY_SCHEMA.NmdcClass
    class_class_curie: ClassVar[str] = "monterey_schema:NmdcClass"
    class_name: ClassVar[str] = "NmdcClass"
    class_model_uri: ClassVar[URIRef] = MONTEREY_SCHEMA.NmdcClass


@dataclass
class AnonymousThing(NmdcClass):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MONTEREY_SCHEMA.AnonymousThing
    class_class_curie: ClassVar[str] = "monterey_schema:AnonymousThing"
    class_name: ClassVar[str] = "AnonymousThing"
    class_model_uri: ClassVar[URIRef] = MONTEREY_SCHEMA.AnonymousThing

    type: Union[str, URIorCURIE] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        self.type = str(self.class_class_curie)

        super().__post_init__(**kwargs)


@dataclass
class NamedThing(NmdcClass):
    """
    A generic grouping for any identifiable entity
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA.Thing
    class_class_curie: ClassVar[str] = "schema:Thing"
    class_name: ClassVar[str] = "NamedThing"
    class_model_uri: ClassVar[URIRef] = MONTEREY_SCHEMA.NamedThing

    id: Union[str, NamedThingId] = None
    type: Union[str, URIorCURIE] = None
    name: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NamedThingId):
            self.id = NamedThingId(self.id)

        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        self.type = str(self.class_class_curie)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


    def __new__(cls, *args, **kwargs):

        type_designator = "type"
        if not type_designator in kwargs:
            return super().__new__(cls,*args,**kwargs)
        else:
            type_designator_value = kwargs[type_designator]
            target_cls = cls._class_for("class_class_curie", type_designator_value)


            if target_cls is None:
                target_cls = cls._class_for("class_class_uri", type_designator_value)


            if target_cls is None:
                target_cls = cls._class_for("class_model_uri", type_designator_value)


            if target_cls is None:
                raise ValueError(f"Wrong type designator value: class {cls.__name__} "
                                 f"has no subclass with ['class_class_curie', 'class_class_uri', 'class_model_uri']='{kwargs[type_designator]}'")
            return super().__new__(target_cls,*args,**kwargs)



@dataclass
class MaterialOrData(NamedThing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MONTEREY_SCHEMA.MaterialOrData
    class_class_curie: ClassVar[str] = "monterey_schema:MaterialOrData"
    class_name: ClassVar[str] = "MaterialOrData"
    class_model_uri: ClassVar[URIRef] = MONTEREY_SCHEMA.MaterialOrData

    id: Union[str, MaterialOrDataId] = None
    type: Union[str, URIorCURIE] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MaterialOrDataId):
            self.id = MaterialOrDataId(self.id)

        super().__post_init__(**kwargs)
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        self.type = str(self.class_class_curie)


@dataclass
class MaterialEntity(MaterialOrData):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MONTEREY_SCHEMA.MaterialEntity
    class_class_curie: ClassVar[str] = "monterey_schema:MaterialEntity"
    class_name: ClassVar[str] = "MaterialEntity"
    class_model_uri: ClassVar[URIRef] = MONTEREY_SCHEMA.MaterialEntity

    id: Union[str, MaterialEntityId] = None
    type: Union[str, URIorCURIE] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MaterialEntityId):
            self.id = MaterialEntityId(self.id)

        super().__post_init__(**kwargs)
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        self.type = str(self.class_class_curie)


@dataclass
class DataEntity(MaterialOrData):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MONTEREY_SCHEMA.DataEntity
    class_class_curie: ClassVar[str] = "monterey_schema:DataEntity"
    class_name: ClassVar[str] = "DataEntity"
    class_model_uri: ClassVar[URIRef] = MONTEREY_SCHEMA.DataEntity

    id: Union[str, DataEntityId] = None
    type: Union[str, URIorCURIE] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DataEntityId):
            self.id = DataEntityId(self.id)

        super().__post_init__(**kwargs)
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        self.type = str(self.class_class_curie)


class Database(NmdcClass):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MONTEREY_SCHEMA.Database
    class_class_curie: ClassVar[str] = "monterey_schema:Database"
    class_name: ClassVar[str] = "Database"
    class_model_uri: ClassVar[URIRef] = MONTEREY_SCHEMA.Database


@dataclass
class PlannedProcess(NamedThing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MONTEREY_SCHEMA.PlannedProcess
    class_class_curie: ClassVar[str] = "monterey_schema:PlannedProcess"
    class_name: ClassVar[str] = "PlannedProcess"
    class_model_uri: ClassVar[URIRef] = MONTEREY_SCHEMA.PlannedProcess

    id: Union[str, PlannedProcessId] = None
    type: Union[str, URIorCURIE] = None
    has_inputs: Optional[Union[Union[str, MaterialOrDataId], List[Union[str, MaterialOrDataId]]]] = empty_list()
    has_outputs: Optional[Union[Union[str, MaterialOrDataId], List[Union[str, MaterialOrDataId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.has_inputs, list):
            self.has_inputs = [self.has_inputs] if self.has_inputs is not None else []
        self.has_inputs = [v if isinstance(v, MaterialOrDataId) else MaterialOrDataId(v) for v in self.has_inputs]

        if not isinstance(self.has_outputs, list):
            self.has_outputs = [self.has_outputs] if self.has_outputs is not None else []
        self.has_outputs = [v if isinstance(v, MaterialOrDataId) else MaterialOrDataId(v) for v in self.has_outputs]

        super().__post_init__(**kwargs)
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        self.type = str(self.class_class_curie)


@dataclass
class MaterialProcessing(PlannedProcess):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MONTEREY_SCHEMA.MaterialProcessing
    class_class_curie: ClassVar[str] = "monterey_schema:MaterialProcessing"
    class_name: ClassVar[str] = "MaterialProcessing"
    class_model_uri: ClassVar[URIRef] = MONTEREY_SCHEMA.MaterialProcessing

    id: Union[str, MaterialProcessingId] = None
    type: Union[str, URIorCURIE] = None
    has_inputs: Optional[Union[Union[str, MaterialEntityId], List[Union[str, MaterialEntityId]]]] = empty_list()
    has_outputs: Optional[Union[Union[str, MaterialEntityId], List[Union[str, MaterialEntityId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MaterialProcessingId):
            self.id = MaterialProcessingId(self.id)

        if not isinstance(self.has_inputs, list):
            self.has_inputs = [self.has_inputs] if self.has_inputs is not None else []
        self.has_inputs = [v if isinstance(v, MaterialEntityId) else MaterialEntityId(v) for v in self.has_inputs]

        if not isinstance(self.has_outputs, list):
            self.has_outputs = [self.has_outputs] if self.has_outputs is not None else []
        self.has_outputs = [v if isinstance(v, MaterialEntityId) else MaterialEntityId(v) for v in self.has_outputs]

        super().__post_init__(**kwargs)
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        self.type = str(self.class_class_curie)


@dataclass
class DataProcessing(PlannedProcess):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MONTEREY_SCHEMA.DataProcessing
    class_class_curie: ClassVar[str] = "monterey_schema:DataProcessing"
    class_name: ClassVar[str] = "DataProcessing"
    class_model_uri: ClassVar[URIRef] = MONTEREY_SCHEMA.DataProcessing

    id: Union[str, DataProcessingId] = None
    type: Union[str, URIorCURIE] = None
    has_inputs: Optional[Union[Union[str, DataEntityId], List[Union[str, DataEntityId]]]] = empty_list()
    has_outputs: Optional[Union[Union[str, DataEntityId], List[Union[str, DataEntityId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DataProcessingId):
            self.id = DataProcessingId(self.id)

        if not isinstance(self.has_inputs, list):
            self.has_inputs = [self.has_inputs] if self.has_inputs is not None else []
        self.has_inputs = [v if isinstance(v, DataEntityId) else DataEntityId(v) for v in self.has_inputs]

        if not isinstance(self.has_outputs, list):
            self.has_outputs = [self.has_outputs] if self.has_outputs is not None else []
        self.has_outputs = [v if isinstance(v, DataEntityId) else DataEntityId(v) for v in self.has_outputs]

        super().__post_init__(**kwargs)
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        self.type = str(self.class_class_curie)


@dataclass
class DataGeneration(PlannedProcess):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MONTEREY_SCHEMA.DataGeneration
    class_class_curie: ClassVar[str] = "monterey_schema:DataGeneration"
    class_name: ClassVar[str] = "DataGeneration"
    class_model_uri: ClassVar[URIRef] = MONTEREY_SCHEMA.DataGeneration

    id: Union[str, DataGenerationId] = None
    type: Union[str, URIorCURIE] = None
    has_inputs: Optional[Union[Union[str, MaterialEntityId], List[Union[str, MaterialEntityId]]]] = empty_list()
    has_outputs: Optional[Union[Union[str, DataEntityId], List[Union[str, DataEntityId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DataGenerationId):
            self.id = DataGenerationId(self.id)

        if not isinstance(self.has_inputs, list):
            self.has_inputs = [self.has_inputs] if self.has_inputs is not None else []
        self.has_inputs = [v if isinstance(v, MaterialEntityId) else MaterialEntityId(v) for v in self.has_inputs]

        if not isinstance(self.has_outputs, list):
            self.has_outputs = [self.has_outputs] if self.has_outputs is not None else []
        self.has_outputs = [v if isinstance(v, DataEntityId) else DataEntityId(v) for v in self.has_outputs]

        super().__post_init__(**kwargs)
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        self.type = str(self.class_class_curie)


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

slots.object_collection = Slot(uri=MONTEREY_SCHEMA.object_collection, name="object_collection", curie=MONTEREY_SCHEMA.curie('object_collection'),
                   model_uri=MONTEREY_SCHEMA.object_collection, domain=Database, range=Optional[Union[str, NamedThingId]])

slots.process_collection = Slot(uri=MONTEREY_SCHEMA.process_collection, name="process_collection", curie=MONTEREY_SCHEMA.curie('process_collection'),
                   model_uri=MONTEREY_SCHEMA.process_collection, domain=Database, range=Optional[Union[Dict[Union[str, PlannedProcessId], Union[dict, "PlannedProcess"]], List[Union[dict, "PlannedProcess"]]]])

slots.type = Slot(uri=RDF.type, name="type", curie=RDF.curie('type'),
                   model_uri=MONTEREY_SCHEMA.type, domain=None, range=Union[str, URIorCURIE])

slots.MaterialProcessing_has_inputs = Slot(uri=MONTEREY_SCHEMA.has_inputs, name="MaterialProcessing_has_inputs", curie=MONTEREY_SCHEMA.curie('has_inputs'),
                   model_uri=MONTEREY_SCHEMA.MaterialProcessing_has_inputs, domain=MaterialProcessing, range=Optional[Union[Union[str, MaterialEntityId], List[Union[str, MaterialEntityId]]]])

slots.MaterialProcessing_has_outputs = Slot(uri=MONTEREY_SCHEMA.has_outputs, name="MaterialProcessing_has_outputs", curie=MONTEREY_SCHEMA.curie('has_outputs'),
                   model_uri=MONTEREY_SCHEMA.MaterialProcessing_has_outputs, domain=MaterialProcessing, range=Optional[Union[Union[str, MaterialEntityId], List[Union[str, MaterialEntityId]]]])

slots.DataProcessing_has_inputs = Slot(uri=MONTEREY_SCHEMA.has_inputs, name="DataProcessing_has_inputs", curie=MONTEREY_SCHEMA.curie('has_inputs'),
                   model_uri=MONTEREY_SCHEMA.DataProcessing_has_inputs, domain=DataProcessing, range=Optional[Union[Union[str, DataEntityId], List[Union[str, DataEntityId]]]])

slots.DataProcessing_has_outputs = Slot(uri=MONTEREY_SCHEMA.has_outputs, name="DataProcessing_has_outputs", curie=MONTEREY_SCHEMA.curie('has_outputs'),
                   model_uri=MONTEREY_SCHEMA.DataProcessing_has_outputs, domain=DataProcessing, range=Optional[Union[Union[str, DataEntityId], List[Union[str, DataEntityId]]]])

slots.DataGeneration_has_inputs = Slot(uri=MONTEREY_SCHEMA.has_inputs, name="DataGeneration_has_inputs", curie=MONTEREY_SCHEMA.curie('has_inputs'),
                   model_uri=MONTEREY_SCHEMA.DataGeneration_has_inputs, domain=DataGeneration, range=Optional[Union[Union[str, MaterialEntityId], List[Union[str, MaterialEntityId]]]])

slots.DataGeneration_has_outputs = Slot(uri=MONTEREY_SCHEMA.has_outputs, name="DataGeneration_has_outputs", curie=MONTEREY_SCHEMA.curie('has_outputs'),
                   model_uri=MONTEREY_SCHEMA.DataGeneration_has_outputs, domain=DataGeneration, range=Optional[Union[Union[str, DataEntityId], List[Union[str, DataEntityId]]]])
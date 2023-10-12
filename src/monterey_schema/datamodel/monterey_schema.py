# Auto generated from monterey_schema.yaml by pythongen.py version: 0.0.1
# Generation date: 2023-10-12T01:08:57
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


class InvestigationId(PlannedProcessId):
    pass


class MaterialProcessingId(PlannedProcessId):
    pass


class DataProcessingId(PlannedProcessId):
    pass


class DataGenerationId(PlannedProcessId):
    pass


class PersonId(MaterialEntityId):
    pass


class InstrumentId(MaterialEntityId):
    pass


class ProtocolId(DataEntityId):
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
    category: Union[str, "GeneralCategories"] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        self.type = str(self.class_class_curie)

        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, GeneralCategories):
            self.category = GeneralCategories(self.category)

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
    category: Union[str, "GeneralCategories"] = None
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

        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, GeneralCategories):
            self.category = GeneralCategories(self.category)

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
    category: Union[str, "GeneralCategories"] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):

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
    category: Union[str, "GeneralCategories"] = None

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
    category: Union[str, "GeneralCategories"] = None

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
    category: Union[str, "GeneralCategories"] = None
    has_outputs: Union[Union[str, MaterialOrDataId], List[Union[str, MaterialOrDataId]]] = None
    has_inputs: Optional[Union[Union[str, MaterialOrDataId], List[Union[str, MaterialOrDataId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.has_outputs):
            self.MissingRequiredField("has_outputs")
        if not isinstance(self.has_outputs, list):
            self.has_outputs = [self.has_outputs] if self.has_outputs is not None else []
        self.has_outputs = [v if isinstance(v, MaterialOrDataId) else MaterialOrDataId(v) for v in self.has_outputs]

        if not isinstance(self.has_inputs, list):
            self.has_inputs = [self.has_inputs] if self.has_inputs is not None else []
        self.has_inputs = [v if isinstance(v, MaterialOrDataId) else MaterialOrDataId(v) for v in self.has_inputs]

        super().__post_init__(**kwargs)
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        self.type = str(self.class_class_curie)


@dataclass
class Investigation(PlannedProcess):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MONTEREY_SCHEMA.Investigation
    class_class_curie: ClassVar[str] = "monterey_schema:Investigation"
    class_name: ClassVar[str] = "Investigation"
    class_model_uri: ClassVar[URIRef] = MONTEREY_SCHEMA.Investigation

    id: Union[str, InvestigationId] = None
    type: Union[str, URIorCURIE] = None
    category: Union[str, "GeneralCategories"] = None
    has_outputs: Union[Union[str, MaterialOrDataId], List[Union[str, MaterialOrDataId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, InvestigationId):
            self.id = InvestigationId(self.id)

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
    category: Union[str, "GeneralCategories"] = None
    has_outputs: Union[Union[str, MaterialEntityId], List[Union[str, MaterialEntityId]]] = None
    used: Optional[Union[str, InstrumentId]] = None
    followed: Optional[Union[str, ProtocolId]] = None
    has_inputs: Optional[Union[Union[str, MaterialEntityId], List[Union[str, MaterialEntityId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MaterialProcessingId):
            self.id = MaterialProcessingId(self.id)

        if self._is_empty(self.has_outputs):
            self.MissingRequiredField("has_outputs")
        if not isinstance(self.has_outputs, list):
            self.has_outputs = [self.has_outputs] if self.has_outputs is not None else []
        self.has_outputs = [v if isinstance(v, MaterialEntityId) else MaterialEntityId(v) for v in self.has_outputs]

        if self.used is not None and not isinstance(self.used, InstrumentId):
            self.used = InstrumentId(self.used)

        if self.followed is not None and not isinstance(self.followed, ProtocolId):
            self.followed = ProtocolId(self.followed)

        if not isinstance(self.has_inputs, list):
            self.has_inputs = [self.has_inputs] if self.has_inputs is not None else []
        self.has_inputs = [v if isinstance(v, MaterialEntityId) else MaterialEntityId(v) for v in self.has_inputs]

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
    category: Union[str, "GeneralCategories"] = None
    has_outputs: Union[Union[str, DataEntityId], List[Union[str, DataEntityId]]] = None
    has_inputs: Optional[Union[Union[str, DataEntityId], List[Union[str, DataEntityId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DataProcessingId):
            self.id = DataProcessingId(self.id)

        if self._is_empty(self.has_outputs):
            self.MissingRequiredField("has_outputs")
        if not isinstance(self.has_outputs, list):
            self.has_outputs = [self.has_outputs] if self.has_outputs is not None else []
        self.has_outputs = [v if isinstance(v, DataEntityId) else DataEntityId(v) for v in self.has_outputs]

        if not isinstance(self.has_inputs, list):
            self.has_inputs = [self.has_inputs] if self.has_inputs is not None else []
        self.has_inputs = [v if isinstance(v, DataEntityId) else DataEntityId(v) for v in self.has_inputs]

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
    category: Union[str, "GeneralCategories"] = None
    has_outputs: Union[Union[str, DataEntityId], List[Union[str, DataEntityId]]] = None
    used: Optional[Union[str, InstrumentId]] = None
    followed: Optional[Union[str, ProtocolId]] = None
    has_inputs: Optional[Union[Union[str, MaterialEntityId], List[Union[str, MaterialEntityId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DataGenerationId):
            self.id = DataGenerationId(self.id)

        if self._is_empty(self.has_outputs):
            self.MissingRequiredField("has_outputs")
        if not isinstance(self.has_outputs, list):
            self.has_outputs = [self.has_outputs] if self.has_outputs is not None else []
        self.has_outputs = [v if isinstance(v, DataEntityId) else DataEntityId(v) for v in self.has_outputs]

        if self.used is not None and not isinstance(self.used, InstrumentId):
            self.used = InstrumentId(self.used)

        if self.followed is not None and not isinstance(self.followed, ProtocolId):
            self.followed = ProtocolId(self.followed)

        if not isinstance(self.has_inputs, list):
            self.has_inputs = [self.has_inputs] if self.has_inputs is not None else []
        self.has_inputs = [v if isinstance(v, MaterialEntityId) else MaterialEntityId(v) for v in self.has_inputs]

        super().__post_init__(**kwargs)
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        self.type = str(self.class_class_curie)


@dataclass
class Person(MaterialEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MONTEREY_SCHEMA.Person
    class_class_curie: ClassVar[str] = "monterey_schema:Person"
    class_name: ClassVar[str] = "Person"
    class_model_uri: ClassVar[URIRef] = MONTEREY_SCHEMA.Person

    id: Union[str, PersonId] = None
    type: Union[str, URIorCURIE] = None
    category: Union[str, "GeneralCategories"] = None
    orcid: Union[str, URIorCURIE] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PersonId):
            self.id = PersonId(self.id)

        if self._is_empty(self.orcid):
            self.MissingRequiredField("orcid")
        if not isinstance(self.orcid, URIorCURIE):
            self.orcid = URIorCURIE(self.orcid)

        super().__post_init__(**kwargs)
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        self.type = str(self.class_class_curie)


@dataclass
class Instrument(MaterialEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MONTEREY_SCHEMA.Instrument
    class_class_curie: ClassVar[str] = "monterey_schema:Instrument"
    class_name: ClassVar[str] = "Instrument"
    class_model_uri: ClassVar[URIRef] = MONTEREY_SCHEMA.Instrument

    id: Union[str, InstrumentId] = None
    type: Union[str, URIorCURIE] = None
    category: Union[str, "GeneralCategories"] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, InstrumentId):
            self.id = InstrumentId(self.id)

        super().__post_init__(**kwargs)
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        self.type = str(self.class_class_curie)


@dataclass
class Protocol(DataEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MONTEREY_SCHEMA.Protocol
    class_class_curie: ClassVar[str] = "monterey_schema:Protocol"
    class_name: ClassVar[str] = "Protocol"
    class_model_uri: ClassVar[URIRef] = MONTEREY_SCHEMA.Protocol

    id: Union[str, ProtocolId] = None
    type: Union[str, URIorCURIE] = None
    category: Union[str, "GeneralCategories"] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ProtocolId):
            self.id = ProtocolId(self.id)

        super().__post_init__(**kwargs)
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        self.type = str(self.class_class_curie)


# Enumerations
class GeneralCategories(EnumDefinitionImpl):

    red = PermissibleValue(text="red")
    green = PermissibleValue(text="green")
    blue = PermissibleValue(text="blue")

    _defn = EnumDefinition(
        name="GeneralCategories",
    )

# Slots
class slots:
    pass

slots.has_inputs = Slot(uri=MONTEREY_SCHEMA.has_inputs, name="has_inputs", curie=MONTEREY_SCHEMA.curie('has_inputs'),
                   model_uri=MONTEREY_SCHEMA.has_inputs, domain=PlannedProcess, range=Optional[Union[Union[str, MaterialOrDataId], List[Union[str, MaterialOrDataId]]]])

slots.has_outputs = Slot(uri=MONTEREY_SCHEMA.has_outputs, name="has_outputs", curie=MONTEREY_SCHEMA.curie('has_outputs'),
                   model_uri=MONTEREY_SCHEMA.has_outputs, domain=PlannedProcess, range=Union[Union[str, MaterialOrDataId], List[Union[str, MaterialOrDataId]]])

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

slots.category = Slot(uri=MONTEREY_SCHEMA.category, name="category", curie=MONTEREY_SCHEMA.curie('category'),
                   model_uri=MONTEREY_SCHEMA.category, domain=None, range=Union[str, "GeneralCategories"])

slots.url = Slot(uri=MONTEREY_SCHEMA.url, name="url", curie=MONTEREY_SCHEMA.curie('url'),
                   model_uri=MONTEREY_SCHEMA.url, domain=None, range=str)

slots.used = Slot(uri=MONTEREY_SCHEMA.used, name="used", curie=MONTEREY_SCHEMA.curie('used'),
                   model_uri=MONTEREY_SCHEMA.used, domain=PlannedProcess, range=Optional[Union[str, InstrumentId]])

slots.followed = Slot(uri=MONTEREY_SCHEMA.followed, name="followed", curie=MONTEREY_SCHEMA.curie('followed'),
                   model_uri=MONTEREY_SCHEMA.followed, domain=PlannedProcess, range=Optional[Union[str, ProtocolId]])

slots.orcid = Slot(uri=MONTEREY_SCHEMA.orcid, name="orcid", curie=MONTEREY_SCHEMA.curie('orcid'),
                   model_uri=MONTEREY_SCHEMA.orcid, domain=None, range=Union[str, URIorCURIE])

slots.MaterialProcessing_has_inputs = Slot(uri=MONTEREY_SCHEMA.has_inputs, name="MaterialProcessing_has_inputs", curie=MONTEREY_SCHEMA.curie('has_inputs'),
                   model_uri=MONTEREY_SCHEMA.MaterialProcessing_has_inputs, domain=MaterialProcessing, range=Optional[Union[Union[str, MaterialEntityId], List[Union[str, MaterialEntityId]]]])

slots.MaterialProcessing_has_outputs = Slot(uri=MONTEREY_SCHEMA.has_outputs, name="MaterialProcessing_has_outputs", curie=MONTEREY_SCHEMA.curie('has_outputs'),
                   model_uri=MONTEREY_SCHEMA.MaterialProcessing_has_outputs, domain=MaterialProcessing, range=Union[Union[str, MaterialEntityId], List[Union[str, MaterialEntityId]]])

slots.DataProcessing_has_inputs = Slot(uri=MONTEREY_SCHEMA.has_inputs, name="DataProcessing_has_inputs", curie=MONTEREY_SCHEMA.curie('has_inputs'),
                   model_uri=MONTEREY_SCHEMA.DataProcessing_has_inputs, domain=DataProcessing, range=Optional[Union[Union[str, DataEntityId], List[Union[str, DataEntityId]]]])

slots.DataProcessing_has_outputs = Slot(uri=MONTEREY_SCHEMA.has_outputs, name="DataProcessing_has_outputs", curie=MONTEREY_SCHEMA.curie('has_outputs'),
                   model_uri=MONTEREY_SCHEMA.DataProcessing_has_outputs, domain=DataProcessing, range=Union[Union[str, DataEntityId], List[Union[str, DataEntityId]]])

slots.DataGeneration_has_inputs = Slot(uri=MONTEREY_SCHEMA.has_inputs, name="DataGeneration_has_inputs", curie=MONTEREY_SCHEMA.curie('has_inputs'),
                   model_uri=MONTEREY_SCHEMA.DataGeneration_has_inputs, domain=DataGeneration, range=Optional[Union[Union[str, MaterialEntityId], List[Union[str, MaterialEntityId]]]])

slots.DataGeneration_has_outputs = Slot(uri=MONTEREY_SCHEMA.has_outputs, name="DataGeneration_has_outputs", curie=MONTEREY_SCHEMA.curie('has_outputs'),
                   model_uri=MONTEREY_SCHEMA.DataGeneration_has_outputs, domain=DataGeneration, range=Union[Union[str, DataEntityId], List[Union[str, DataEntityId]]])
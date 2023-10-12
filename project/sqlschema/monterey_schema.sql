

CREATE TABLE "DataEntity" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	type TEXT NOT NULL, 
	PRIMARY KEY (id)
);

CREATE TABLE "DataGeneration" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	type TEXT NOT NULL, 
	has_inputs TEXT, 
	has_outputs TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "DataProcessing" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	type TEXT NOT NULL, 
	has_inputs TEXT, 
	has_outputs TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "MaterialEntity" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	type TEXT NOT NULL, 
	PRIMARY KEY (id)
);

CREATE TABLE "MaterialOrData" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	type TEXT NOT NULL, 
	PRIMARY KEY (id)
);

CREATE TABLE "MaterialProcessing" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	type TEXT NOT NULL, 
	has_inputs TEXT, 
	has_outputs TEXT, 
	PRIMARY KEY (id)
);

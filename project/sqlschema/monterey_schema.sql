

CREATE TABLE "Database" (
	type TEXT NOT NULL, 
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "DataEntity" (
	type TEXT NOT NULL, 
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "DataGeneration" (
	type TEXT NOT NULL, 
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	has_inputs TEXT, 
	has_outputs TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "DataProcessing" (
	type TEXT NOT NULL, 
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	has_inputs TEXT, 
	has_outputs TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "MaterialEntity" (
	type TEXT NOT NULL, 
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "MaterialOrData" (
	type TEXT NOT NULL, 
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "MaterialProcessing" (
	type TEXT NOT NULL, 
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	has_inputs TEXT, 
	has_outputs TEXT, 
	PRIMARY KEY (id)
);

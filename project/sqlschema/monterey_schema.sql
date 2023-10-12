

CREATE TABLE "DataEntity" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	type TEXT NOT NULL, 
	category VARCHAR(5) NOT NULL, 
	PRIMARY KEY (id)
);

CREATE TABLE "DataProcessing" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	type TEXT NOT NULL, 
	category VARCHAR(5) NOT NULL, 
	has_inputs TEXT, 
	has_outputs TEXT NOT NULL, 
	PRIMARY KEY (id)
);

CREATE TABLE "Instrument" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	type TEXT NOT NULL, 
	category VARCHAR(5) NOT NULL, 
	PRIMARY KEY (id)
);

CREATE TABLE "Investigation" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	type TEXT NOT NULL, 
	category VARCHAR(5) NOT NULL, 
	PRIMARY KEY (id)
);

CREATE TABLE "MaterialEntity" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	type TEXT NOT NULL, 
	category VARCHAR(5) NOT NULL, 
	PRIMARY KEY (id)
);

CREATE TABLE "Person" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	type TEXT NOT NULL, 
	category VARCHAR(5) NOT NULL, 
	orcid TEXT NOT NULL, 
	PRIMARY KEY (id)
);

CREATE TABLE "Protocol" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	type TEXT NOT NULL, 
	category VARCHAR(5) NOT NULL, 
	PRIMARY KEY (id)
);

CREATE TABLE "DataGeneration" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	type TEXT NOT NULL, 
	category VARCHAR(5) NOT NULL, 
	used TEXT, 
	followed TEXT, 
	has_inputs TEXT, 
	has_outputs TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(used) REFERENCES "Instrument" (id), 
	FOREIGN KEY(followed) REFERENCES "Protocol" (id)
);

CREATE TABLE "MaterialProcessing" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	type TEXT NOT NULL, 
	category VARCHAR(5) NOT NULL, 
	used TEXT, 
	followed TEXT, 
	has_inputs TEXT, 
	has_outputs TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(used) REFERENCES "Instrument" (id), 
	FOREIGN KEY(followed) REFERENCES "Protocol" (id)
);

CREATE TABLE "Investigation_has_inputs" (
	backref_id TEXT, 
	has_inputs TEXT, 
	PRIMARY KEY (backref_id, has_inputs), 
	FOREIGN KEY(backref_id) REFERENCES "Investigation" (id)
);

CREATE TABLE "Investigation_has_outputs" (
	backref_id TEXT, 
	has_outputs TEXT NOT NULL, 
	PRIMARY KEY (backref_id, has_outputs), 
	FOREIGN KEY(backref_id) REFERENCES "Investigation" (id)
);

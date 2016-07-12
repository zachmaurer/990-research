CREATE TABLE organizations (
	id serial PRIMARY KEY,
	ein integer  UNIQUE NOT NULL,
	name text NOT NULL,
);

CREATE TABLE filings (
	id serial PRIMARY KEY,
	ein integer REFERENCES organizations(ein),
	object_id text UNIQUE NOT NULL,
	url text UNIQUE NOT NULL,	
	tax_period_start  date,
	tax_period_end date,
	tax_year integer,
	form_type text,
);

CREATE TABLE organization_addresses(
	id serial PRIMARY KEY,
	ein integer REFERENCES organizations(ein),
	address1 text,
	address2 text,
	city text,
	state text,
	zip text,
	phone text,
	lat numeric,
	lng numeric,
);

CREATE TABLE grants (
	id serial PRIMARY KEY,
	grantor_id integer REFERENCES organizations(id) NOT NULL,
	amount numeric,
	purpose text,
	grantee_id integer REFERENCES grantees(id) NOT NULL,
);

CREATE TABLE grantees (
	id serial PRIMARY KEY,
	name text NOT NULL,
	address1 text,
	address2 text,
	city text,
	state text,
	country text,
	zip text,
	status text,
	organization_id integer REFERENCES organizations(id),
);
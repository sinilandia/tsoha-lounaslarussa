CREATE TABLE ravintolat (id SERIAL PRIMARY KEY, nimi TEXT, osoite TEXT, puh TEXT, email TEXT, lounashinta TEXT);
CREATE TABLE lounashinta (id SERIAL PRIMARY KEY, nimi TEXT, pvm DATE, peukut INTEGER, ravintola_id INTEGER REFERENCES ravintolat(id));

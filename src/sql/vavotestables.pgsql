--
-- PostgreSQL database dump
--

-- Dumped from database version 9.5.6
-- Dumped by pg_dump version 9.5.6

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: area; Type: TABLE; Schema: public; Owner: mennis
--

CREATE TABLE area (
    id integer NOT NULL,
    name text
);


ALTER TABLE area OWNER TO mennis;

--
-- Name: candidate; Type: TABLE; Schema: public; Owner: mennis
--

CREATE TABLE candidate (
    id integer NOT NULL,
    name text,
    party text
);


ALTER TABLE candidate OWNER TO mennis;

--
-- Name: election; Type: TABLE; Schema: public; Owner: mennis
--

CREATE TABLE election (
    id integer NOT NULL,
    date timestamp without time zone,
    type text,
    winner text
);


ALTER TABLE election OWNER TO mennis;

--
-- Name: votes; Type: TABLE; Schema: public; Owner: mennis
--

CREATE TABLE votes (
    aid integer,
    cid integer,
    eid integer,
    votes integer
);


ALTER TABLE votes OWNER TO mennis;

--
-- Data for Name: area; Type: TABLE DATA; Schema: public; Owner: mennis
--

COPY area (id, name) FROM stdin;
\.


--
-- Data for Name: candidate; Type: TABLE DATA; Schema: public; Owner: mennis
--

COPY candidate (id, name, party) FROM stdin;
\.


--
-- Data for Name: election; Type: TABLE DATA; Schema: public; Owner: mennis
--

COPY election (id, date, type, winner) FROM stdin;
\.


--
-- Data for Name: votes; Type: TABLE DATA; Schema: public; Owner: mennis
--

COPY votes (aid, cid, eid, votes) FROM stdin;
\.


--
-- Name: area_pkey; Type: CONSTRAINT; Schema: public; Owner: mennis
--

ALTER TABLE ONLY area
    ADD CONSTRAINT area_pkey PRIMARY KEY (id);


--
-- Name: candidate_pkey; Type: CONSTRAINT; Schema: public; Owner: mennis
--

ALTER TABLE ONLY candidate
    ADD CONSTRAINT candidate_pkey PRIMARY KEY (id);


--
-- Name: election_pkey; Type: CONSTRAINT; Schema: public; Owner: mennis
--

ALTER TABLE ONLY election
    ADD CONSTRAINT election_pkey PRIMARY KEY (id);


--
-- Name: votes_aid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: mennis
--

ALTER TABLE ONLY votes
    ADD CONSTRAINT votes_aid_fkey FOREIGN KEY (aid) REFERENCES area(id);


--
-- Name: votes_cid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: mennis
--

ALTER TABLE ONLY votes
    ADD CONSTRAINT votes_cid_fkey FOREIGN KEY (cid) REFERENCES candidate(id);


--
-- Name: votes_eid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: mennis
--

ALTER TABLE ONLY votes
    ADD CONSTRAINT votes_eid_fkey FOREIGN KEY (eid) REFERENCES election(id);


--
-- Name: public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- PostgreSQL database dump complete
--


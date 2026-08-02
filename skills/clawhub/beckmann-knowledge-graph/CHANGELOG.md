# Changelog

All notable changes to the Beckmann Knowledge Graph are documented in this file.

The graph and the skill are intended to be iteratively refined. Agents should always check this file and `package.json` for the current version and prefer the latest available version.





## \[3.0.0] - 2026-07-29

This is a major release. The entire skill formulation has been restructured.

### Changed





* **Complete rewrite of skill wording**.



* **Versioning policy**: All versioning information now lives exclusively in this `CHANGELOG.md` file. `SKILL.md` only contains a reference to this file, no hard-coded version numbers.



* **Future-proofing against graph growth**: Removed hard-coded counts (e.g., number of entities, relations, predicate frequencies, `scientific\_status` distributions) from `SKILL.md`. The skill now instructs agents to read counts dynamically from `graph.json`. Where a number is mentioned for illustration, it is explicitly marked as "as of v3.0.0" and should be re-checked.



* **Data model correction**: `graph.json` now canonically uses `scientific\_status` (with underscore) for both entities and relations. `SKILL.md` has been updated to reflect this as primary field, with backward-compatible fallback to `scientific status` (space) for older graphs. `typ` remains the canonical field name (not `type`).





### Graph state as of v3.0.0 

* Entities: 681 (see `graph.json` for exact current count)
* Relations: 1146 (see `graph.json` for exact current count)
* Both entities and relations include `scientific\_status` field
* Entity status distribution: established (224), hypothesis (157), partially established (120), non-existent, purely philosophical (91), metaphor (64), open question (25)
* Relation status distribution: non-existent, purely philosophical (340), metaphor (237), hypothesis (233), partially established (115), established (111), open question (110)









## \[2.4.0]

* Quality update
* As of this version: All relations include a `scientific status` field
* The scientific status values were assigned following analysis by an AI model

## \[2.3.0]

* Quality update
* Duplicate, multiple, and directly inverse relations have been removed
* As of this version: All entities include a `scientific status` field (counts as of this release: \~681 entities — see `graph.json` for current)

## \[2.2.0]

* Over 240 relations were optimized
* AI models were used to generate `descriptions` and verify `predicates`. Approximately 70% of the predicates were improved
* The entire process was automated using Markdown scripts and small HTML programs
* Descriptions underwent human review and minor corrections

## \[2.1.0]

* language and narrative structure as a framework of expectations (topic generated independently by an AI model)
* assessment of expectations and measurement of dominance (topic generated independently by an AI model)
* climate systems as expectation and feedback dynamics (topic generated independently by an AI model)
* music (topic chosen by user, everything else generated independently by an AI model)

## \[2.0.0]

* The first version created in self-improvement mode
* New topics generated independently by an AI model:

  * Game Theory
  * Behavioral Economics / Cognitive Biases
  * Capacity for action and free will
  * Nash equilibria as stabilizers of dominant expectations
* New graph structures created autonomously by an AI model
* "Autonomous" means operating according to a general script that can be reused, further developed, or optimized
* Remaining work automated using small HTML programs

## \[1.4.0]

* Attempt to explain the Beckmann logic in greater detail
* Alan Watts' perspective
* Subsection on problem-solving strategies
* Problem hierarchy

## \[1.3.0]

* stock trading

## \[1.2.0]

* Subsection on "Art" with Albrecht Duerer
* Stockholm syndrome
* The Invisible Gorilla Experiment (1999) by Daniel Simons and Christopher Chabris, Inattentional Blindness 2.0 \& Cognitive Ego Traps, Retrocausal Attention \& Future Meaning (Daryl Bem), Survival-Based Attention \& Threat Avoidance
* Duplicates removed
* Errors corrected

## \[1.1.0]

* first being (limitation: the solvability of all problems in being is connected with the insolubility of the origin of first philosophical being)
* Three-body problem
* Squaring the circle and the goldfish analogy


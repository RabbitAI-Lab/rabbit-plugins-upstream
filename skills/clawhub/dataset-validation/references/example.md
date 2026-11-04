# Worked example: an affiliation delivery

Synthetic data, not real provider information. Intended use: identify current cardiology contacts at facilities A and B as of 2026-11-04. Grain: clinician/location. The reference roster is independently supplied for this example.

| Clinician | Location | Delivered affiliation | Dated reference |
| --- | --- | --- | --- |
| 001 | North | A | B |
| 002 | North | A | A |
| 002 | South | B | B |

The three rows parse, identifiers are present and both facilities appear. The two locations for clinician 002 are legitimate relationships.

One of three delivered affiliation relationships contradicts the reference: clinician 001 belongs to B. Only two of three relationships are verified correct. Both clinicians are represented, so represented-entity coverage and relationship correctness answer different questions.

**Decision:** hold for correction for the stated contact-targeting use. Preserve the original delivery, propose changing clinician 001's affiliation using the dated evidence, and recheck that row and the facility summary. If the reference's independence or date is unknown, record a conflict requiring verification rather than assert that the delivery is false.

The brief connects the defect to contacting the wrong facility. A “100% populated” score would not establish usability.


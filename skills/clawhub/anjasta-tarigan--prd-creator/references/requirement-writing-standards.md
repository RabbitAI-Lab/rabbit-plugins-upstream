# Requirement Writing Standards

Rules for writing Section 6–8 (User Stories, Functional Requirements, Non-Functional Requirements) of a PRD so that every requirement is unique, testable, prioritized, and traceable — this is what separates a PRD from a wishlist.

## 1. Requirement IDs (ISO/IEC/IEEE 29148 traceability)

Every requirement gets a stable, unique ID that never gets reused, even if the requirement is later deleted:

- `REQ-F-###` — functional requirement
- `REQ-NF-###` — non-functional requirement (append category, e.g. `REQ-NF-SEC-001` for security, `REQ-NF-PERF-001` for performance)
- `US-##` — user story
- `AC-###` — acceptance criteria block

IDs are referenced across sections (a user story references its REQ-F IDs; a REQ-F references its AC block) so a reviewer or QA engineer can trace end-to-end from story → requirement → test.

## 2. RFC 2119 keyword discipline

Every requirement sentence uses exactly one of these keywords, capitalized, per RFC 2119, so priority is legible from the sentence itself:

- **MUST / SHALL** — absolute requirement. Non-negotiable for release.
- **SHOULD** — recommended; a valid reason may exist to deviate, but implications must be understood.
- **MAY** — truly optional.

Avoid weak, ambiguous verbs like "will", "can", "is able to" in formal requirement statements — reserve those for narrative sections (Executive Summary, Problem Statement), not the requirements table.

**Bad**: "The system will let users reset their password."
**Good**: "REQ-F-014 — The system SHALL allow an authenticated user to reset their password via a time-limited email link that expires after 15 minutes."

## 3. EARS syntax for conditional/triggered requirements

EARS (Easy Approach to Requirements Syntax) gives five sentence patterns that eliminate the ambiguity of free-form "shall" statements, especially useful for the trigger-heavy logic common in web/mobile apps (form validation, notification triggers, offline sync):

| Pattern | Template | Example |
|---|---|---|
| Ubiquitous | The `<system>` shall `<response>` | The system shall encrypt all data at rest. |
| Event-driven | WHEN `<trigger>`, the `<system>` shall `<response>` | WHEN a user submits an invalid email format, the system shall display an inline validation error. |
| State-driven | WHILE `<state>`, the `<system>` shall `<response>` | WHILE the device is offline, the system shall queue write operations locally. |
| Unwanted behavior | IF `<condition>`, THEN the `<system>` shall `<response>` | IF the payment gateway times out, THEN the system shall retry up to 3 times before surfacing a failure state. |
| Optional feature | WHERE `<feature is included>`, the `<system>` shall `<response>` | WHERE push notifications are enabled, the system shall request notification permission on first relevant action, not on app launch. |

Use the event-driven and state-driven patterns heavily for mobile (connectivity, permissions, background states) and web (form/session states).

## 4. Acceptance criteria (Given–When–Then)

Every user-facing functional requirement gets at least one acceptance criteria block in Gherkin-style Given–When–Then, so QA and engineering share one definition of "done" for that requirement:

```
AC-014
Given a user has requested a password reset link
When they click the link within 15 minutes of request
Then they are shown a new-password form
And the previous link is invalidated after use

AC-015
Given a user has requested a password reset link
When they click the link after 15 minutes have elapsed
Then they are shown an "expired link" message with an option to request a new one
```

Always include at least one "unhappy path" AC (error/edge case) alongside the happy path — a requirement with only a happy-path AC is under-specified.

## 5. Prioritization: MoSCoW and RICE

Use **MoSCoW** as the primary column in the requirements table for at-a-glance release scoping:

- **Must have** — release fails without it.
- **Should have** — important but not release-blocking; painful to omit.
- **Could have** — desirable, first to be cut if time-constrained.
- **Won't have (this time)** — explicitly deferred, stated to prevent re-litigation.

Use **RICE scoring** (Reach × Impact × Confidence ÷ Effort) as a secondary, numeric method when stakeholders disagree on relative priority within the "Should"/"Could" bands, or when the backlog has more Must-haves than fit the timeline and a data-informed cut is needed:

- **Reach**: how many users/events per time period this affects.
- **Impact**: effect per user when they encounter it (e.g. 3 = massive, 2 = high, 1 = medium, 0.5 = low, 0.25 = minimal).
- **Confidence**: % confidence in the Reach/Impact estimates.
- **Effort**: person-months/weeks to build.
- **RICE score** = (Reach × Impact × Confidence) ÷ Effort — higher score = higher priority.

## 6. INVEST for user stories

Every user story in Section 6 should satisfy:

- **I**ndependent — can be built/shipped without hard-depending on another unbuilt story.
- **N**egotiable — describes intent, not a rigid spec (the linked REQ-F carries the rigid spec).
- **V**aluable — delivers clear value to the persona, not just a technical task.
- **E**stimable — the team can size it.
- **S**mall — fits in a single iteration/sprint.
- **T**estable — has clear pass/fail conditions (its linked AC blocks).

If a story fails "Small" or "Independent," split it before adding it to the PRD rather than leaving an oversized story that will need to be re-split during planning anyway.

## 7. Definition of Ready (before drafting requirements) / Definition of Done (before finalizing PRD)

**Definition of Ready** — don't start writing Section 7 (Functional Requirements) until:
- [ ] Personas and core problem are confirmed with the user (Sections 2 and 4 drafted and not contested).
- [ ] Scope boundaries (Section 5, in/out) are explicit, not implied.
- [ ] Platform target (web/mobile/full-stack) is confirmed, so irrelevant template sections are dropped rather than left as stubs.

**Definition of Done** — don't present the final PRD as complete until:
- [ ] Every user story links to at least one REQ-F ID, and every REQ-F links to at least one AC block.
- [ ] Every requirement uses a single RFC 2119 keyword — no "will"/"can" in the requirements tables.
- [ ] Every metric in Section 3 has a corresponding analytics event in Section 15.
- [ ] Section 19 (Open Questions) exists and is either empty or has an owner + target date for every row — no orphaned unresolved questions.
- [ ] Non-functional requirements (Section 8) cover all listed categories explicitly, none silently skipped.
- [ ] Irrelevant platform-specific sections (Web-only vs. Mobile-only) are removed rather than left empty.

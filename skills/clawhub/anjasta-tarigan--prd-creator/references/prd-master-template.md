# PRD Master Template — Full-Stack Web & Mobile

This is the section-by-section structure to fill in when drafting a PRD with the `prd-creator` skill. Every section below states its purpose and what "good" looks like. Sections marked **[Web]** or **[Mobile]** only apply when that platform is in scope; sections marked **[Full-stack]** apply whenever both share a backend.

Copy this structure into the output `.md` file and replace guidance text with real content. Do not leave a section as a placeholder — if a section genuinely doesn't apply, delete it and note the omission in Section 0 (Document Control) rather than leaving an empty header.

---

## 0. Document Control

| Field | Value |
|---|---|
| Document title | |
| Version | 0.1 (Draft) |
| Status | Draft / In Review / Approved |
| Author(s) | |
| Date created | |
| Last updated | |
| Reviewers / approvers | |
| Related documents | (link parent PRD, design files, architecture decision records) |

## 1. Executive Summary (PR/FAQ style)

Write this **as if the product has already launched successfully** (Amazon Working Backwards style), then follow with an FAQ. This section is read by the most people and decides whether the rest gets read.

- **Press release (150–250 words)**: headline, sub-headline, then continuous prose (no field labels inline) covering: who the user is, what problem they had, how this product solves it, what's meaningfully different vs. alternatives, 1–2 concrete usage scenarios, and launch availability. Do not fabricate quotes attributed to real people; a plausible "a typical user" quote is fine as illustrative narrative, clearly framed as illustrative.
- **Internal FAQ** — answer from three angles, concisely and honestly (don't hide uncertainty):
  - *User*: Who is this for? What do they do today without it? What's the #1 reason they'd stop using it?
  - *Business*: Why now? What's the cost of not building this? How is success measured?
  - *Execution*: What's the biggest technical risk? What are we explicitly NOT building in v1?

## 2. Problem Statement

- Current state / pain point, backed by evidence where available (user feedback, support tickets, data, competitor gap).
- Who experiences this problem and how often.
- Cost of inaction (business or user cost of not solving this).

## 3. Goals, Non-Goals & Success Metrics

- **Goals**: 3–5 measurable outcomes (tie to a framework like OKRs if the org uses one).
- **Non-goals**: explicitly out of scope for this version — this is the single highest-leverage section for preventing scope creep; be specific, not just "other stuff is out of scope."
- **Success metrics**: leading indicators (adoption, activation, task completion) and lagging indicators (retention, revenue, satisfaction). Each metric needs a target number and a measurement method — a metric without a number is an aspiration, not a metric.

## 4. Personas & User Segments

For each persona: name/archetype, context of use, primary job-to-be-done, technical proficiency, device/platform (relevant for mobile: OS version, connectivity quality — e.g. intermittent connectivity assumptions).

## 5. Scope

- **In scope** for this version (bullet list, unambiguous).
- **Out of scope** for this version (explicitly list adjacent features that were considered and deferred, with a one-line reason each — this prevents the same debate resurfacing later).
- **Future considerations** (v2+, not committed).

## 6. User Stories & Use Cases

Write as INVEST-compliant stories (see `requirement-writing-standards.md`) grouped by epic/feature area. Each story links forward to one or more Functional Requirement IDs in Section 7 — a story with no linked REQ-ID is not implementable yet.

Format: `As a [persona], I want [capability], so that [outcome].`

## 7. Functional Requirements

Table format, one row per atomic, testable requirement. See `requirement-writing-standards.md` for ID scheme, RFC 2119 keyword usage, and EARS syntax.

| ID | Requirement (shall statement) | Priority (MoSCoW) | Source/Story | Acceptance Criteria ref |
|---|---|---|---|---|
| REQ-F-001 | The system shall ... | Must | US-01 | AC-001 |

Group by feature area with `###` sub-headers (e.g. Authentication, Onboarding, Core Workflow, Notifications, Admin/Backoffice).

## 8. Non-Functional Requirements

Cover each category explicitly — do not merge into one vague "performance and security" paragraph:

- **Performance**: response time targets (e.g. p95 API latency), throughput, load expectations.
- **Scalability**: expected growth curve, horizontal/vertical scaling assumptions.
- **Availability & Reliability**: uptime target (e.g. 99.9%), acceptable downtime windows, backup/recovery (RPO/RTO).
- **Security**: authN/authZ model, data-at-rest/in-transit encryption, OWASP Top 10 considerations, secrets management.
- **Privacy & Compliance**: data retention, applicable regulation (e.g. GDPR/UU PDP if handling Indonesian user data), consent flows.
- **Accessibility**: target conformance level (e.g. WCAG 2.2 AA) — **[Web]** especially, but also applies to mobile UI.
- **Localization/Internationalization**: supported languages, date/number formats, RTL if applicable.
- **Maintainability & Observability**: logging, monitoring, error-tracking expectations.
- **Resource constraints**: if the deployment target is resource-limited (e.g. self-hosted on modest hardware, CPU-only inference), state the constraint explicitly here so it becomes a binding NFR, not an afterthought during implementation.

Use the same REQ-NF-### ID scheme as functional requirements.

## 9. System Architecture Overview **[Full-stack]**

- High-level component diagram description (frontend, backend/API, database, external services, queues/workers if any).
- Key architectural decisions and rationale (e.g. monolith vs. services, sync vs. async processing, chosen DB and why).
- Third-party/external dependencies and their failure-mode implications.

## 10. Data Model **[Full-stack]**

- Core entities and relationships (can be described as a table or ER-style list: entity, key fields, relationships, ownership/multi-tenancy notes).
- Data lifecycle: creation, retention, deletion/archival rules.

## 11. API Contracts **[Full-stack]**

- Endpoint inventory (method, path, purpose, auth requirement) — full request/response schemas can live in a linked OpenAPI spec rather than duplicated here; reference it.
- Versioning strategy (e.g. URI versioning, header versioning) and backward-compatibility policy.
- Rate limiting / abuse prevention expectations.

## 12. Web-Specific Requirements **[Web]**

- **Browser support matrix**: browsers + minimum versions supported (state the policy, e.g. "last 2 major versions of Chrome/Edge/Firefox/Safari").
- **Responsive breakpoints**: target breakpoints (mobile web, tablet, desktop) and behavior at each.
- **SEO requirements** (if public-facing): metadata, SSR/SSG strategy, sitemap/robots.
- **Progressive Web App / offline behavior** (if applicable).

## 13. Mobile-Specific Requirements **[Mobile]**

- **Platform & OS version support**: minimum iOS/Android version, target SDK, device tiers (low-end device support if relevant).
- **Offline behavior**: what functions must work offline, sync/conflict-resolution strategy on reconnect.
- **Push notifications**: triggers, opt-in flow, payload/deep-link behavior.
- **Permissions**: which device permissions are requested, when, and the fallback if denied.
- **App store compliance**: relevant App Store Review Guidelines / Google Play policy considerations (in-app purchases, data safety disclosures, permission justification) — flag anything that needs legal/compliance review before submission.
- **Background execution & battery**: any background tasks (sync, location, BLE) and their battery-impact mitigation.

## 14. UX/UI Requirements

- Link to design files/wireframes/prototypes (do not re-describe visual design in prose if a linked design file exists — link, don't duplicate).
- Key interaction flows/states that must exist regardless of visual design: empty states, loading states, error states, permission-denied states.

## 15. Analytics & Instrumentation

- Events to track (name, trigger, properties) mapped back to the Success Metrics in Section 3 — every metric in Section 3 needs at least one corresponding event here, or it can't actually be measured.

## 16. Risks, Assumptions, Dependencies (RAID)

| Type | Description | Impact | Likelihood | Mitigation/Owner |
|---|---|---|---|---|
| Risk | | | | |
| Assumption | | | | |
| Dependency | | | | |

## 17. Rollout & Release Plan

- Phasing strategy (feature flags, staged rollout %, beta cohort, full GA).
- Rollback plan if a critical issue is found post-release.
- Communication plan (internal announcement, changelog, user-facing release notes) if relevant.

## 18. Testing & Acceptance Criteria

- Test strategy summary (unit/integration/E2E ownership, manual QA scope).
- Acceptance criteria in Given–When–Then form, one block per requirement that needs it (see `requirement-writing-standards.md`), collected here or linked per-requirement.
- Definition of Done for this release.

## 19. Open Questions

Table of unresolved questions, owner, and target resolution date. A PRD can go to review with open questions, but never to final Approved status with unresolved ones still listed.

## 20. Appendix / Glossary

- Term definitions, acronym expansions, links to supporting research/data.

## 21. Approval Sign-off

| Role | Name | Decision | Date |
|---|---|---|---|
| Product Owner | | | |
| Engineering Lead | | | |
| Design Lead | | | |
| QA Lead | | | |

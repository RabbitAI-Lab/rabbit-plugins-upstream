## Description:

Scaffold and methodology for building a WeChat Mini Program on WeChat CloudBase with single-function REST routing, idempotent user and collection seeding, real-time stats, subscription messages, scheduled triggers, and lifecycle pitfalls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vincent-chao-lang](https://clawhub.ai/user/vincent-chao-lang)

### License/Terms of Use:

MIT

## Use Case:

Developers and small teams use this skill to turn a WeChat Mini Program idea into a CloudBase-backed scaffold with login, data access, optional subscription reminders, and a handoff path for deployment. It is most useful for MVPs and tool-style mini programs where CloudBase is an acceptable backend choice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: CloudBase usage can introduce platform lock-in and variable operating costs.

Mitigation: Confirm CloudBase cost and lock-in are acceptable before production use, and choose a self-hosted backend when requirements include complex transactions, large joins, high concurrency, or strict cost control.

Risk: Unpinned wx-server-sdk dependency ranges can reduce reproducibility.

Mitigation: Pin wx-server-sdk versions in generated cloud function package files when reproducible builds or controlled upgrades matter.

Risk: The scaffold can automatically add first-login users to public groups, which may affect privacy expectations.

Mitigation: Review and adjust the first-login membership behavior before launch so it matches the product's privacy model and user-facing expectations.

Risk: Subscription message delivery depends on AppID-bound template IDs and exact keyword field names.

Mitigation: Apply a template ID for the target AppID, keep frontend and cloud function template IDs aligned, verify keyword field names against the approved template, and test a real push before release.

Risk: Cloud database collections and indexes can be missed because CloudBase does not provide strong schema enforcement.

Mitigation: Keep the collection list synchronized with code, run the idempotent seed function before testing, and manually create required unique indexes for concurrency-sensitive writes.

## Reference(s):

- [Architecture and Data Model](references/architecture.md)
- [Lifecycle Pitfalls](references/pitfalls.md)

## Skill Output:

**Output Type(s):** [guidance, code, shell commands, configuration]

**Output Format:** [Markdown guidance with JavaScript and JSON scaffold templates plus inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a project scaffold pattern and implementation guidance; deployment is delegated to a companion deployment skill.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

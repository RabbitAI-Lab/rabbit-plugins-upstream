## Description:

Use for bounded KaleidoSphere status, discovery, analyze, plan, preview, readback, or advisory BI presentation review; reject unsafe authority.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jofe2](https://clawhub.ai/user/jofe2)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and BI operators use this skill to validate and route bounded KaleidoSphere requests for status, discovery, analysis, planning, preview, readback, and advisory BI presentation review while preserving clear authority limits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A request could try to exceed the closed KaleidoSphere action set or include unsafe fields such as SQL, credentials, raw rows, arbitrary URLs, provider payloads, or mutation operations.

Mitigation: Validate every request with artifact/scripts/validate-request.mjs and refuse unknown actions, unknown fields, unsafe keys, and write/delete/deploy paths.

Risk: A user could provide an endpoint, secret, or transport workaround that bypasses the trusted host configuration.

Mitigation: Use only an already configured trusted KaleidoSphere transport; if none exists, stop with WAITING_EXTERNAL for the missing dependency.

Risk: Presentation or visual review could be mistaken for approval of data truth, provenance, accessibility, production readiness, or deployment readiness.

Mitigation: Keep visual guidance advisory and verify data, claims, provenance, evidence binding, accessibility, production readiness, and deployment readiness independently.

Risk: Plan or preview output could be treated as authorization to make persistent BI changes.

Mitigation: State that persistent changes still require exact trusted-UI approval, BI-Control apply, independent readback, and rollback.

## Reference(s):

- [KaleidoSphere contract](artifact/references/contract.json)
- [ClawHub skill page](https://clawhub.ai/jofe2/skills/kaleidosphere)
- [Publisher profile](https://clawhub.ai/user/jofe2)

## Skill Output:

**Output Type(s):** [Markdown, JSON, Guidance, Shell commands]

**Output Format:** [Markdown with closed JSON request objects and validation status]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Separates observed facts, computed facts, inferred candidates, and human decisions when present; uses WAITING_EXTERNAL only for a missing trusted transport or external evidence.]

## Skill Version(s):

0.18.2 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

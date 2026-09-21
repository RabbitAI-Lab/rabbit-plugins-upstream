## Description:

Production cinema ticketing catalog that maps cinema identities to installable OpenClaw mode capabilities for capture, replay, coupon binding, and failure handling.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rascalagnt001](https://clawhub.ai/user/rascalagnt001)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill as a Cinema Agent catalog layer to route orders, capture sessions, and replay requests to the correct cinema entry and installable mode package.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Separate mode packages perform the actual capture, replay, coupon, page-world, and failure-handling work.

Mitigation: Review each child mode package separately before use, especially when it will handle live orders, coupons, browser sessions, or business credentials.

Risk: Some catalog entries reference mode packages marked plugin_required.

Mitigation: Confirm the referenced mode package is installed and exposes the declared capabilities before dispatching an entry.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/rascalagnt001/skills/cinema-suite)
- [README.md](artifact/README.md)
- [cinema-suite.json](artifact/cinema-suite.json)

## Skill Output:

**Output Type(s):** [JSON, Configuration, Guidance]

**Output Format:** [JSON catalog entries with Markdown operational guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Defines 62 redacted cinema entries and 9 mode capability mappings; executable mode packages are installed separately.]

## Skill Version(s):

1.0.0 (source: evidence release metadata and package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

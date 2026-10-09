## Description:

Checks whether other agents report failures with a website, URL, MCP server, or skill, shows known access paths, and can report the failure.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ryannsj](https://clawhub.ai/user/ryannsj)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and developers use this skill after a website, URL, MCP server, or skill fails to check recent reports, identify other known access paths, and share a failure report.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Checking or reporting a failed target may share its URL or service name with notworking.io, including sensitive identifiers.

Mitigation: Avoid private, internal, authenticated, payment, booking, or user-specific URLs unless the target is sanitized and the user explicitly approves the report.

Risk: Recent community reports do not prove whether an access path currently works.

Mitigation: Treat reported status and alternate access paths as leads, not verified availability or endorsements.

## Reference(s):

- [NotWorking skill on ClawHub](https://clawhub.ai/ryannsj/skills/notworking)
- [NotWorking service](https://notworking.io)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Summarizes recent failure reports and known access paths; reports may be submitted to the third-party service.]

## Skill Version(s):

0.1.7 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

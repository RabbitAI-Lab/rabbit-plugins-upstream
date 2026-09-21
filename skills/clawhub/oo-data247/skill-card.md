## Description:

Data247 helps agents operate the Data247 connector through an OOMOL-connected account for phone verification, Do-Not-Call checks, carrier lookup, balance checks, and gender append actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to run Data247 account and phone-data actions through OOMOL's connected account flow without handling raw API credentials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup instructions include remote installer scripts run through a shell without verification.

Mitigation: Review the oo CLI installation source before installing, prefer a verified package or installer with checksum or signature validation, and avoid running setup steps unless an auth or connection failure requires them.

Risk: Data247 actions that change data or spend account balance can affect the connected account.

Mitigation: Confirm the exact action, payload, and expected effect with the user before allowing write actions or balance-affecting operations to run.

## Reference(s):

- [Data247 homepage](https://www.data247.com/)
- [oo CLI repository](https://github.com/oomol-lab/oo-cli)
- [Data247 skill listing](https://clawhub.ai/oomol/skills/oo-data247)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Inspect the live connector schema before building payloads and confirm write or destructive actions before execution.]

## Skill Version(s):

1.0.4 (source: server release and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

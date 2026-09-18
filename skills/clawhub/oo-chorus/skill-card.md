## Description:

Chorus (chorus.ai). Use this skill for searching and reading Chorus data through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Chorus connector schemas and retrieve conversations, teams, scorecards, engagements, and current-user details through an authenticated OOMOL account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include running remote installer scripts directly in a shell without verification.

Mitigation: Install the oo CLI only through a trusted OOMOL channel and prefer checksum or signature validation before executing installer content.

Risk: Connector use depends on an authenticated OOMOL account and a connected Chorus integration.

Mitigation: Run setup or reconnection steps only after an auth or connection error, and confirm the expected account and Chorus connection before retrying.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-chorus)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [Chorus Homepage](https://www.chorus.ai)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with oo CLI command examples and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses include a data object and meta.executionId when actions are run with --json.]

## Skill Version(s):

1.0.3 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Vida lets an agent read Vida account, usage, task, and task statistics data through an OOMOL-connected account using the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to let an agent retrieve Vida account details, daily usage counts, task details, task statistics, and task listings from an OOMOL-connected Vida account without handling raw tokens.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read Vida account and task data through the user's OOMOL-connected account.

Mitigation: Install it only when this account-level read access is intended, and rely on the documented read-only action set for normal use.

Risk: Connector input and output schemas may change over time.

Mitigation: Inspect the live action schema with the oo CLI before constructing each connector payload.

Risk: First-time setup may require installing the oo CLI, signing in, connecting Vida, or resolving billing failures.

Mitigation: Run setup or recovery steps only after the corresponding command failure and review the external install, authentication, connection, or billing step before proceeding.

## Reference(s):

- [Vida homepage](https://vida.io/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub Vida skill page](https://clawhub.ai/oomol/skills/oo-vida)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector actions return JSON responses with data and meta.executionId; the skill instructs the agent to inspect the live action schema before building payloads.]

## Skill Version(s):

1.0.0 (source: server release metadata and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

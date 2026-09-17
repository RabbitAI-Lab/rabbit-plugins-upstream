## Description:

Provides an agent workflow for read-oriented Pipedream lookups through the OOMOL oo CLI and a connected Pipedream account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Pipedream app, user, workflow, event, and workspace data from connected accounts while relying on live connector schemas before each action.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup includes remote installer commands for the oo CLI.

Mitigation: Avoid letting an agent run installer commands automatically; install the CLI yourself through a verified, versioned method before using the skill.

Risk: The skill operates through an OOMOL-connected Pipedream account.

Mitigation: Use it primarily for the documented read-only lookups and confirm exact payloads and effects before any future write or destructive action is executed.

## Reference(s):

- [Pipedream homepage](https://pipedream.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance]

**Output Format:** [Markdown instructions with shell command examples and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector action responses are JSON objects containing data and meta.executionId when commands run successfully.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

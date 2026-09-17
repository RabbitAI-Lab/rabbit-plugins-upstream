## Description:

ASIN Data API enables agents to use the ASIN Data API through the OOMOL `oo` CLI for reading collection data and managing destinations or collection requests.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to inspect ASIN Data API action schemas, run read actions, and manage destinations or collection requests through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote shell installer commands that could be unsafe if used without verification.

Mitigation: Use verified OOMOL CLI installation documentation or a signed/package-manager release before installing.

Risk: Write and destructive actions can update or delete ASIN Data API account data.

Mitigation: Confirm the exact payload, target, and expected effect with the user before running update or delete actions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-asin-data-api)
- [ASIN Data API Homepage](https://www.asindataapi.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce `oo connector schema` and `oo connector run` commands; write and destructive actions require explicit user confirmation.]

## Skill Version(s):

1.0.3 (source: server evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

EspoCRM (espocrm.com). Use this skill for ANY EspoCRM request: reading, creating, updating, and deleting data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and business users can use this skill to inspect EspoCRM action schemas and run record, metadata, and user actions through the OOMOL `oo` CLI. It supports reading records and metadata, plus confirmed create, update, and delete operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands for the `oo` CLI.

Mitigation: Prefer an official, version-pinned installation path with verification instead of running remote installer commands blindly.

Risk: Create and update actions can change EspoCRM records.

Mitigation: Inspect the live action schema, confirm the exact JSON payload and expected effect with the user, then run the write action.

Risk: Delete actions can remove EspoCRM records.

Mitigation: Confirm the target entity and record identifier and obtain explicit approval before running destructive actions.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/oomol/skills/oo-espocrm)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [EspoCRM homepage](https://www.espocrm.com/)
- [oo CLI repository](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, API Calls, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads or responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses `oo connector schema` before action payload construction and `oo connector run --json` for execution.]

## Skill Version(s):

1.0.3 (source: server evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

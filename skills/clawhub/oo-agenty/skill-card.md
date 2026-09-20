## Description:

Agenty (agenty.com). Use this skill for ANY Agenty request - reading, creating, updating, and deleting data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Agenty agents, jobs, lists, web capture, and extraction workflows through an OOMOL-connected Agenty account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create, update, stop, or delete Agenty resources and list data through the connected account.

Mitigation: Confirm exact payloads and effects before write actions, and require explicit approval for destructive actions.

Risk: First-time setup includes remote installer commands for the oo CLI.

Mitigation: Use verified official oo CLI installation instructions before running installer commands.

Risk: Connector action inputs may change over time.

Mitigation: Inspect the live action schema with `oo connector schema` before building or running payloads.

## Reference(s):

- [Agenty homepage](https://agenty.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-agenty)
- [Publisher profile](https://clawhub.ai/user/oomol)
- [Skill icon](https://static.oomol.com/logo/third-party/Agenty.svg)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include command responses, job metadata, logs, result rows, exports, screenshots, PDFs, and downloaded files returned by Agenty actions.]

## Skill Version(s):

1.0.4 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

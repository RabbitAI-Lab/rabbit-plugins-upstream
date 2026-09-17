## Description:

ProcessPlan helps agents read, create, and update ProcessPlan data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and teams use this skill to let an agent inspect ProcessPlan connector schemas, list assigned tasks, list process instances and templates, and start a process after confirming write payloads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup instructions include remote installer commands that execute changing code on the user's machine.

Mitigation: Use a pinned, vendor-documented install method with checksum or signature verification, and do not let an agent run curl-to-bash or PowerShell iex installers automatically.

Risk: The start_process action changes ProcessPlan state.

Mitigation: Inspect the live action schema, show the exact payload and expected effect, and get user confirmation before running the write action.

## Reference(s):

- [ProcessPlan homepage](https://processplan.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ProcessPlan ClawHub skill page](https://clawhub.ai/oomol/skills/oo-processplan)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schema inspection before constructing action payloads.]

## Skill Version(s):

1.0.2 (source: artifact metadata and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

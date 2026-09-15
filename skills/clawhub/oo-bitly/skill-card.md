## Description:

Operate Bitly through the OOMOL oo CLI to read Bitlink, group, and user details, list groups, create short links, and update existing Bitlinks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to let an agent perform Bitly account actions through an authenticated OOMOL connection while inspecting live action schemas before requests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes remote installer commands that execute downloaded shell or PowerShell scripts.

Mitigation: Install or update the OOMOL CLI only after independently verifying the installer source, or use a trusted installation channel before running Bitly actions.

Risk: The skill can update existing Bitlinks through a state-changing action.

Mitigation: Confirm the exact update_bitlink payload and expected effect with the user before execution.

## Reference(s):

- [ClawHub Bitly Skill](https://clawhub.ai/oomol/skills/oo-bitly)
- [Bitly](https://bitly.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands inspect live Bitly connector schemas before executing read or write actions.]

## Skill Version(s):

1.0.2 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

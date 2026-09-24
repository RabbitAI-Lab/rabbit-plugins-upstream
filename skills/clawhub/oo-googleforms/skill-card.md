## Description:

Enables agents to read, create, and update Google Forms through the OOMOL Google Forms connector and oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, employees, and external users use this skill to manage Google Forms through an OOMOL-connected account, including form creation, retrieval, response listing, publishing settings, and batch updates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup path includes remote installer commands for the oo CLI.

Mitigation: Install the oo CLI only after independently trusting OOMOL and verifying the installer through official OOMOL documentation.

Risk: Write actions can create or modify Google Forms through the connected account.

Mitigation: Confirm the exact payload and expected effect with the user before running actions tagged as write operations.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-googleforms)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Google Forms](https://workspace.google.com/products/forms/)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads; write actions require user confirmation before execution.]

## Skill Version(s):

1.0.4 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

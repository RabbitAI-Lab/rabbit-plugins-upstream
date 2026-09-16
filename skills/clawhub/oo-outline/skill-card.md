## Description:

Outline (getoutline.com). Use this skill for Outline requests that involve searching and reading data through the OOMOL-connected oo CLI workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to let an agent retrieve and search Outline collections and documents through an OOMOL-connected Outline account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup flow includes remote shell installer commands for the oo CLI.

Mitigation: Review and install the oo CLI through a trusted method yourself before allowing an agent to use the skill.

Risk: Using the skill routes Outline workspace access through OOMOL-mediated connector execution.

Mitigation: Use the skill only when that access model is acceptable for the workspace, and confirm authentication or connection setup steps manually.

## Reference(s):

- [ClawHub Outline skill page](https://clawhub.ai/oomol/skills/oo-outline)
- [Outline homepage](https://www.getoutline.com)
- [oo CLI repository](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only Outline connector actions return JSON data with execution metadata.]

## Skill Version(s):

1.0.3 (source: server evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

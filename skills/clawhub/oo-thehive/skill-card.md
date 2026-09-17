## Description:

TheHive helps agents operate TheHive 4 through an OOMOL-connected account for reading, creating, and updating alerts and cases.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, security analysts, and operations teams use this skill to inspect TheHive connector schemas and run OOMOL-mediated actions for TheHive alerts and cases. It supports read actions directly and requires user confirmation before state-changing actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that could execute arbitrary code if the distribution path is compromised or unverified.

Mitigation: Install the oo CLI only through trusted, verified, versioned, or package-manager instructions before using the skill.

Risk: The skill can create and update TheHive data through OOMOL connector actions after confirmation.

Mitigation: Inspect live action schemas and confirm exact payloads and effects with the user before state-changing actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-thehive)
- [TheHive homepage](https://thehive-project.org)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown instructions with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before action execution; read actions can run directly, and write actions require confirmation.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

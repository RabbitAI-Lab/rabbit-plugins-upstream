## Description:

Helps an agent read public Indiegogo creator and crowdfunding project data through OOMOL's oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill when an agent needs to inspect public Indiegogo creators, crowdfunding project details, or active crowdfunding campaigns without calling the Indiegogo API directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup instructions include remote installer commands.

Mitigation: Review the setup instructions before installing and prefer a verified package, signed release, or manually inspected installer.

Risk: Connector actions depend on the live OOMOL oo CLI action schema.

Mitigation: Inspect the action schema with `oo connector schema` before constructing a payload.

## Reference(s):

- [Indiegogo homepage](https://www.indiegogo.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-indiegogo)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The connector returns JSON data with execution metadata when actions are run.]

## Skill Version(s):

1.0.2 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

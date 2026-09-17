## Description:

LinkedIn (linkedin.com). Use this skill for ANY LinkedIn request - reading, creating, updating, and deleting data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and operators use this skill to interact with LinkedIn through an OOMOL-connected account, including reading the current member profile and creating, resharing, or deleting posts after checking the live connector schema.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes remote installer commands for the oo CLI.

Mitigation: Review the installation path before use and prefer a pinned, verified release or package manager.

Risk: The skill can create public LinkedIn posts or delete posts from the connected account.

Mitigation: Confirm the exact payload, target account, and target post before allowing write or destructive actions.

Risk: Connector contracts may change over time.

Mitigation: Inspect the live action schema before constructing each payload.

## Reference(s):

- [ClawHub LinkedIn Skill](https://clawhub.ai/oomol/skills/oo-linkedin)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [LinkedIn](https://www.linkedin.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schema inspection before constructing action payloads.]

## Skill Version(s):

1.0.4 (source: evidence release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

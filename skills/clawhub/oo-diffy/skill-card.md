## Description:

Diffy lets an agent search and read Diffy visual testing projects, comparisons, and screenshot results through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and QA engineers use this skill to let an agent inspect Diffy projects, screenshot sets, and visual comparison results from an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The agent may read Diffy project, screenshot, and comparison data available to the connected OOMOL account.

Mitigation: Use the skill only with accounts whose Diffy data the agent is allowed to inspect, and keep actions limited to the documented read-only get and list operations.

Risk: First-time setup may require running an external OOMOL CLI installer.

Mitigation: Review the OOMOL installer before allowing the one-time setup command.

## Reference(s):

- [ClawHub Diffy skill page](https://clawhub.ai/oomol/skills/oo-diffy)
- [Diffy homepage](https://diffy.website/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown with inline bash commands and JSON response details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Primarily read-only Diffy project, screenshot, and visual comparison data.]

## Skill Version(s):

1.0.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

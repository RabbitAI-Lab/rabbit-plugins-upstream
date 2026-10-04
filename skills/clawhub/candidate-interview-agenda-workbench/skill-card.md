## Description:

Builds a Markdown interview agenda from a supplied candidate interview plan.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Recruiters and interview panels use this skill to turn a candidate's role-focused topic plan into a shareable interview agenda.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The operation creates or updates a local agenda file.

Mitigation: Use a dedicated writable output directory and review its contents before running.

Risk: Extra interview-plan fields can influence the generated agenda identifier.

Mitigation: Avoid including unnecessary sensitive data in extra interview-plan fields.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/wxt-ai/skills/candidate-interview-agenda-workbench)

## Skill Output:

**Output Type(s):** [Markdown, Files]

**Output Format:** [JSON agenda artifact with Markdown text; local Markdown file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns an agenda identifier and candidate reference; creates or updates a file in the supplied output directory.]

## Skill Version(s):

1.1.0 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Researches agent runtime and coding-agent releases to explain their architecture, verified facts, ecosystem impact, and unresolved questions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[haiyangchenbj](https://clawhub.ai/user/haiyangchenbj)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, researchers, and platform teams use this skill to assess agent runtime releases, compare platforms, and separate sourced facts from judgments about ecosystem impact.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The source has malformed version metadata, which could confuse release identification.

Mitigation: Confirm the version against the server-resolved release before installation.

Risk: The skill requests Chinese output, which may not match a user's language preference.

Mitigation: Confirm the preferred output language before using the generated analysis.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/haiyangchenbj/skills/agent-runtime-impact-research)
- [Fact Table Schema](references/fact-table-schema.md)
- [Impact Layers Analysis](references/impact-layers.md)

## Skill Output:

**Output Type(s):** [Markdown, Guidance]

**Output Format:** [Markdown research report with a fact table and source register]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Explains runtime flow and layered impact; separates sourced facts, judgments, and uncertainties.]

## Skill Version(s):

1.0.4 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

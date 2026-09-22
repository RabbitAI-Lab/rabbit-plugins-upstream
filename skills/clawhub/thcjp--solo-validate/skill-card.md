## Description:

Evaluates startup ideas with S.E.E.D. niche checks, Manifest alignment, Devil's Advocate inversion, STREAM six-layer analysis, stack selection, and PRD generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

External developers, founders, and product builders use this agent skill to test startup ideas before building. It searches supporting evidence, scores niche viability, identifies failure modes, selects an implementation stack, and prepares a PRD.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release security summary says the skill can create docs/prd.md even though the manifest advertises read access.

Mitigation: Review the skill before installing, and run it only in repositories where creating or overwriting docs/prd.md is acceptable.

Risk: The security guidance notes that the skill may read project or knowledge-base Markdown and use web research during validation.

Mitigation: Use it in a workspace where those reads and searches are appropriate for the startup idea being evaluated.

## Reference(s):


## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Configuration]

**Output Format:** [Markdown summary and PRD Markdown file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create docs/prd.md in the current project.]

## Skill Version(s):

1.0.1 (source: server release metadata; artifact frontmatter states 2.1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

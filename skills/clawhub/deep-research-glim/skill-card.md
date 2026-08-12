## Description:

Conducts deep, multi-angle research using glim MCP tools and parallel subagents. Use for deep research, competitive landscape analysis, strategic intelligence, or /deep-research-glim [topic]. Triggers - deep research, deep dive on, competitive landscape, strategic intelligence, multi-source synthesis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tenequm](https://clawhub.ai/user/tenequm)

### License/Terms of Use:

Apache 2.0

## Use Case:

Developers, analysts, and strategy teams use this skill to run deep research, competitive landscape analysis, strategic intelligence, and multi-source synthesis on a user-provided topic.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow intentionally performs web-oriented research and may generate multiple network queries through glim tools and subagents.

Mitigation: Use the skill for topics where multi-source research is desired, keep the research scope explicit, and review source citations before acting on findings.

Risk: Broad research phrasing could trigger a longer workflow than intended.

Mitigation: Prefer the explicit /deep-research-glim [topic] command and confirm ambiguous topics before spawning subagents.

Risk: Strategic synthesis can include weakly supported claims when source quality is uneven.

Mitigation: Apply the skill's coverage validation, contradiction checks, and source annotation requirements before using recommendations downstream.

## Reference(s):

- [Source homepage](https://github.com/tenequm/skills/tree/main/skills/deep-research-glim)
- [ClawHub skill page](https://clawhub.ai/tenequm/skills/deep-research-glim)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Structured Markdown research report with citations and source annotations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include source links, quotations, metrics, contradictions, strategic recommendations, and annotated sources.]

## Skill Version(s):

0.2.7 (source: frontmatter metadata and changelog, released 2026-08-07)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

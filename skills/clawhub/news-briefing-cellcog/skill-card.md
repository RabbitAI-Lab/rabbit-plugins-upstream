## Description:

News Briefing helps agents create CellCog-powered news briefings, competitive intelligence, market updates, trend reports, and current-events research from multi-source synthesis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cellcog](https://clawhub.ai/user/cellcog)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to ask an agent for daily briefings, market updates, competitive intelligence, trend monitoring, industry reports, and current-events research powered by CellCog.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Briefing prompts are sent to an external CellCog service using an API key.

Mitigation: Use this skill only with appropriate CellCog account and data-handling terms, and avoid including secrets or sensitive internal material in prompts.

Risk: News and competitive-intelligence summaries may be incomplete, outdated, or inaccurate for high-impact decisions.

Mitigation: Request source URLs and review important findings against cited sources before acting on them.

## Reference(s):

- [CellCog homepage](https://cellcog.ai)
- [ClawHub skill page](https://clawhub.ai/cellcog/skills/news-briefing-cellcog)
- [CellCog publisher profile](https://clawhub.ai/user/cellcog)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown, structured text, Python usage snippets, shell installation commands, and optional PDF or HTML reports produced by CellCog.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires python3 and CELLCOG_API_KEY; briefing prompts are sent to CellCog's external service.]

## Skill Version(s):

1.0.14 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

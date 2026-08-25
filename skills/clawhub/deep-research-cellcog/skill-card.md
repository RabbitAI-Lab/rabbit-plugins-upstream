## Description:

Deep Research uses CellCog to produce multi-source research for market analysis, competitive analysis, investment research, academic research, due diligence, financial analysis, crypto research, and news intelligence.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cellcog](https://clawhub.ai/user/cellcog)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to request CellCog deep research across competitive analysis, market research, investment analysis, academic research, and due diligence. It is suited for research reports, structured comparisons, summaries, and source-backed analysis when citations are explicitly requested.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Confidential, regulated, financial, or proprietary prompts may be sent to the external CellCog service.

Mitigation: Use the skill only with data your organization permits sending to CellCog; avoid sensitive data unless approved.

Risk: Generated HTML or PDF reports may need review before sharing or rendering in trusted environments.

Mitigation: Review generated reports before distribution and open them in an environment appropriate for generated external-service content.

Risk: Source traceability may be incomplete if citations are not requested.

Mitigation: Explicitly request citations and source URLs for factual claims when traceability is required.

## Reference(s):

- [CellCog homepage](https://cellcog.ai)
- [DeepResearch Bench Leaderboard](https://huggingface.co/spaces/muset-ai/DeepResearch-Bench-Leaderboard)
- [ClawHub Deep Research skill page](https://clawhub.ai/cellcog/skills/deep-research-cellcog)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown guidance with Python examples; research outputs may be plain text, Markdown, PDF, or interactive HTML when requested.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires python3, the cellcog dependency, CELLCOG_API_KEY, and use of the external CellCog service; citations must be explicitly requested.]

## Skill Version(s):

1.0.20 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

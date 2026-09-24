## Description:

Provides a structured deep-research workflow for multi-round search, source tiering, cross-validation, and synthesis into research reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, analysts, and agent users use this skill to plan open-source research, collect and rank sources, compare conflicting information, and produce concise markdown reports with summaries, citations, data artifacts, and research logs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requests broad host command execution and file or API access for research workflows.

Mitigation: Run it in a sandboxed workspace, review commands before execution, avoid exposing secrets or private databases unless necessary, and write outputs to a non-sensitive folder.

Risk: Research outputs may contain outdated, conflicting, or weakly supported claims from public sources.

Mitigation: Keep source tiering, cross-validation notes, conflict labels, and limitations in the final report, and manually review high-impact conclusions before use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/deep-research-engine)
- [Publisher profile](https://clawhub.ai/user/thcjp)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown reports, summaries, source lists, CSV or JSON datasets, charts, and research logs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are organized under topic-specific output folders when the skill's workflow is followed.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

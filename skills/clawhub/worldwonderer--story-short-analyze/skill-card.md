## Description:

Analyzes short-form Chinese web fiction by decomposing story core, structure, emotional arc, reversals, writing techniques, reader resonance, and reusable patterns into project files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT-0

## Use Case:

Writers, editors, and agent users use this skill to analyze legally held short web-fiction stories and produce reusable narrative analysis for downstream story writing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill saves analyzed stories and derived reports locally.

Mitigation: Run it in a controlled workspace, analyze only material the user has rights to use, and review or remove local output directories when they are no longer needed.

Risk: Market and reader-profile references can reflect writing assumptions rather than neutral social analysis.

Mitigation: Treat those references as genre and platform heuristics, and verify conclusions against the target audience, platform, and source text.

Risk: Narrative analysis may be incorrect or misleading if reused without review.

Mitigation: Review generated reports against the source story and the skill's evidence-chain checks before using them for downstream writing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/worldwonderer/skills/story-short-analyze)
- [OpenClaw metadata source](https://github.com/zenstory-ai/oh-story-claudecode)
- [Output contract](references/output-contract.md)
- [Output templates](references/output-templates.md)
- [Short-story decomposition methodology](references/material-decomposition.md)
- [Analysis report style guide](references/analysis-report-style.md)
- [Source story quality checklist](references/source-story-quality.md)
- [Short web fiction market reference](references/real-market-data.md)

## Skill Output:

**Output Type(s):** [text, markdown, json, files, guidance]

**Output Format:** [Markdown analysis reports plus JSON metadata and local source-text backup]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates 拆文报告.md, 情节节点.md, 写作手法.md, _meta.json, and an 原文/ backup directory under 拆文库/{book title}/.]

## Skill Version(s):

1.1.18 (source: server release metadata; artifact frontmatter reports 3.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

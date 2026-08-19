## Description:

Deep Research Engine guides agents through multi-step public-source research, source ranking, cross-checking, and structured report generation for market, competitor, literature, investment, and technical-selection analyses.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and research-focused agent users use this skill to plan public-source research, collect and rank sources, cross-validate findings, and produce structured reports with citations, limitations, and research logs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requests broad command execution and its stated whitelist or sandbox protections are not enforced by the artifact itself.

Mitigation: Run it in a sandboxed agent environment, require explicit approval for shell commands, and review any command before execution.

Risk: Generated research may include outdated, conflicting, or weakly sourced public information.

Mitigation: Require source citations, prefer primary sources, preserve uncertainty labels, and perform human review before business, legal, financial, or technical decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/deep-research-engine)
- [Packaged skill definition](artifact/SKILL.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown reports with source lists, optional CSV/JSON datasets, chart files, and research logs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May organize generated artifacts under output/{research-topic}/ including report.md, executive-summary.md, sources.md, data files, charts, and research-log.md.]

## Skill Version(s):

1.0.1 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

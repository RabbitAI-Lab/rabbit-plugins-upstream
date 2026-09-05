## Description:

Research an open-ended question with current multi-source web evidence and produce a cited brief with facts, uncertainty, and recommendations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dataify-server](https://clawhub.ai/user/dataify-server)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, analysts, developers, and decision makers use this skill to gather current public web evidence and produce concise cited briefs for industry, policy, technology, company, or market questions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A crafted resume state could cause the research workflow to read or overwrite local files during resume.

Mitigation: Resume only from state.json files created by your own trusted runs, and review generated reports before sharing them.

Risk: Live web research can include stale, blocked, low-quality, or contradictory source material.

Mitigation: Use the skill's quality gates, numbered citations, contradiction notes, and evidence gaps to verify material claims before decisions.

## Reference(s):

- [Dataify documentation](https://doc.dataify.com)
- [Dataify support](https://www.dataify.com/)
- [Research brief contract](references/report-template.md)
- [ClawHub listing](https://clawhub.ai/dataify-server/skills/dataify-live-research)
- [Publisher profile](https://clawhub.ai/user/dataify-server)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown research brief with supporting JSON evidence and local source files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs include research date, scope, evidence table, findings, contradictions, unknowns, prioritized recommendations, and numbered source references.]

## Skill Version(s):

1.1.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Tracks a single A-share restructuring across multiple announcements, organizing milestones and sourced changes over time while identifying missing information.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huhoo](https://clawhub.ai/user/huhoo)

### License/Terms of Use:

MIT-0

## Use Case:

Investors and analysts use this skill to organize public announcements for one A-share restructuring into a source-linked timeline and compare changes between filings. It does not provide ratings, price targets, trading advice, or approval predictions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan reports a mismatch between the stated no-network purpose and network requests, and flags that generated source retrieval dates may be fabricated (medium confidence).

Mitigation: Review network behavior before use, pin the installation to a reviewed version, and verify retrieval dates against the original announcements.

Risk: Scanner coverage is partial; two local references could not be resolved.

Mitigation: Resolve the references and complete a review before relying on scanner results.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/huhoo/skills/cue-cn-restructuring-tracker)
- [Cue MCP catalog](https://cuecue.cn/api/mcp-catalog)

## Skill Output:

**Output Type(s):** [Markdown, Guidance]

**Output Format:** [Structured seven-section Markdown tracker with announcement links, retrieval dates, and before-and-after changes; an outline with placeholders when source access is unavailable]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Designed for one transaction with multiple announcements; missing information is named explicitly.]

## Skill Version(s):

0.1.0 (source: frontmatter and CHANGELOG.md, released 2026-11-08)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Searches clinical-trial registries across sources and summarizes normalized trial records for planning and competitive landscape analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[medstatstar](https://clawhub.ai/user/medstatstar)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers and trial-planning teams use this skill to find and compare publicly registered clinical trials, check for similar studies, and assess sponsors, timelines, and competitor activity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms and a stable machine-derived identifier are sent to the author's third-party endpoints; Chinese WHO searches may also use online translation services.

Mitigation: Use public, non-sensitive search terms only; avoid external retrieval paths for confidential trial strategy, unreleased drugs, protocols, personal data, or sponsor-sensitive queries.

Risk: Broad or timed-out searches can return incomplete trial results.

Mitigation: Check for partial-result indicators and narrow or repeat searches before drawing conclusions.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/medstatstar/skills/ct-registry)
- [Project homepage](https://github.com/medstatstar/ct-registry)
- [Search procedure](references/search_procedure.md)
- [Retrieval and data-volume guide](docs/retrieval_guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Spreadsheet files]

**Output Format:** [Narrative summaries and structured trial records, with optional Excel export]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results may be partial when retrieval times out.]

## Skill Version(s):

0.13.3 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

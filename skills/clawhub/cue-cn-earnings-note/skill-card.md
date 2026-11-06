## Description:

Creates an eight-section, evidence-linked first-draft earnings review for a public company and reporting period, with ratings and target prices left for human review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huhoo](https://clawhub.ai/user/huhoo)

### License/Terms of Use:

MIT-0

## Use Case:

External users and investment researchers use the skill to prepare structured earnings-review drafts from public filings and optional user materials. A human reviewer supplies ratings, target prices, and final judgments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authenticated requests could expose the optional CUE_API_KEY to an unapproved destination.

Mitigation: Use the manual-material fallback until request destinations and redirect handling are validated; restrict authenticated requests to approved destinations.

Risk: The processing location and retention of documents accessed through Bridge are not established by the supplied release evidence.

Mitigation: Limit Bridge access to selected public documents and confirm where their contents are processed.

Risk: Passing the report checks does not establish source accuracy or financial correctness.

Mitigation: Have a human verify cited figures and source material, and supply all ratings and target-price judgments.

Risk: Optional installers and skills have not been reviewed as part of this release evidence.

Mitigation: Review and pin optional installers and skills separately before enabling them.

## Reference(s):

- [Data channels and Cue setup](references/data-channels.md)
- [Earnings report structure](references/report-skeleton.md)
- [Coverage ledger format](references/coverage-ledger.md)
- [Evidence format](references/evidence-format.md)
- [Cue MCP information](https://cuecue.cn/hub/mcp)
- [Cue Omni Reader information](https://cuecue.cn/hub/omni-reader)
- [Cue API key page](https://cuecue.cn/hub/api-key)

## Skill Output:

**Output Type(s):** [Markdown, JSON, JSONL, Text]

**Output Format:** [Structured earnings-review Markdown with JSON and JSONL evidence and tracking files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Eight-section first draft; figures include source confidence labels where available, and ratings and target prices remain for human completion.]

## Skill Version(s):

0.3.46 (source: SKILL.md frontmatter, server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

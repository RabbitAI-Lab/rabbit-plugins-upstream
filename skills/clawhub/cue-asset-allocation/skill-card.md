## Description:

Generates a monthly asset-allocation report using Cue to connect macroeconomic indicators and capital flows with suggested equity, bond, and commodity allocations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Investment advisers and portfolio teams use this skill to prepare monthly allocation reports, client proposals, and investment-committee briefing materials based on macroeconomic trends.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installation executes an unpinned external Cue runner, which may change between runs.

Mitigation: Review and trust the runner repository before installing or updating it.

Risk: Cue API credentials are used for remote requests, and reports may consume paid credits.

Mitigation: Have the user manage their own API key and confirm before paid report runs.

Risk: A shared report link may expose confidential client or business information.

Mitigation: Check report sensitivity and recipients before sharing the original Cue link.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/panting09266-ai/skills/cue-asset-allocation)
- [Cue platform](https://cuecue.cn)
- [Cue runner repository (referenced installation dependency)](https://github.com/sensedeal/cue-skills)

## Skill Output:

**Output Type(s):** [Markdown, Analysis, Guidance]

**Output Format:** [Markdown monthly report with allocation rationale, suggested proportions, risk notes, and source links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Provides a local report file and, when available, a link to the original Cue report; optional Word or PDF conversion.]

## Skill Version(s):

1.0.9 (source: ClawHub release; supplied SKILL.md frontmatter says 1.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

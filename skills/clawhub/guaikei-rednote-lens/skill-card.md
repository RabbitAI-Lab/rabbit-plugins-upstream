## Description:

Fetches public Xiaohongshu keyword search results, note details, comments, and creator posts as structured JSON for downstream analysis and reporting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External content creators, brand marketers, analysts, and operators use this skill to collect public Xiaohongshu content, comments, engagement metrics, and creator posts for topic research, competitor monitoring, KOL screening, trend analysis, and reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Xiaohongshu search terms, links, and GUAIKEI_API_TOKEN are sent to the guaikei.com API.

Mitigation: Use only with an approved token and an acceptable data-sharing posture for the third-party API.

Risk: Generated local logs may contain public comments, profile links, or sensitive market research.

Mitigation: Review, protect, or delete generated logs according to the sensitivity of the collected results.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/guaikei-rednote-lens)
- [Parameter and invocation reference](references/options.md)
- [Skill changelog](references/changelog.md)
- [Guaikei API service](https://www.guaikei.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [Structured JSON command output with optional concise text summary; successful runs also write JSON result logs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 16.14.0+ and GUAIKEI_API_TOKEN; documented result limits are 1-10000 items per request.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

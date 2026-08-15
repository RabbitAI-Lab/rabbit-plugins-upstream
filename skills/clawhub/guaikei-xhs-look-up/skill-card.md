## Description:

Fetches structured public Xiaohongshu note search results, note details, comments, and creator post lists through the Guaikei API for social content analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT

## Use Case:

Content creators, brand marketers, market researchers, and data analysts use this skill to collect public Xiaohongshu data for trend research, competitive monitoring, KOL screening, and comment analysis. It supports read-only lookup workflows and does not log in, publish content, or interact with Xiaohongshu accounts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Xiaohongshu keywords, URLs, request metadata, and the GUAIKEI_API_TOKEN are sent to guaikei.com.

Mitigation: Install only when this third-party API use is acceptable, avoid sensitive or regulated inputs, and manage the token as a credential.

Risk: Returned notes, comments, creator data, and run output can be retained locally in generated logs.

Mitigation: Review and delete local logs when no longer needed, especially in shared environments.

Risk: The skill is limited to public lookup data and can return empty or error results for invalid links, unavailable content, or API failures.

Mitigation: Validate keywords and URLs before execution, handle non-success statuses explicitly, and avoid treating empty results as factual analysis.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/guaikei-xhs-look-up)
- [Guaikei API service](https://www.guaikei.com)
- [Options reference](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, JSON, Guidance]

**Output Format:** [Structured JSON with status, request metadata, skill metadata, and result payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 16.14.0+ and GUAIKEI_API_TOKEN; successful runs may save local log files under logs/.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata; artifact metadata reports 1.1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

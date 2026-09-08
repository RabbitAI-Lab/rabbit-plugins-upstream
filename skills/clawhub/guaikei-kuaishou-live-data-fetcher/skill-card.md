## Description:

Fetches public Kuaishou/Kwai video search results, creator posts, and video comments for content research, trend analysis, keyword monitoring, and competitive analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT

## Use Case:

External users, content teams, marketers, and analysts use this skill to collect structured public Kuaishou data for topic research, competitor monitoring, creator work review, and comment analysis. The skill routes keyword, creator-profile, and video-comment requests to command-line scripts that return JSON for downstream analysis or reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Kuaishou research targets and the Guaikei API token are sent to www.guaikei.com.

Mitigation: Use the skill only after approving that data sharing, keep GUAIKEI_API_TOKEN in environment variables, avoid printing or sharing it, and rotate the token if exposed.

Risk: Scraped results are automatically written to a local logs directory and may contain sensitive research data.

Mitigation: Restrict access to generated logs and review or remove them before sharing the workspace.

Risk: The authoritative security scan marked the release suspicious because of token-handling guidance and automatic result logging.

Mitigation: Review the scan summary before deployment and confirm the token handling and log retention practices match the intended environment.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/engheng-art/skills/guaikei-kuaishou-live-data-fetcher)
- [Guaikei API Service](https://www.guaikei.com)
- [Complete Option Reference](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [text, json, shell commands, configuration, guidance]

**Output Format:** [Structured JSON with status, request metadata, skill metadata, and results, plus concise command guidance or error text.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires GUAIKEI_API_TOKEN and writes per-run JSON result logs under the skill's logs directory.]

## Skill Version(s):

1.0.0 (source: frontmatter, package.json, changelog, and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

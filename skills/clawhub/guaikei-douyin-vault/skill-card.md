## Description:

Guides an agent to map natural-language Douyin research requests to Node.js CLI commands that query public Douyin videos, creator posts, comments, and hot topics and return JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External users, marketers, analysts, and developers use this skill to search public Douyin content, retrieve creator posts or comments, inspect hot topics, and export structured data for competitive research, marketing reports, public sentiment monitoring, and trend tracking.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Douyin keywords, creator or video URLs, and the configured GUAIKEI_API_TOKEN are sent to guaikei.com.

Mitigation: Use the skill only when the user is comfortable sharing those values with guaikei.com, and keep the token in the GUAIKEI_API_TOKEN environment variable rather than embedding it in prompts or files.

Risk: Saved logs can contain comments, user identifiers, public profile data, and query history.

Mitigation: Treat logs as potentially sensitive, avoid committing or broadly sharing them, and delete or restrict access to logs that are no longer needed.

Risk: The skill collects public Douyin data that may still be subject to platform, privacy, or organizational use restrictions.

Mitigation: Use it only for public data the user is authorized to collect and analyze, and avoid redistributing collected data outside permitted personal or team use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/guaikei-douyin-vault)
- [Complete options reference](references/options.md)
- [Changelog](references/changelog.md)
- [Search request schema](assets/search_cli_req.schema.json)
- [Search response schema](assets/search_cli_resp.schema.json)
- [Guaikei token and help site](https://www.guaikei.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Analysis, Guidance, Configuration]

**Output Format:** [JSON from CLI stdout, with optional text or Markdown summaries from the agent.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires GUAIKEI_API_TOKEN; saves JSON logs under logs/; single runs are limited to 10000 records.]

## Skill Version(s):

1.0.0 (source: server release metadata, package.json, changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

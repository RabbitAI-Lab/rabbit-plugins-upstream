## Description:

Retrieves public TikTok search results, creator posts, and video comments to support audience research and product opportunity analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[why20261](https://clawhub.ai/user/why20261)

### License/Terms of Use:

MIT-0

## Use Case:

Product researchers, marketers, and creators use public TikTok posts and comments to investigate audience needs, monitor competitors, and identify content or product opportunities.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The API token and TikTok search terms or target URLs are sent to guaikei.com.

Mitigation: Use the skill only if sharing the token and requested targets with that service is acceptable.

Risk: Fetched public comments and profile identifiers are saved in local temporary logs.

Mitigation: Remove logs when no longer needed and anonymize identifiers before sharing results externally.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/why20261/skills/tiktok-user-insight)
- [Guaikei service and token information](https://www.guaikei.com)
- [Command options](references/options.md)
- [Release notes](references/changelog.md)

## Skill Output:

**Output Type(s):** [Structured data, Analysis guidance]

**Output Format:** [JSON results and text summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results include status, error codes, and warnings; runs also save local logs.]

## Skill Version(s):

1.0.0 (source: ClawHub release, SKILL.md frontmatter, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

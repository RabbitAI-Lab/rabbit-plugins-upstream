## Description:

This skill lets agents retrieve public TikTok keyword search results, creator post lists, and video comments as structured JSON for content research, competitor monitoring, influencer screening, and social listening.

This skill is ready for commercial/non-commercial use.

## Publisher:

[why20261](https://clawhub.ai/user/why20261)

### License/Terms of Use:

MIT

## Use Case:

External users and developers use this skill to retrieve public TikTok keyword, creator-post, and video-comment data for content research, market monitoring, influencer screening, and downstream AI analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends the GUAIKEI_API_TOKEN plus TikTok queries, profile URLs, video IDs, and result requests to www.guaikei.com.

Mitigation: Use only approved provider credentials, avoid sensitive research targets, and rotate or revoke the token if exposure is suspected.

Risk: Successful runs save JSON result logs in the system temp directory, which may include public comments and user identifiers.

Mitigation: Delete or protect local logs when handling sensitive research, and sanitize user identifiers before sharing results.

Risk: The returned data is public TikTok content but may still be subject to platform, privacy, or customer policy constraints.

Mitigation: Confirm permitted use before external or commercial publication, and anonymize personal identifiers where practical.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/why20261/skills/tiktok-skill)
- [GUAIKEI API provider](https://www.guaikei.com)
- [TikTok skill options reference](references/options.md)
- [TikTok skill changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Guidance]

**Output Format:** [Structured JSON envelopes from Node.js CLI commands, with operational logs on stderr.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires GUAIKEI_API_TOKEN; successful runs may save JSON result logs in the system temp directory.]

## Skill Version(s):

1.0.0 (source: frontmatter, package.json, changelog, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

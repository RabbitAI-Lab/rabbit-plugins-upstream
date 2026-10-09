## Description:

Retrieves public TikTok search results, creator posts, and video comments to support competitor and content analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[why20261](https://clawhub.ai/user/why20261)

### License/Terms of Use:

MIT-0

## Use Case:

Brands, creators, marketers, and agent developers use this skill to research public TikTok videos, compare creator posts, and examine comment trends.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The API token and requested TikTok search terms or URLs are sent to Guaikei.

Mitigation: Confirm the service is acceptable before use, and protect the GUAIKEI_API_TOKEN credential.

Risk: Saved results can retain usernames, stable identifiers, and public comments.

Mitigation: Delete unneeded temporary logs and share results only when there is a compliant basis to do so.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/why20261/skills/tiktok-insight)
- [Command options and output format](references/options.md)
- [Guaikei service and token setup](https://www.guaikei.com)

## Skill Output:

**Output Type(s):** [JSON data, Text, Guidance]

**Output Format:** [Structured JSON results and natural-language analysis]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results include status and warnings; fetched results are also saved as local JSON logs.]

## Skill Version(s):

1.0.0 (source: ClawHub release, skill frontmatter, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Search TikTok videos by keyword, retrieve creators’ public posts, and collect video comments for content and market research.

This skill is ready for commercial/non-commercial use.

## Publisher:

[why20261](https://clawhub.ai/user/why20261)

### License/Terms of Use:

MIT

## Use Case:

Creators, marketing teams, and researchers can use the skill to find public TikTok videos, review a creator’s posts, and analyze video comments for content and competitor research.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan had partial coverage and could not fully interpret 12 of 32 components, including several scripts.

Mitigation: Review the uninterpreted components before installation and account for the scan’s stated coverage limits.

Risk: The scanner notes a minor timezone-formatting concern that may affect how returned times are interpreted.

Mitigation: Confirm timestamp and timezone interpretation before using results for time-sensitive comparisons.

## Reference(s):

- [Usage options](artifact/references/options.md)
- [Changelog](artifact/references/changelog.md)
- [TikTok data service and token access](https://www.guaikei.com)
- [ClawHub skill listing](https://clawhub.ai/why20261/skills/tiktok-skill)

## Skill Output:

**Output Type(s):** [Structured data, JSON]

**Output Format:** [JSON output envelope containing TikTok search results, creator posts, or video comments]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes one JSON envelope to stdout; empty results are valid.]

## Skill Version(s):

1.1.2 (source: frontmatter, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

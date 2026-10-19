## Description:

Retrieves Xiaohongshu creator notes through SocialDataX for recent publishing reviews, content research, and creator analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, marketers, and researchers use this read-only skill to review Xiaohongshu account posts, compare creators, and analyze publishing patterns and engagement.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Running an unpinned npm CLI may execute a newly published package with access to the SocialDataX API key.

Mitigation: Trust the publisher and package before installation; in stricter environments, pin and review a package version or use a preconfigured MCP tool.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/devinchen2014/skills/socialdatax-xhs-creator-notes)
- [SocialDataX API access](https://socialdatax.com/ai?from=clawhub)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands]

**Output Format:** [Markdown summaries of creator notes; JSON from the CLI or MCP tools]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include note IDs, publish times, engagement counts, media links, and pagination tokens when available.]

## Skill Version(s):

0.1.17 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

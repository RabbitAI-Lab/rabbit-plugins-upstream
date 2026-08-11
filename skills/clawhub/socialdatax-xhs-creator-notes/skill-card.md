## Description:

Fetches Xiaohongshu (XHS/RedNote) creator note lists from SocialDataX for recent publishing review, account tracking, creator benchmarking, and content analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve Xiaohongshu creator post lists through SocialDataX, then summarize recent posts, interaction counts, media links, content types, and creator publishing patterns.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a SocialDataX API key in the runtime environment.

Mitigation: Use the official SocialDataX API-key URL from the skill, scope and store the key according to local credential-handling policy, and avoid committing it to skill files.

Risk: The npm package is executed at runtime to call SocialDataX.

Mitigation: Review the package source and installation policy before deployment, and run it only in environments approved for third-party npm packages.

Risk: Multi-page or --all fetches may consume API quota or credits.

Mitigation: Set page or item limits for exploratory use and confirm quota expectations before broad collection.

## Reference(s):

- [SocialDataX API access and homepage](https://socialdatax.com/ai?from=clawhub)
- [ClawHub skill page](https://clawhub.ai/devinchen2014/skills/socialdatax-xhs-creator-notes)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON result summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May call SocialDataX CLI or MCP tools and summarize returned JSON fields including note IDs, publish times, interaction counts, media links, content types, page counts, item counts, and pagination tokens.]

## Skill Version(s):

0.1.16 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

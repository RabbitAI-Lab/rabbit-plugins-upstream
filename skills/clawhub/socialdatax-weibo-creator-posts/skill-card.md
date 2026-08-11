## Description:

Retrieves Weibo creator post lists for recent publishing review, content research, creator benchmarking, account tracking, and content analysis through SocialDataX.

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

External analysts, developers, and agent users use this skill to retrieve and summarize public Weibo creator posts, recent publishing activity, interaction counts, media links, and author facts when available.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a SocialDataX API key from the user's runtime environment.

Mitigation: Keep SOCIALDATAX_API_KEY private and avoid placing it in prompts, logs, generated files, or shared shell history.

Risk: Unbounded pagination can consume more credits or time than intended.

Mitigation: Prefer bounded requests such as --max-items or --pages when exploring a creator's posts.

Risk: The direct CLI is installed and executed through npx.

Mitigation: Review npm package provenance before use, as with any npx-based tool.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/devinchen2014/skills/socialdatax-weibo-creator-posts)
- [SocialDataX API access](https://socialdatax.com/ai?from=clawhub)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown guidance with inline shell commands; SocialDataX CLI responses are JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only data retrieval using SOCIALDATAX_API_KEY; pagination can be bounded with --pages or --max-items.]

## Skill Version(s):

0.1.17 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

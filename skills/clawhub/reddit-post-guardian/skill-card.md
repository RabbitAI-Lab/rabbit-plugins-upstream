## Description:

Checks Reddit post drafts against subreddit rules, scores removal and AI-content risk, and suggests human-facing edits before posting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heroinyan-stack](https://clawhub.ai/user/heroinyan-stack)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, founders, and marketers use this skill to review Reddit drafts for subreddit-rule compliance, removal risk, AI-sounding language, and concrete edits before posting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can be used to create deceptive Reddit marketing rewrites or work around community moderation rules.

Mitigation: Use it to summarize rules and spot obvious compliance issues; do not use rewrite or post-plan guidance to fabricate anecdotes, fake claims, hide AI authorship, or evade subreddit promotion rules.

Risk: The artifact relies on subreddit rule interpretation and predictive removal-risk scoring that may be incomplete or wrong.

Mitigation: Verify subreddit rules directly, ask users to provide current sidebar or wiki rules when rule data is missing, and seek moderator approval where promotion is restricted.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/heroinyan-stack/skills/reddit-post-guardian)
- [Publisher profile](https://clawhub.ai/user/heroinyan-stack)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown report with scored checks, risk guidance, and suggested rewrite text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include compliance tables, removal-risk scores, AI-content likelihood estimates, rewrite suggestions, and posting-plan guidance.]

## Skill Version(s):

1.0.0 (source: server release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

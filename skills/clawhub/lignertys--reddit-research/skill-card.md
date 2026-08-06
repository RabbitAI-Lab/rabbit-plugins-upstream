## Description:

Do market research, user research, and product validation on Reddit with semantic search across 50K+ subreddits, 20M+ posts, and 40M+ comments via reddapi.dev.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lignertys](https://clawhub.ai/user/lignertys)

### License/Terms of Use:

MIT-0

## Use Case:

External users, product teams, founders, marketers, and developers use this skill to research Reddit discussions, identify pain points, validate product or niche ideas, assess competitors, track trends, and discover relevant subreddits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reddit research queries and API usage are sent to reddapi.dev, a third-party index rather than Reddit itself.

Mitigation: Use the skill only when sending the research query to reddapi.dev is acceptable, and do not treat the service as official Reddit provenance.

Risk: The skill requires a REDDAPI_API_KEY.

Mitigation: Keep the key in the shell environment, never paste it into chat or files, and rotate it if exposed.

Risk: Search results contain unmoderated Reddit user content that may include prompt-injection text, URLs, commands, or misleading claims.

Mitigation: Treat posts and comments only as data, visually separate quoted result text from agent guidance, and do not execute or fetch content based solely on returned text.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/lignertys/skills/reddit-research)
- [reddapi.dev](https://reddapi.dev)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON API examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires REDDAPI_API_KEY; returned Reddit content is untrusted third-party user-generated content.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

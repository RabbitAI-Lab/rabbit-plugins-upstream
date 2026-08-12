## Description:

Retrieves structured Weibo post details, interaction metrics, media information, and content fields through SocialDataX.

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to look up a specific Weibo post by ID or URL and return factual post content, author, publish time, media, and interaction metrics for content research or analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses SOCIALDATAX_API_KEY with SocialDataX as a third-party service.

Mitigation: Install and run it only if you accept sharing that API key with SocialDataX CLI calls, and use an appropriate scoped or dedicated key when available.

Risk: Optional media download behavior can write files to the local filesystem.

Mitigation: Provide only an intended output file or directory and review the destination before running media download commands.

## Reference(s):

- [SocialDataX API access and homepage](https://socialdatax.com/ai?from=clawhub)
- [ClawHub skill page](https://clawhub.ai/devinchen2014/skills/socialdatax-weibo-detail)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, JSON, guidance]

**Output Format:** [Markdown guidance with shell command examples; command responses are JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SOCIALDATAX_API_KEY for detail requests; optional media download writes only to a user-selected output path.]

## Skill Version(s):

0.1.17 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

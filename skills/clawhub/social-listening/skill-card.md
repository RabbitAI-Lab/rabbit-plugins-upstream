## Description:

Finds relevant public LinkedIn conversations each week and sends a Slack digest of posts worth joining and commenters who match the buyer profile.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Marketing and sales-development teams use this skill to identify public LinkedIn posts relevant to their buyer profile and review a weekly Slack digest before deciding whether to join the conversation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The digest names public commenters and could be shared beyond the intended team.

Mitigation: Confirm the Slack channel is internal and appropriate for named commenters before deployment.

Risk: LinkedIn searches and comment reads may incur usage costs.

Mitigation: Verify the search limit and live pricing, and review the Cargo CDK plan before deployment.

Risk: Incorrect keywords, channel ID, or connector bindings could produce irrelevant results or send the digest to the wrong destination.

Mitigation: Check the configured keywords, channelId, and connector bindings before deploying.

## Reference(s):

- [ClawHub social-listening release](https://clawhub.ai/cargo-ai/skills/social-listening)
- [Publisher-provided project homepage (not verified provenance)](https://github.com/getcargohq/gtm-skills)
- [Digest format reference](references/digest.md)

## Skill Output:

**Output Type(s):** [Guidance, Code, Configuration instructions, Markdown]

**Output Format:** [Markdown guidance and code/configuration for a weekly Slack digest]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Digest highlights at most five posts and ten relevant commenters; no automated LinkedIn engagement.]

## Skill Version(s):

0.1.1 (source: frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

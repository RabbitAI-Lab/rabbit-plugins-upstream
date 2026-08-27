## Description:

First-run flow for PostKing: authenticate, top up credits, onboard a brand from a URL, connect socials, and ship a first post.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bitsandtea](https://clawhub.ai/user/bitsandtea)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to complete the first PostKing setup flow: authenticate, fund credits, onboard a brand, connect social accounts, and schedule an initial post.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide an agent through paid credit purchases or subscriptions.

Mitigation: Review each billing option and approve only the pack or subscription you intend to purchase.

Risk: The skill can guide OAuth connection of social accounts.

Mitigation: Confirm the target platform and account before opening an OAuth link, and verify the connected account afterward.

Risk: The skill can guide scheduling a public social post.

Mitigation: Review generated post variations, selected platform, and schedule before approving the post.

## Reference(s):

- [PostKing ClawHub skill page](https://clawhub.ai/bitsandtea/skills/postking)
- [PostKing MCP endpoint](https://mcp.postking.app/mcp)
- [PostKing skill icon](https://raw.githubusercontent.com/bitsandtea/postking-skills/main/assets/icons/postking-getting-started.svg)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline tool names and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Stage-by-stage flow that asks for user confirmation before billing, OAuth, onboarding, and posting actions.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

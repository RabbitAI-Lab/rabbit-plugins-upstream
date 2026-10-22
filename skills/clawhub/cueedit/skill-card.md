## Description:

Connects agents to Instagram and Facebook Pages to review comments, draft and send replies or private messages, and manage keyword-triggered Auto DM rules.

This skill is ready for commercial/non-commercial use.

## Publisher:

[theindianappguy](https://clawhub.ai/user/theindianappguy)

### License/Terms of Use:

MIT

## Use Case:

External users and social-media managers use CueEdit to review unanswered Instagram and Facebook Page comments, prepare replies or private messages for approval, and manage Instagram keyword-triggered Auto DM rules.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Connected-account data and message logs are processed by CueEdit, and credentials could expose account access.

Mitigation: Connect only accounts you intend to manage and keep the API key private.

Risk: Replies, DMs, and Auto DM rules can affect real users; an active rule continues handling new comments.

Mitigation: Review recipients and exact message text before approving writes, and pause rules when they are no longer wanted.

Risk: Changing the API endpoint can redirect account requests away from the expected CueEdit service.

Mitigation: Leave CUEEDIT_API_URL at its default.

Risk: Reel scheduling and cancellation are not supported for publishing as described by the release guidance.

Mitigation: Avoid scheduling and cancellation tools; publish reels directly in Instagram.

## Reference(s):

- [CueEdit API and MCP reference](references/api.md)
- [CueEdit workflow examples](references/examples.md)
- [CueEdit website](https://www.cueedit.io/?ref=skill)

## Skill Output:

**Output Type(s):** [Text, Guidance, Shell commands]

**Output Format:** [Natural-language guidance, message drafts, and JSON API results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes require explicit user approval; active Auto DM rules continue until paused.]

## Skill Version(s):

1.0.0 (source: frontmatter, server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

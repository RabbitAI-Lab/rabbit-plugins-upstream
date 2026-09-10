## Description:

Post text content to LinkedIn using the official API. Triggers on "post to LinkedIn", "share on LinkedIn", or /linkedin-direct.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sivraj](https://clawhub.ai/user/sivraj)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to configure LinkedIn API credentials and publish text-only LinkedIn posts from an agent workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can publish public LinkedIn posts for the configured account.

Mitigation: Review the post text and visibility before use, and install only for accounts where agent-assisted publishing is intended.

Risk: The LinkedIn access token grants account posting access if exposed.

Mitigation: Store the token only in the configured environment, treat it like a password, and rotate or remove it when posting access is no longer needed.

Risk: LinkedIn app approval, token scopes, or token expiry can block posting.

Mitigation: Confirm the Share on LinkedIn product approval, use the required scopes, and renew expired tokens through LinkedIn's token generator.

## Reference(s):

- [LinkedIn Developers Apps](https://www.linkedin.com/developers/apps)
- [LinkedIn Userinfo API](https://api.linkedin.com/v2/userinfo)
- [LinkedIn UGC Posts API](https://api.linkedin.com/v2/ugcPosts)
- [ClawHub skill page](https://clawhub.ai/sivraj/skills/linkedin-poster)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash code blocks and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces text-only LinkedIn posting instructions and curl commands; posts are public unless changed by the user.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

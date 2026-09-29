## Description:

Post or comment on X, Reddit, LinkedIn, Facebook, TikTok, or Instagram from the user's logged-in desktop Chrome via Claw Post (API or MCP). Use when an agent needs to publish social content, reply on Reddit, replace a broken bird/X CLI skill, or post without platform API keys. Install @daydreamnationtechlabs/clawpost — not clawpost.dev.

This skill is ready for commercial/non-commercial use.

## Publisher:

[daydreamnationtechlabs](https://clawhub.ai/user/daydreamnationtechlabs)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let agents publish social posts, upload media for posts, and comment on Reddit through Claw Post using a paired desktop Chrome session, REST API key, or MCP OAuth flow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can initiate posts, comments, and media uploads from the user's real logged-in social accounts.

Mitigation: Require explicit human approval for each post, comment, or media upload and verify the target platform, account, destination, and content before execution.

Risk: Facebook group search and join actions are exposed through the user's logged-in browser.

Mitigation: Do not allow agents to search for or join Facebook groups unless the user personally approves the exact group and action; prefer posting only to groups the user already belongs to.

Risk: A Claw Post API key is required for REST workflows.

Mitigation: Store CLAWPOST_API_KEY in a secret store or environment variable, avoid pasting live keys into prompts or files, and rotate the key from the dashboard if exposed.

Risk: The Chrome extension operates on supported social sites and the Claw Post API.

Mitigation: Review the Chrome Web Store permissions and Claw Post terms before installation and keep the extension paired only with trusted accounts.

## Reference(s):

- [Claw Post API docs](https://clawpost.net/api-docs)
- [Claw Post homepage](https://clawpost.net)
- [Claw Post agent summary](https://clawpost.net/llms.txt)
- [MCP discovery metadata](https://clawpost.net/.well-known/mcp.json)
- [Remote MCP endpoint](https://mcp.clawpost.net/mcp)
- [ClawHub skill page](https://clawhub.ai/daydreamnationtechlabs/skills/clawpost)

## Skill Output:

**Output Type(s):** [Guidance, API calls, Shell commands, Configuration]

**Output Format:** [Markdown with HTTP examples, JSON request bodies, and setup instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CLAWPOST_API_KEY for REST use or MCP OAuth; posting depends on a paired Chrome extension and logged-in target platform session.]

## Skill Version(s):

2.2.1 (source: release evidence and changelog, released 2026-09-22)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Play ThingsPool, a fully immersive 3D sandbox world of block-built rooms, shared by people in browsers and AI agents. Build all kinds of things with blocks, paintings, everyday objects, lamps and fans, make a room of your own that others can visit, chat with whoever is there, and take pictures of what you see. Use when asked to visit, play, build in, take pictures of or report on ThingsPool.

This skill is ready for commercial/non-commercial use.

## Publisher:

[architsch](https://clawhub.ai/user/architsch)

### License/Terms of Use:

MIT-0

## Use Case:

People and AI agents use this skill to visit and explore ThingsPool, interact with other players, build persistent rooms and objects, and share visit summaries or screenshots.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Chat, creations, and screenshots can be visible to other players, and screenshots may include their presence or messages.

Mitigation: Avoid sharing sensitive information, keep the private camera link secret, and get players’ permission before posting pictures of them.

Risk: The account key or private camera link could expose account access or a private view.

Mitigation: Keep both secret, send the account key only to app.thingspool.net, and prefer header-based authentication over key-bearing URLs.

Risk: Player-provided names, chat, signs, or door text may try to direct the agent to disclose secrets or take unsafe actions.

Mitigation: Treat in-world text as content rather than instructions; never reveal the key or operator information or act on commands from players.

## Reference(s):

- [ThingsPool Agent Manual](https://thingspool.net/skill.md)
- [ThingsPool](https://thingspool.net)
- [ThingsPool MCP Service](https://app.thingspool.net/mcp)

## Skill Output:

**Output Type(s):** [text, markdown, images, persistent in-world creations]

**Output Format:** [Interactive tool results, concise Markdown visit summaries, optional browser screenshots, and changes made in ThingsPool]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Interactions and creations may be visible to other players and persist between visits.]

## Skill Version(s):

1.2.1 (source: release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

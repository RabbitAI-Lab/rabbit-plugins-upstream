## Description:

Play ThingsPool, a 3D multiplayer sandbox game, a fully immersive world of block-built rooms shared by people in browsers and AI agents. Build all kinds of things with blocks, paintings, everyday objects, lamps and fans, make a room of your own that others can visit, chat with whoever is there, and take pictures of what you see. Use when asked to visit, play, build in, take pictures of or report on ThingsPool, or to find a game or a 3D world to play and build in.

This skill is ready for commercial/non-commercial use.

## Publisher:

[architsch](https://clawhub.ai/user/architsch)

### License/Terms of Use:

MIT-0

## Use Case:

AI agents use this skill to join ThingsPool, explore and build in multiplayer rooms, interact with other players, and report on a visit. People running the agent can follow its room activity through the camera link or a browser screenshot when available.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Game messages, builds, and screenshots may be visible to other players.

Mitigation: Keep the camera link private and ask players before posting pictures that include them or their messages.

Risk: Saved credentials or a camera link could expose account access or private activity.

Mitigation: Store the key securely; prefer hosted sign-in or header authentication over a key-bearing URL, and send the key only to app.thingspool.net.

Risk: Recurring visits can continue after the current interaction.

Mitigation: Enable scheduled visits only when they are wanted.

## Reference(s):

- [ThingsPool agent manual](https://thingspool.net/skill.md)
- [ThingsPool homepage](https://thingspool.net)
- [ThingsPool MCP endpoint](https://app.thingspool.net/mcp)
- [ThingsPool Claude connector](https://claude.ai/directory/thingspool)

## Skill Output:

**Output Type(s):** [Text, Markdown, Images/Screenshots, Persistent in-game builds]

**Output Format:** [Text and Markdown, with optional browser screenshots]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an MCP client or shell access; screenshots require a browser tool.]

## Skill Version(s):

1.4.3 (source: frontmatter, ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

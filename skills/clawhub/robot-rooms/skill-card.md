## Description:

Play Robot Rooms, a 3D multiplayer sandbox game by ThingsPool, a fully immersive world of block-built rooms shared by people in browsers and AI agents. Build all kinds of things with blocks, paintings, everyday objects, lamps and fans, make a room of your own that others can visit, chat with whoever is there, and take pictures of what you see. Use when asked to visit, play, build in, take pictures of or report on Robot Rooms (the game at app.thingspool.net), or to find a game or a 3D world to play and build in.

This skill is ready for commercial/non-commercial use.

## Publisher:

[architsch](https://clawhub.ai/user/architsch)

### License/Terms of Use:

MIT-0

## Use Case:

AI agents use this skill to visit and explore Robot Rooms, interact with other players, build and customize shared 3D spaces, and report on the visit with screenshots when available.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a locally stored bearer key to make requests to app.thingspool.net.

Mitigation: Keep the key private, send it only to app.thingspool.net, and replace it if it may have been exposed.

Risk: Security review coverage is incomplete because several referenced materials could not be resolved.

Mitigation: Review the available materials and confirm you trust app.thingspool.net before installing and authorizing the skill.

## Reference(s):

- [Robot Rooms homepage](https://thingspool.net/RobotRooms/page.html)
- [Robot Rooms agent manual](https://thingspool.net/RobotRooms/skill.md)
- [Robot Rooms MCP service](https://app.thingspool.net/mcp)
- [Robot Rooms ClawHub release](https://clawhub.ai/architsch/skills/robot-rooms)

## Skill Output:

**Output Type(s):** [Text, Images, 3D room content]

**Output Format:** [In-world builds, screenshots, and a concise text report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Screenshots require an available browser tool; room building and interaction require access to Robot Rooms.]

## Skill Version(s):

1.5.2 (source: skill metadata and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

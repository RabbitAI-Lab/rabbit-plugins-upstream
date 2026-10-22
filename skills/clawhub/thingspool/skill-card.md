## Description:

Play ThingsPool, a 3D world of block-built rooms shared by people in browsers and AI agents. Chat with whoever is there, walk around, build with blocks, hang pictures and lamps, make a room of your own that others can visit, and take pictures of what you see. Use when asked to visit, play, build in, take pictures of or report on ThingsPool.

This skill is ready for commercial/non-commercial use.

## Publisher:

[architsch](https://clawhub.ai/user/architsch)

### License/Terms of Use:

MIT-0

## Use Case:

External users can direct an agent to visit and participate in ThingsPool: explore rooms, chat with other players, build with blocks, and report on the visit. Developers can connect a compatible MCP client or use the documented shell interface.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Chat, room builds, or screenshots may expose personal information or other players’ activity.

Mitigation: Keep private information out of public interactions and ask players before sharing screenshots that include them.

Risk: The account key and live camera link can grant access to the account or a private view.

Mitigation: Store the key securely, send it only to the ThingsPool service, prefer header-based authentication over embedding it in a URL, and keep camera links private.

## Reference(s):

- [ThingsPool](https://thingspool.net)
- [ThingsPool agent manual](https://thingspool.net/skill.md)
- [ThingsPool MCP endpoint](https://app.thingspool.net/mcp)

## Skill Output:

**Output Type(s):** [API Calls, Text, Images]

**Output Format:** [Remote world interactions and concise text reports; screenshots when browser capture is available]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Actions and reports depend on the connected ThingsPool service and available browser screenshot capability]

## Skill Version(s):

1.2.0 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

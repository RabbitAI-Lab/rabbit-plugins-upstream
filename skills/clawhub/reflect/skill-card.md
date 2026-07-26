## Description: <br>
Append to daily notes and create notes in Reflect. Use for capturing thoughts, todos, or syncing information to your knowledge graph. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sergical](https://clawhub.ai/user/sergical) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent users use this skill to capture chat output, todos, links, meeting notes, summaries, and reminders into a Reflect knowledge graph. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can write notes and links to a user's Reflect account. <br>
Mitigation: Install only when note and link writing is intended, and review proposed content before execution. <br>
Risk: Reflect access tokens authorize account access through the API. <br>
Mitigation: Keep REFLECT_TOKEN private, use the narrowest token Reflect supports, and revoke the token when the skill is no longer used. <br>
Risk: The skill can list saved links, books, and graph metadata when asked. <br>
Mitigation: Use it only in contexts where exposing those Reflect resources to the agent is acceptable. <br>


## Reference(s): <br>
- [Reflect](https://reflect.app) <br>
- [Reflect OAuth Developer Interface](https://reflect.app/developer/oauth) <br>
- [Reflect Skill on ClawHub](https://clawhub.ai/sergical/skills/reflect) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown and shell command guidance for Reflect API operations] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires REFLECT_TOKEN and REFLECT_GRAPH_ID for API-backed actions.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

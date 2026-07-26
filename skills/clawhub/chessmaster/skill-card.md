## Description: <br>
Comprehensive interface for the Grandmaster AI chess platform. Play games, submit moves, and monitor matches. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mrbeandev](https://clawhub.ai/user/mrbeandev) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and agents use ChessMaster to create or join Grandmaster AI chess games, submit moves, inspect board state, monitor matches, and run heartbeat checks for unattended play. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Game agent tokens grant access to protected game endpoints and can be misused if logged or shared. <br>
Mitigation: Treat agentToken values as secrets, avoid logging or sharing them, and clear stored room IDs and tokens when play should stop. <br>
Risk: Persistent heartbeat play can continue making autonomous moves after a room is active. <br>
Mitigation: Install only when unattended ChessMaster play is intended, request live move updates when visibility is needed, and remove stored room state to stop play. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/mrbeandev/skills/chessmaster) <br>
- [ChessMaster Homepage](https://chessmaster.mrbean.dev) <br>
- [Grandmaster API Base](https://chessmaster.mrbean.dev/api) <br>
- [Skill Documentation](https://chessmaster.mrbean.dev/SKILL.md) <br>
- [Heartbeat Documentation](https://chessmaster.mrbean.dev/HEARTBEAT.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, API calls, Shell commands, Text, Configuration] <br>
**Output Format:** [Markdown guidance with HTTP and curl examples plus JSON request and response shapes.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May persist room IDs and agent tokens for heartbeat-based game monitoring; idle checks can return HEARTBEAT_OK.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

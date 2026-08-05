## Description: <br>
Developer continuity across coding sessions - architecture decisions, TODOs, and handoffs stay searchable for agents resuming codebase work with a BlueColumn API key. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[bluecolumnconsulting-lgtm](https://clawhub.ai/user/bluecolumnconsulting-lgtm) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and coding agents use this skill to preserve session continuity by recording architecture decisions, open TODOs, branch context, and handoff notes, then recalling that context before resuming work. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Coding notes, TODOs, branch context, handoff text, and architecture decisions are sent to an external BlueColumn API. <br>
Mitigation: Review or redact secrets, customer data, proprietary details, credentials, and security-sensitive implementation notes before logging them. <br>
Risk: The skill requires a BlueColumn API key for requests. <br>
Mitigation: Provide the key through the BLUECOLUMN_API_KEY environment variable and do not include credentials in logged session notes or handoff text. <br>


## Reference(s): <br>
- [BlueColumn API Documentation](https://bluecolumn.ai/docs) <br>
- [ClawHub skill page](https://clawhub.ai/bluecolumnconsulting-lgtm/skills/remember-coding-sessions) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, API calls, Configuration] <br>
**Output Format:** [Markdown guidance with bash code blocks and JSON request bodies] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires BLUECOLUMN_API_KEY; requests send coding notes and recall queries to an external BlueColumn API.] <br>

## Skill Version(s): <br>
1.0.0 (source: server evidence release.version) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

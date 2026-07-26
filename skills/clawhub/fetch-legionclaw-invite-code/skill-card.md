## Description: <br>
Fetches Tongfudun LegionClaw usage-permission invite codes by deriving an agentid from a LegionClaw session handle and POSTing it as userId. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[legionspace-hackathon](https://clawhub.ai/user/legionspace-hackathon) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Agents running inside LegionClaw use this skill to retrieve one or more Tongfudun LegionClaw access invite codes for the current task-bound agent identity. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill obtains a session-derived agent identifier and sends it to an external invite-code endpoint. <br>
Mitigation: Install only in expected LegionClaw environments and prefer an explicit, scoped platform capability that returns only the needed agentid. <br>
Risk: Invite codes may grant access and could be exposed if written to files or logs. <br>
Mitigation: Return codes inline only to the requesting user by default, avoid logging session handles or agent identifiers, and create files only when the user explicitly requests file delivery. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/legionspace-hackathon/skills/fetch-legionclaw-invite-code) <br>
- [Tongfudun LegionClaw invite-code endpoint](https://legion.tongfudun.com/userInvite/claimIndustryInviteCode) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, API calls, guidance] <br>
**Output Format:** [Markdown text with optional inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Returns invite codes inline in chat by default; files are only produced when explicitly requested by the user.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

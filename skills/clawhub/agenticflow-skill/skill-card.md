## Description: <br>
AgenticFlow automates LinkedIn posting, private messaging, invitation management, and engagement analytics. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cgreselin-create](https://clawhub.ai/user/cgreselin-create) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users or developers use this skill to coordinate LinkedIn publishing, message handling, connection workflows, engagement reporting, and daily activity summaries through an agent. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can allow an agent to act on private messages, posts, invitations, and possibly browser sessions without enough opt-in or scope controls. <br>
Mitigation: Require separate opt-in for private-message automation, previews or approval before replies are sent, and clear limits on invitation handling and posting. <br>
Risk: LinkedIn automation can exceed platform limits or use broader account access than necessary. <br>
Mitigation: Prefer official LinkedIn API access with least-privilege OAuth scopes, enforce rate limits, and handle OAuth refresh errors explicitly. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, API calls, Guidance] <br>
**Output Format:** [Markdown or text responses with LinkedIn post, message, scheduling, analytics, and summary content.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May initiate LinkedIn API or browser-automation actions when the required account access and permissions are configured.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

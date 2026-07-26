## Description: <br>
Meetlark creates scheduling polls for humans and agents, shares participation links, collects votes, and finds the best meeting time. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mkelk](https://clawhub.ai/user/mkelk) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and their agents use Meetlark to coordinate meetings by creating scheduling polls, sharing participation links, collecting votes, checking results, and closing polls once a meeting time is selected. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Meetlark uses an external scheduling service that may handle meeting details and participant availability. <br>
Mitigation: Use the skill only when the user is comfortable using Meetlark as an external scheduling service. <br>
Risk: Admin tokens and individual vote results can expose sensitive poll management access or participant availability. <br>
Mitigation: Treat admin tokens and individual vote results as sensitive, share only the participation URL with invitees, and clear stored admin tokens after the poll is closed or no longer needed. <br>


## Reference(s): <br>
- [Meetlark OpenAPI spec](https://meetlark.ai/api/v1/openapi.json) <br>
- [Meetlark interactive docs](https://meetlark.ai/docs) <br>
- [Meetlark AI plugin manifest](https://meetlark.ai/.well-known/ai-plugin.json) <br>
- [Meetlark website](https://meetlark.ai) <br>
- [ClawHub skill page](https://clawhub.ai/mkelk/skills/meetlark) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, API Calls, Text, Markdown] <br>
**Output Format:** [Markdown with API request examples and user-facing scheduling text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include admin tokens, participation URLs, poll status, vote results, and suggested invitation text.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

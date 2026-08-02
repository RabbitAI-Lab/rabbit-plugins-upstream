## Description: <br>
Query Canvas LMS (Instructure) from a shell with curl and a bearer access token for courses, grades, assignments, submissions, calendar, planner, announcements, conversations, discussions, and files for yourself or a linked observee without running the canvas-parent-mcp server. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chrischall](https://clawhub.ai/user/chrischall) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, students, parents, or administrators use this skill to query Canvas LMS data directly with curl when they need scriptable access without running the MCP server. It helps retrieve profile, course, grade, assignment, submission, calendar, planner, announcement, conversation, discussion, and file data for an authenticated user or linked observee. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Bearer tokens and OAuth refresh credentials can expose Canvas data reachable by the account. <br>
Mitigation: Use a personal access token or trusted secrets manager where possible, avoid shared terminals and logs, and revoke or rotate credentials according to the institution's policy. <br>
Risk: The QR-login helper is invoked through npx and eval in the documented setup flow. <br>
Mitigation: Review the helper before using the QR-login flow and avoid pasting long-lived client secrets or refresh tokens into shared scripts. <br>
Risk: Downloaded Canvas files can overwrite local paths if commands are adapted into scripts without checks. <br>
Mitigation: Add explicit destination-file and parent-directory checks before scripted downloads. <br>


## Reference(s): <br>
- [Canvas API endpoints for curl](references/canvas-endpoints.md) <br>
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/canvas-parent-api) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and Canvas REST API examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands require a Canvas base URL and bearer token; API responses are typically JSON processed with jq.] <br>

## Skill Version(s): <br>
1.2.2 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

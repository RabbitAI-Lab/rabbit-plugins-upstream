## Description: <br>
Query Canvas LMS from a shell with curl and a bearer access token for courses, grades, assignments, submissions, calendar, planner, announcements, conversations, discussions, and files for yourself or a linked observee. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chrischall](https://clawhub.ai/user/chrischall) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, administrators, students, and observers use this skill to query Canvas LMS data directly with curl when they want scriptable API access without running the Canvas MCP server. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The OAuth QR setup example uses eval around output from an external npx helper, which could execute unexpected shell code. <br>
Mitigation: Prefer a personal Canvas access token where available, or inspect the helper output and export only CANVAS_BASE_URL, CANVAS_CLIENT_ID, CANVAS_CLIENT_SECRET, and CANVAS_REFRESH_TOKEN. <br>


## Reference(s): <br>
- [Canvas API endpoints for curl](references/canvas-endpoints.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with curl, shell, and jq examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a Canvas base URL and bearer or OAuth token; many calls return JSON and some list endpoints require pagination.] <br>

## Skill Version(s): <br>
1.2.4 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

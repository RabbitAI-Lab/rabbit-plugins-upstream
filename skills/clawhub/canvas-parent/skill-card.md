## Description: <br>
This skill helps agents access Canvas LMS information for a user or observed student, including courses, grades, assignments, announcements, planner items, conversations, and files. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chrischall](https://clawhub.ai/user/chrischall) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, parents, observers, students, and developers use this skill to let an agent read Canvas LMS account data, linked student records, course work, grades, calendars, inbox conversations, announcements, and course files. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can access sensitive Canvas account data and linked student records using session credentials, tokens, OAuth credentials, or username and password authentication. <br>
Mitigation: Install only when the user intends to grant Canvas access, prefer scoped token or OAuth authentication where available, and configure fetchproxy only deliberately. <br>
Risk: The file download tool can expose Canvas credentials to an arbitrary URL if misused. <br>
Mitigation: Confirm every download path and avoid allowing arbitrary URLs to be passed to canvas_download_file unless the package validates downloads against the configured Canvas host. <br>


## Reference(s): <br>
- [Canvas Parent skill on ClawHub](https://clawhub.ai/chrischall/skills/canvas-parent) <br>
- [canvas-parent-mcp npm package](https://www.npmjs.com/package/canvas-parent-mcp) <br>
- [fetchproxy extension](https://github.com/chrischall/fetchproxy) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, configuration, shell commands] <br>
**Output Format:** [Markdown with JSON and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Provides MCP setup and authentication guidance for Canvas read and download tools.] <br>

## Skill Version(s): <br>
1.2.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

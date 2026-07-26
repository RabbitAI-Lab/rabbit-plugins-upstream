## Description: <br>
This skill helps an agent use a Canvas LMS MCP server to read Canvas courses, grades, assignments, announcements, planner items, conversations, linked observees, and course files. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chrischall](https://clawhub.ai/user/chrischall) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to connect an agent to Canvas LMS data for their own account or linked observer students. It supports reviewing coursework, grades, messages, announcements, calendar items, planner tasks, and downloadable course files through the Canvas MCP server. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The MCP can access Canvas records, messages, files, and linked student data. <br>
Mitigation: Install only when the package and publisher are trusted, and grant access only for Canvas accounts and observees that the user is authorized to review. <br>
Risk: Session cookies, username/password credentials, OAuth secrets, or access tokens may expose sensitive Canvas access if mishandled. <br>
Mitigation: Prefer the least-sensitive authentication option supported by the institution, avoid username/password or session-cookie modes unless necessary, and store credentials outside shared project files. <br>
Risk: Downloaded course files may contain sensitive educational records or personal data. <br>
Mitigation: Confirm destination paths before downloads and keep saved files in appropriate local storage with access controls. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/canvas-parent-mcp) <br>
- [npm package: canvas-parent-mcp](https://www.npmjs.com/package/canvas-parent-mcp) <br>
- [Source repository: canvas-parent-mcp](https://github.com/chrischall/canvas-parent-mcp) <br>
- [fetchproxy extension](https://github.com/chrischall/fetchproxy) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Configuration, Shell commands] <br>
**Output Format:** [Markdown with JSON and shell command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May guide configuration of an MCP server that accesses Canvas records and can download course files.] <br>

## Skill Version(s): <br>
1.1.8 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

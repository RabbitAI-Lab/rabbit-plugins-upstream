## Description: <br>
Provides agent assistance for Canvas LMS accounts, including courses, grades, assignments, announcements, planner items, conversations, and course file downloads. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chrischall](https://clawhub.ai/user/chrischall) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to connect an agent to Canvas LMS for their own account or observed students, then retrieve school information and download course files through the Canvas helper. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can access sensitive Canvas session data, including browser session cookies when fetchproxy is enabled. <br>
Mitigation: Use it only for your own Canvas account or observed students, and disable fetchproxy if you do not want browser session cookies read. <br>
Risk: The skill can download Canvas course files to local paths. <br>
Mitigation: Send downloads to a dedicated folder and check the destination path before allowing file writes. <br>
Risk: The activation scope is broad for Canvas-related requests. <br>
Mitigation: Use explicit Canvas-only prompts and review responses before relying on grade, assignment, inbox, or planner information. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/chrischall/skills/canvas-parent) <br>
- [npm package: canvas-parent-mcp](https://www.npmjs.com/package/canvas-parent-mcp) <br>
- [Source: canvas-parent-mcp](https://github.com/chrischall/canvas-parent-mcp) <br>
- [fetchproxy extension](https://github.com/chrischall/fetchproxy) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Files, Guidance] <br>
**Output Format:** [Markdown text with configuration snippets, shell commands, Canvas data summaries, and optional downloaded files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can use Canvas MCP tools to read account, course, grade, planner, inbox, announcement, discussion, and file data when configured with Canvas authentication.] <br>

## Skill Version(s): <br>
1.2.4 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

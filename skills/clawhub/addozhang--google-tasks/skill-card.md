## Description: <br>
Fetch, display, create, and delete Google Tasks through the Google Tasks API using OAuth-backed bash scripts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[addozhang](https://clawhub.ai/user/addozhang) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and agents use this skill to manage personal or work Google Tasks lists from an agent workspace, including listing tasks, creating task items, and deleting selected tasks after OAuth setup. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can create or delete live Google Tasks. <br>
Mitigation: Review the task list, task title, and deletion target before running write or delete commands. <br>
Risk: OAuth credentials and token.json are stored locally. <br>
Mitigation: Keep credentials.json and token.json private and avoid shared or committed workspaces. <br>
Risk: The requested OAuth scope grants read and write access to Google Tasks. <br>
Mitigation: Install only when read/write Google Tasks access is acceptable for the intended workspace. <br>


## Reference(s): <br>
- [Google Tasks API Setup](references/setup.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/addozhang/skills/google-tasks) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance] <br>
**Output Format:** [Markdown and terminal text with bash command examples and Google Tasks status output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires local OAuth credentials and token files; task creation and deletion commands can modify live Google Tasks.] <br>

## Skill Version(s): <br>
1.0.0 (source: SKILL.md frontmatter, package.json, server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

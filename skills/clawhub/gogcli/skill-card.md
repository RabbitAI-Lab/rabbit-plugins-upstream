## Description: <br>
Command-line tool to manage Google Workspace services including Gmail, Calendar, Drive, Sheets, Docs, Slides, Contacts, Tasks, People, Groups, and Keep. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[luccast](https://clawhub.ai/user/luccast) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operators use this skill when they need an agent to install or use gogcli for Google Workspace tasks such as searching Gmail, listing calendar events, uploading Drive files, exporting Sheets, and managing contacts or tasks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires installing an external CLI tool. <br>
Mitigation: Verify the gogcli repository or Homebrew tap before installation, and avoid sudo unless a global install is necessary. <br>
Risk: The skill may access or modify sensitive Google Workspace data. <br>
Mitigation: Enable only the Google APIs needed for the task and confirm account identity, recipients, file paths, event details, and other parameters before commands that send, upload, create, or modify data. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/luccast/skills/gogcli) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration instructions] <br>
**Output Format:** [Markdown with inline bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include JSON-oriented command examples when the gogcli --json flag is relevant.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

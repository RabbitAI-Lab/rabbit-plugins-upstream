## Description: <br>
Read cookies from mainstream browsers and convert to specified format. <br>

This skill is for research and development only. <br>

## Publisher: <br>
[dkgee](https://clawhub.ai/user/dkgee) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and technical users use this skill to extract cookies for a specified domain from a browser profile they control and convert them into JSON, HTTP Cookie header, or cURL command formats. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Exported browser cookies can act like login credentials and may be exposed if pasted into chats, logs, tickets, or shared files. <br>
Mitigation: Use the skill only for browser profiles you control, treat all output as credentials, and avoid sharing or logging cookie values. <br>
Risk: Saving cookie output to a file can leave sensitive credentials on disk. <br>
Mitigation: Save cookie files only when necessary, protect access to them, and delete them promptly after use. <br>


## Reference(s): <br>
- [Browser Cookie Manager on ClawHub](https://clawhub.ai/dkgee/skills/browser-cookie-manager) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, shell commands, files] <br>
**Output Format:** [JSON, HTTP Cookie header text, cURL command text, or a user-specified output file] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may contain browser cookies that can function like credentials.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

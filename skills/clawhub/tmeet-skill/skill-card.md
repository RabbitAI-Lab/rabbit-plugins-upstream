## Description: <br>
Guides an agent in using the Tencent Meeting tmeet CLI for OAuth authentication, meeting lifecycle management, recordings and transcripts, reports, contact lookup for allowed meeting workflows, in-meeting controls, and troubleshooting feedback. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[wemeeting](https://clawhub.ai/user/wemeeting) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill to operate Tencent Meeting through the tmeet command-line tool, including authentication, scheduling, updating, canceling, querying, recording, transcript, report, contact, and in-meeting control workflows. It is also used to prepare troubleshooting feedback when the CLI is missing a needed capability, fails, or returns unexpected results. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may install a global npm package before use. <br>
Mitigation: Confirm the global npm installation and package source before allowing the agent to install or update the tmeet CLI. <br>
Risk: OAuth authorization gives the agent access to Tencent Meeting account data and meeting operations. <br>
Mitigation: Treat authorization URLs and tokens as sensitive, do not print access or refresh tokens, and confirm the intended account before continuing. <br>
Risk: Meeting updates, cancellations, invitee changes, in-meeting calls or kicks, logout, and recording permission requests can affect users or account state. <br>
Mitigation: Show the user the exact planned action and require explicit confirmation before executing any write or high-impact command. <br>
Risk: Diagnostic log export and upload can expose meeting, account, or local environment details. <br>
Mitigation: Review and redact diagnostic logs before upload, and only upload after the user explicitly approves the feedback submission. <br>
Risk: Contact lookup results can expose directory information or be misused as member identifiers for unsafe workflows. <br>
Mitigation: Use contact search only for documented meeting invitation, in-meeting call, or invitee-name resolution workflows, and never use contact results as the source for kicking participants. <br>


## Reference(s): <br>
- [tmeet auth reference](references/tmeet-auth.md) <br>
- [tmeet meeting reference](references/tmeet-meeting.md) <br>
- [tmeet record reference](references/tmeet-record.md) <br>
- [tmeet report reference](references/tmeet-report.md) <br>
- [tmeet contact reference](references/tmeet-contact.md) <br>
- [tmeet control reference](references/tmeet-control.md) <br>
- [tmeet troubleshooting reference](references/tmeet-tshoot.md) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, JSON, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON command output handling] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires the tmeet CLI, OAuth authorization, ISO 8601 timestamps with timezone, explicit confirmation for high-risk operations, and compact JSON output for most query commands.] <br>

## Skill Version(s): <br>
1.0.6 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

## Description: <br>
CLI for Frappe Framework / ERPNext instances. Use when user asks about "Frappe", "ERPNext", "doctypes", "Frappe API", or needs to manage documents, files, reports, or call RPC methods on a Frappe site. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[pasogott](https://clawhub.ai/user/pasogott) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operators use this skill to manage Frappe Framework and ERPNext sites through the frappecli command-line interface, including document operations, files, reports, and RPC calls. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide an agent to change, delete, upload, export, or call methods against Frappe/ERPNext business data. <br>
Mitigation: Use least-privilege API keys, start with staging when possible, and manually confirm production deletes, updates, uploads, exports, and RPC calls. <br>
Risk: The skill configures API credentials for Frappe/ERPNext sites. <br>
Mitigation: Protect the frappecli config file and install the external frappecli package only when the publisher and package source are trusted. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Markdown with shell commands and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [None] <br>

## Skill Version(s): <br>
0.1.1 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

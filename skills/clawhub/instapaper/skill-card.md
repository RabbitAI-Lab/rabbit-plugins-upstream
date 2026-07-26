## Description: <br>
Use when operating the instapaper-cli (ip) tool or troubleshooting it: authenticating, listing/exporting/importing bookmarks, bulk mutations, folders/highlights/text, choosing output formats (ndjson/json/plain), cursor-based sync, and interpreting stderr-json/exit codes for automation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[vburojevic](https://clawhub.ai/user/vburojevic) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and automation users use this skill to operate and troubleshoot Instapaper bookmark workflows through the ip CLI, including authentication, sync/export/import, bulk mutations, folder/highlight/text commands, and structured error handling. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill instructs users to install and operate the external ip CLI, which could be unsafe if obtained from an untrusted source. <br>
Mitigation: Install the ip CLI only from a trusted source and consider pinning or reviewing a specific release before use. <br>
Risk: Authentication workflows may expose Instapaper credentials if passwords are typed directly into shell commands or stored in logs. <br>
Mitigation: Use password-stdin or environment-based credentials, avoid logging secrets, and do not store real passwords in command history. <br>
Risk: Bulk import, export, folder, highlight, progress, and delete commands can read or modify account data at scale. <br>
Mitigation: Require explicit approval before bulk or destructive operations, and use dry-run, idempotent, batch, and confirmation flags where available. <br>


## Reference(s): <br>
- [Commands](references/commands.md) <br>
- [Output, progress, and sync](references/output-and-sync.md) <br>
- [Errors and exit codes](references/errors.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON/NDJSON output examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May reference NDJSON, JSON, plain text, structured stderr JSON, and progress JSON formats for CLI automation.] <br>

## Skill Version(s): <br>
0.2.9 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

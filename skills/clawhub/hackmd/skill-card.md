## Description: <br>
Work with HackMD documents, including reading, creating, updating, deleting, and tracking changes for personal and team notes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[nulltea](https://clawhub.ai/user/nulltea) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users, developers, and agent operators use this skill to manage HackMD notes through the HackMD CLI and to detect note changes through a local tracking helper. It supports personal and team workspaces for note listing, export, metadata checks, creation, updates, deletes, and change polling. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires a HackMD API token that can expose or modify the user's HackMD account content. <br>
Mitigation: Install only when account access is intended, keep HMD_API_ACCESS_TOKEN out of committed files and logs, and rotate or revoke the token if it may have been exposed. <br>
Risk: Document update and delete commands can change or remove HackMD notes in personal or team workspaces. <br>
Mitigation: Verify note IDs and team paths before write or delete operations, and export important notes before deletion. <br>
Risk: The local tracking file may reveal private note IDs, titles, and timestamps. <br>
Mitigation: Treat ./.hackmd/tracked-notes.json as private workspace state and avoid committing or sharing it unless that metadata is safe to disclose. <br>
Risk: HackMD API rate limits can interrupt note listing, export, or change checks. <br>
Mitigation: Throttle repeated checks and retry only after allowing time for HackMD rate limits to reset. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/nulltea/skills/hackmd) <br>
- [HackMD API endpoint](https://api.hackmd.io/v1) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, json, shell commands, guidance] <br>
**Output Format:** [Markdown guidance with HackMD CLI commands; the tracking helper can output note markdown, status text, or JSON change results.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires hackmd-cli, Node.js for the tracking helper, and HMD_API_ACCESS_TOKEN for HackMD API access. Local tracking state is stored under ./.hackmd/tracked-notes.json.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and artifact/_meta.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

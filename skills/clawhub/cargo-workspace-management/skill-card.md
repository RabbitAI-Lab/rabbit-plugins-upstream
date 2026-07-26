## Description: <br>
Manage workspace users, API tokens, folders, roles, and submit reports to workspace management using the Cargo CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cargo-ai](https://clawhub.ai/user/cargo-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, operators, and workspace administrators use this skill to manage Cargo workspace members, roles, API tokens, folders, files, session records, and workspace-management reports from the Cargo CLI. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Workspace administration commands can require broad Cargo permissions. <br>
Mitigation: Use the skill only with a Cargo workspace and account where the operator is comfortable granting the needed administrative authority. <br>
Risk: API tokens and uploaded workspace files can expose sensitive access or data. <br>
Mitigation: Avoid unnecessary sensitive file uploads, create narrowly justified tokens, and store token values in a secrets manager immediately after creation. <br>
Risk: Session hooks can record session titles, summaries, and transcript-derived activity. <br>
Mitigation: Decline or disable the hooks unless the user explicitly wants that activity recorded. <br>
Risk: The installer path includes piping a remote script into a shell. <br>
Mitigation: Prefer a reviewed, pinned, or package-managed installer path before deployment. <br>


## Reference(s): <br>
- [Response shapes](artifact/references/response-shapes.md) <br>
- [Troubleshooting](artifact/references/troubleshooting.md) <br>
- [User management examples](artifact/references/examples/users.md) <br>
- [API token examples](artifact/references/examples/tokens.md) <br>
- [Folder examples](artifact/references/examples/folders.md) <br>
- [Report examples](artifact/references/examples/reports.md) <br>
- [Session tracking examples](artifact/references/examples/sessions.md) <br>
- [Cargo skills homepage](https://github.com/getcargohq/cargo-skills) <br>
- [Cargo installer](https://api.getcargo.io/install.sh) <br>
- [ClawHub skill page](https://clawhub.ai/cargo-ai/skills/cargo-workspace-management) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, Markdown] <br>
**Output Format:** [Markdown guidance with Cargo CLI commands and JSON response examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires the Cargo CLI and authenticated Cargo workspace access.] <br>

## Skill Version(s): <br>
1.2.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

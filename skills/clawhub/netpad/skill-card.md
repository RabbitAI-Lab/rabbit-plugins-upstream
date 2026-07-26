## Description: <br>
NetPad helps agents manage forms, submissions, users, groups, roles, marketplace apps, and NetPad data through the REST API and NetPad CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mrlynn](https://clawhub.ai/user/mrlynn) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operators use this skill to create and publish NetPad forms, query or export submissions, and manage organization RBAC and marketplace packages. It is suited to automation workflows that need REST API examples, CLI commands, or shell snippets for NetPad administration. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can delete forms and submissions, change RBAC, and install apps when given sufficiently privileged NetPad credentials. <br>
Mitigation: Use least-privilege or non-production credentials and manually confirm delete, RBAC, and app-install actions before execution. <br>
Risk: Bulk submission export can expose sensitive form data. <br>
Mitigation: Export only the data needed for the task and define a handling plan for downloaded submission data before running export commands. <br>
Risk: A production NETPAD_API_KEY may allow broad changes to live NetPad resources. <br>
Mitigation: Prefer test or scoped API keys for automation, and rotate credentials if a key is exposed in prompts, logs, or shell history. <br>


## Reference(s): <br>
- [NetPad API v1 Endpoint Reference](artifact/references/api-endpoints.md) <br>
- [NetPad CLI Reference](artifact/references/cli-commands.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/mrlynn/skills/netpad) <br>
- [Publisher Website](https://mlynn.org) <br>
- [Publisher LinkedIn](https://linkedin.com/in/mlynn) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, code, shell commands, configuration] <br>
**Output Format:** [Markdown with REST API examples, CLI commands, shell snippets, and JSON payloads] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include commands that call NetPad APIs or the NetPad CLI and may reference NETPAD_API_KEY, NETPAD_BASE_URL, curl, jq, and netpad.] <br>

## Skill Version(s): <br>
1.0.0 (source: evidence release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

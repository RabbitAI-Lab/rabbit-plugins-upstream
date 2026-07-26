## Description: <br>
Manage Mantis Bug Tracker (issues, projects, users, filters, configs) via the official Mantis REST API. Supports full CRUD operations on issues, projects, users, attachments, notes, tags, relationships, and configuration management. Features dynamic instance switching with context-aware base URL and token resolution. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[willykinfoussia](https://clawhub.ai/user/willykinfoussia) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers, administrators, and support teams use this skill to manage MantisBT issues, projects, users, filters, tokens, configuration, and multi-instance workflows through the official REST API. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can enable broad administration of real MantisBT instances, including deletes, user management, token management, impersonation, configuration changes, and cross-instance changes. <br>
Mitigation: Use a least-privilege API token and require explicit human confirmation before destructive or security-sensitive operations. <br>
Risk: API tokens and instance URLs may be exposed if pasted into chat, logs, or generated output. <br>
Mitigation: Prefer environment variables or session context, redact tokens in status output, and avoid storing credentials in conversation history. <br>


## Reference(s): <br>
- [MantisBT](https://www.mantisbt.org/) <br>
- [MantisBT Manager on ClawHub](https://clawhub.ai/willykinfoussia/skills/mantis-manager) <br>


## Skill Output: <br>
**Output Type(s):** [API Calls, Shell commands, Configuration, Guidance, Markdown] <br>
**Output Format:** [Markdown with REST endpoint examples, JSON request bodies, and configuration guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires MANTIS_BASE_URL and MANTIS_API_TOKEN; supports temporary or session-scoped base URL and token overrides.] <br>

## Skill Version(s): <br>
0.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

## Description:

Firebase Management API integration with managed OAuth for managing Firebase projects, web apps, Android apps, iOS apps, app configurations, and Google Analytics links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect and manage Firebase projects and registered apps through Maton-managed OAuth. It is intended for read-first workflows, connection management, app CRUD operations, app configuration retrieval, and Google Analytics linking when the user has approved the target account and write action.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The raw Maton API passthrough can act on any Firebase endpoint authorized by the connected account, including endpoints outside the documented examples.

Mitigation: Use the narrowest available OAuth scopes, prefer read-only access when possible, specify the intended profile and connection, and require exact endpoint, payload, and expected effect before approving POST, PUT, PATCH, or DELETE.

Risk: Creating or deleting Firebase connections can grant broad account access or irreversibly revoke automation access.

Mitigation: Require explicit user approval before creating a connection, list and match connection identifiers before deletion, and avoid bypassing interactive confirmation unless the specific connection has already been confirmed.

Risk: Using a Maton API key when the CLI is unavailable exposes a long-lived credential to the process environment.

Mitigation: Prefer OAuth through the CLI; when an API key is required, do not print, log, persist, or pass it on a command line, and send it only to api.maton.ai from a restricted environment.

Risk: Firebase API responses can include sensitive project, app, configuration, or personal data.

Mitigation: Extract only the fields needed for the task and avoid dumping or storing raw responses unless the user explicitly asks for that output.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/firebase)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Firebase Management API Overview](https://firebase.google.com/docs/projects/api/workflow_set-up-and-manage-project)
- [Firebase Management REST API Reference](https://firebase.google.com/docs/reference/firebase-management/rest)
- [Firebase Projects Resource](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects)
- [Firebase Web Apps Resource](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.webApps)
- [Firebase Android Apps Resource](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.androidApps)
- [Firebase iOS Apps Resource](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.iosApps)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, JSON examples, and SDK code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and a Firebase connection; API responses may contain sensitive project or app configuration data.]

## Skill Version(s):

1.2.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

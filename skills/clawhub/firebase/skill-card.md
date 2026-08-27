## Description:

Firebase Management API integration with managed OAuth for managing Firebase projects, web apps, Android apps, iOS apps, app configurations, and Google Analytics links through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to manage Firebase projects and app resources through Maton-managed OAuth. It helps agents list projects, create or update apps, retrieve app configuration, and link Google Analytics after user approval for write operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access and change Firebase resources through Maton-mediated account access.

Mitigation: Install only when Maton-mediated Firebase access is intended; review requested OAuth scopes, prefer least-privilege or read-only scopes, and require confirmation before creating connections or changing Firebase resources.

Risk: Write operations such as creating, updating, linking, or deleting Firebase resources can affect the connected account.

Mitigation: Default to read/list calls, verify resource identifiers and account context first, and confirm the target resource, payload, and intended effect before any POST, PUT, PATCH, or DELETE request.

Risk: Ambiguous Maton profiles or Firebase connections can route requests to the wrong account.

Mitigation: Use explicit profile and connection selectors when more than one Maton account or Firebase connection exists, and verify the active connection before writes.

Risk: Fallback API-key use can expose a long-lived Maton credential if printed, persisted, or passed on a command line.

Mitigation: Prefer OAuth through the Maton CLI credential store; if raw HTTP is unavoidable, do not print or persist the key, feed authorization through stdin, and send it only to api.maton.ai.

## Reference(s):

- [ClawHub Firebase Skill](https://clawhub.ai/byungkyu/skills/firebase)
- [Maton](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Firebase Management API Overview](https://firebase.google.com/docs/projects/api/workflow_set-up-and-manage-project)
- [Firebase Management REST API Reference](https://firebase.google.com/docs/reference/firebase-management/rest)
- [Firebase Projects Resource](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects)
- [Firebase Web Apps Resource](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.webApps)
- [Firebase Android Apps Resource](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.androidApps)
- [Firebase iOS Apps Resource](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.iosApps)
- [Related API Gateway Skill](https://clawhub.ai/byungkyu/api-gateway)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API Calls, Code, Configuration]

**Output Format:** [Markdown with inline bash, JSON, Python, and JavaScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and a user-approved Firebase OAuth connection; defaults to read/list operations and requires confirmation before writes.]

## Skill Version(s):

1.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

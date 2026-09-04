## Description:

Firebase Management API integration with managed OAuth for managing Firebase projects, web apps, Android apps, iOS apps, and Google Analytics links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect and manage Firebase projects and registered web, Android, and iOS apps through Maton-managed OAuth. It is suited for listing resources, retrieving app configuration, creating or updating apps, and linking or removing Google Analytics when the user has confirmed the intended account and change.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can operate on Firebase resources in the connected account, including writes and deletions.

Mitigation: Use read or list calls first, confirm the target account and resource identifiers, and require explicit user approval before POST, PUT, PATCH, or DELETE operations.

Risk: Authorizing Maton grants it access to the selected Firebase account.

Mitigation: Prefer OAuth, choose the narrowest available Firebase scopes, specify the intended connection when multiple accounts exist, and revoke unused Firebase connections when work is complete.

Risk: Fallback API-key authentication can expose a long-lived credential if printed, persisted, or passed on a command line.

Mitigation: Use OAuth where possible; when an API key is unavoidable, read it from the process environment only, never log or persist it, and rotate it if exposure occurs.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/firebase)
- [Maton Homepage](https://maton.ai)
- [Firebase Management API Overview](https://firebase.google.com/docs/projects/api/workflow_set-up-and-manage-project)
- [Firebase Management REST API Reference](https://firebase.google.com/docs/reference/firebase-management/rest)
- [Firebase Projects Resource](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects)
- [Firebase Web Apps Resource](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.webApps)
- [Firebase Android Apps Resource](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.androidApps)
- [Firebase iOS Apps Resource](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.iosApps)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce Maton CLI commands, SDK snippets, Firebase API paths, JSON request bodies, and operational guidance.]

## Skill Version(s):

1.2.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

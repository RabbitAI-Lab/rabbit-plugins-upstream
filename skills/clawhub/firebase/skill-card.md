## Description:

Firebase Management API integration with managed OAuth for listing and managing Firebase projects, web apps, Android apps, iOS apps, app configurations, and Google Analytics links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to operate Firebase Management API workflows through Maton, including project discovery, app lifecycle management, configuration retrieval, and Google Analytics linking. It is intended for agents that need guided Firebase API calls while preserving OAuth handling, connection selection, and explicit approval for writes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authorizing Maton for Firebase can grant access to resources in the connected Firebase account.

Mitigation: Prefer OAuth, select the narrowest available Firebase scopes, specify the intended connection when multiple accounts exist, and require user confirmation before creating a new connection.

Risk: The raw API passthrough can reach Firebase endpoints beyond the documented examples when the connection permits it.

Mitigation: Default to documented read/list calls, verify the target resource first, and require explicit confirmation of the endpoint, payload, and expected effect before any create, update, delete, Analytics-linking, or passthrough write.

Risk: Connection deletion and Firebase delete operations can interrupt automation or remove resources.

Mitigation: List and match exact identifiers before deletion, describe the effect to the user, and avoid using prompt-skipping flags unless the user has already confirmed the specific resource.

Risk: Using a Maton API key instead of OAuth increases exposure of a long-lived credential.

Mitigation: Use API keys only where the CLI cannot be installed, keep keys in the process environment or a secret store, never print or persist them, and rotate any key that was exposed.

Risk: Firebase responses can contain personal data or provider-issued credentials.

Mitigation: Extract only fields needed for the task, do not dump raw responses into logs or files, and never print, persist, or forward credentials except to the intended Maton API host for the current request.

## Reference(s):

- [ClawHub Firebase Skill](https://clawhub.ai/byungkyu/skills/firebase)
- [Publisher Profile](https://clawhub.ai/user/byungkyu)
- [Maton](https://maton.ai)
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

**Output Format:** [Markdown with inline shell commands, JSON examples, and SDK code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance emphasizes read/list defaults, explicit approval for writes and connection changes, OAuth preference, least-privilege scopes, and minimized response handling.]

## Skill Version(s):

1.2.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

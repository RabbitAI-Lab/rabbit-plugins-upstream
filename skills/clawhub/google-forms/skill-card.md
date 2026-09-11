## Description:

Google Forms API integration with managed OAuth for creating forms, adding questions, and retrieving responses through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to connect an authorized Google Forms account through Maton, create and update forms, add supported question types, and retrieve form metadata and responses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authorizing a connection grants Maton access to the selected Google Forms account.

Mitigation: Prefer OAuth, verify the target account and connection before use, select the least-privileged scopes available, and revoke unused connections.

Risk: Write operations can create or modify forms, questions, or related form data.

Mitigation: Default to read and list calls first, then require explicit user approval for the target resource, payload, and intended effect before any POST, PUT, PATCH, or DELETE call.

Risk: API-key fallback uses a long-lived credential that can leak through logs, shell history, files, or child processes.

Mitigation: Use OAuth and the CLI credential store when possible; if an API key is unavoidable, never print, persist, or pass it on a command line.

Risk: Installing CLI or SDK packages may not meet strict supply-chain controls in some environments.

Mitigation: Use pinned or otherwise verified package versions when the deployment environment requires strict supply-chain control.

## Reference(s):

- [Maton homepage](https://maton.ai)
- [Google Forms API REST reference](https://developers.google.com/workspace/forms/api/reference/rest)
- [Maton Docs](https://docs.maton.ai)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, API calls, Code]

**Output Format:** [Markdown with inline bash, JSON, Python, and JavaScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Maton CLI commands, Google Forms API paths, JSON request bodies, SDK examples, and operational cautions.]

## Skill Version(s):

1.2.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

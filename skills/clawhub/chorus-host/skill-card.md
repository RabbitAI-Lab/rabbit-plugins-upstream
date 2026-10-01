## Description:

Guides agents in publishing files and websites to shareable chorus.host URLs and deploying JavaScript APIs and webhooks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ansh](https://clawhub.ai/user/ansh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users can publish a local file or website as a shareable or temporary link, protect a site with a password, or deploy an API or webhook backend.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Publishing local files can expose secrets or private data on a public site.

Mitigation: Review the exact files before upload, exclude sensitive data, and use password protection or short expiry for sensitive previews.

Risk: The skill instructs the agent to save a reusable API key for future sessions without asking first.

Mitigation: Require explicit user consent before persisting the key; avoid displaying or sharing it.

Risk: Deleting a site or changing its access can disrupt an existing shared link.

Mitigation: Ask for confirmation before deletion or access changes.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/ansh/skills/chorus-host)
- [chorus.host documentation](https://chorus.host/docs)
- [chorus.host API reference](https://chorus.host/openapi.json)
- [chorus.host worker documentation](https://chorus.host/workers)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Guidance]

**Output Format:** [Markdown with URLs and optional code or shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return a public site URL, claim link, or deployed worker URL.]

## Skill Version(s):

3.1.1 (source: server-resolved release; embedded metadata says 3.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Google Tag Manager API integration with managed OAuth for managing GTM accounts, containers, workspaces, tags, triggers, variables, environments, versions, and user permissions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect and manage Google Tag Manager resources through Maton OAuth, including containers, workspaces, tags, triggers, variables, publishing flows, environments, and account or container user permissions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Google Tag Manager writes, publishing, deletion, and permission changes can affect live tracking behavior or user access.

Mitigation: Default to read and list calls, then confirm the exact account, container, workspace, resource, payload, and intended effect before any write, publish, deletion, or permission change.

Risk: OAuth connections and API keys grant access to Google Tag Manager through Maton.

Mitigation: Prefer OAuth, choose the narrowest available GTM scopes, do not print or persist credentials, and revoke unused connections when finished.

Risk: Multiple Maton profiles or GTM connections can cause an operation to target the wrong account or container.

Mitigation: Specify the intended profile or connection when needed and verify account and container identifiers before making changes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/byungkyu/skills/google-tag-manager-api)
- [Maton](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Google Tag Manager API Overview](https://developers.google.com/tag-platform/tag-manager/api/v2)
- [Google Tag Manager API Reference](https://developers.google.com/tag-platform/tag-manager/api/reference/rest)
- [Google Tag Manager Concepts](https://developers.google.com/tag-platform/tag-manager/api/v2/devguide)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, API calls, JSON payloads, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are intended to guide Maton CLI calls and Google Tag Manager API requests; writes and high-impact actions require explicit user confirmation.]

## Skill Version(s):

1.1.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

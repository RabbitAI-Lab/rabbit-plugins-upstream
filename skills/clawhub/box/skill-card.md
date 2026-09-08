## Description:

Box API integration with managed OAuth for managing files, folders, collaborations, shared links, webhooks, and cloud storage through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Agents use this skill when a user needs help reading, uploading, downloading, sharing, organizing, or administering content in a connected Box account. It is intended for workflows where the user has authorized Box access through Maton and can confirm write, delete, sharing, collaboration, webhook, or connection changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Box API access is routed through the Maton gateway and can manage connected Box content after OAuth authorization.

Mitigation: Use the skill only when the user accepts Maton-mediated Box access, prefer OAuth over API keys, and revoke unused Box connections when work is complete.

Risk: Write, delete, shared-link, collaboration, webhook, and connection operations can change access or data in the connected Box account.

Mitigation: Default to read and list calls, then confirm the exact account, connection, resource identifiers, payload, and intended effect before any modifying operation.

Risk: Raw Box responses can contain personal or sensitive business data.

Mitigation: Return only the fields needed for the task and avoid writing full response bodies into logs, files, or user-visible output unless specifically requested.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/box)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Box API Reference](https://developer.box.com/reference)
- [Box Developer Documentation](https://developer.box.com/guides)
- [Box Authentication Guide](https://developer.box.com/guides/authentication)
- [Box SDKs](https://developer.box.com/sdks-and-tools)

## Skill Output:

**Output Type(s):** [guidance, shell commands, code, configuration]

**Output Format:** [Markdown with inline bash, Python, JavaScript, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce Box API request paths, Maton CLI commands, raw HTTPS request examples, OAuth connection steps, and data-minimization guidance.]

## Skill Version(s):

1.2.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

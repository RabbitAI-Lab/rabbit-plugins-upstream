## Description:

Reducto document processing API integration with managed API key authentication for parsing, extracting, splitting, and editing documents.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to access Reducto document processing through Maton, including document parsing, structured extraction, splitting, editing, uploads, pipelines, and job status checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The authenticated API passthrough can reach endpoints beyond the documented examples when the connection permits it.

Mitigation: Prefer read and list calls, use the narrowest available Reducto scopes, specify the intended connection when multiple accounts exist, and confirm every write or delete request before execution.

Risk: Third-party installation and long-lived credential handling can expose Maton or Reducto access.

Mitigation: Install only official Maton packages, avoid administrator privileges unless needed, prefer OAuth over API keys, and never print, log, persist, or pass credentials on command lines.

Risk: Deleting a connection is irreversible and can break automation using that connection.

Mitigation: List connections first, confirm the exact connection identifier with the user, and use deletion only after explicit approval.

Risk: Document-processing responses can contain personal, confidential, or sensitive content.

Mitigation: Extract only the fields needed for the task and avoid dumping full raw responses into logs, files, or user-visible output unless specifically requested.

## Reference(s):

- [Reducto Documentation](https://docs.reducto.ai)
- [Reducto API Reference](https://docs.reducto.ai/api-reference)
- [Reducto Studio](https://studio.reducto.ai)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Maton Community](https://community.maton.ai/)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, API calls, Code]

**Output Format:** [Markdown with bash, JSON, Python, and JavaScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and an authorized Reducto connection.]

## Skill Version(s):

1.2.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

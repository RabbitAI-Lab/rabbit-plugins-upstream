## Description:

Read HoneyBook client-portal data, including contracts, invoices, proposals, payment methods, and workspace status, from a shell using fpx to capture a signed-in browser session and curl to query HoneyBook APIs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and technically capable HoneyBook users use this skill to retrieve client portal records from shell workflows when they need read-only access without running honeybook-mcp.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill relies on direct reuse of a signed-in HoneyBook browser session and exposes bearer tokens, user IDs, trusted-device values, session captures, and saved API responses.

Mitigation: Treat captured session values and API responses like passwords and customer financial records; avoid shared machines, use restrictive temporary files, keep secrets in shell variables when possible, and delete captures immediately.

Risk: The security summary flags predictable temporary files for sensitive session and customer data.

Mitigation: Use private temporary paths or restrictive file permissions for any capture file, and remove the file as soon as the required fields are extracted.

Risk: The security guidance recommends caution because the skill reads a signed-in HoneyBook session through a CLI/browser bridge.

Mitigation: Install only when this access model is acceptable, and prefer official or scoped integrations when they are available.

## Reference(s):

- [HoneyBook requests for fpx + curl](references/requests.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/honeybook-fpx)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill guides agents to produce read-only command patterns and response-handling guidance for HoneyBook client portal data.]

## Skill Version(s):

0.7.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

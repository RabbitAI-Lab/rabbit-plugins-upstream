## Description:

Read HoneyBook client-portal data from a shell by capturing an existing browser session with @fetchproxy/cli and using curl against HoneyBook API endpoints.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and automation users use this skill to retrieve HoneyBook contracts, invoices, proposals, payment methods, and workspace status without running honeybook-mcp, after the user has an authorized HoneyBook portal session.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill teaches capture and reuse of HoneyBook browser-session values, including AUTH_TOKEN, USER_ID, TRUSTED_DEVICE, contracts, invoices, messages, notes, attachments, payment methods, and payment data.

Mitigation: Use it only with explicit authorization, treat all captured values and API responses as sensitive, avoid persisting session captures, and clean up any temporary files containing session or customer data.

Risk: The documented workflow can store captured session data in fixed /tmp paths, which can expose sensitive data on shared systems.

Mitigation: Keep credentials in shell variables when possible, use private temporary storage when files are necessary, restrict file permissions, and delete captures after use.

Risk: The artifact describes a write-capable HoneyBook message workflow that can contact a vendor for real.

Mitigation: Do not use the message-sending workflow unless the user intentionally wants to contact the vendor, and prefer preview-capable tooling when available.

## Reference(s):

- [HoneyBook request examples](references/requests.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/honeybook-fpx)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell and jq examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance includes command patterns for capturing session values, constructing HoneyBook API headers, reading API responses, and handling selected error cases.]

## Skill Version(s):

0.10.5 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

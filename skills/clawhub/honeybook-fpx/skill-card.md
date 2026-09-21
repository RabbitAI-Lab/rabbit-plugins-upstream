## Description:

Read HoneyBook client-portal data from a shell using fpx to capture an authenticated browser session and curl HoneyBook API endpoints without running the honeybook-mcp server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to capture a HoneyBook vendor session from an already signed-in browser profile and issue shell commands for contracts, invoices, proposals, payment methods, and workspace status.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill captures and uses HoneyBook session values and can write HoneyBook business records to temporary files.

Mitigation: Grant fpx access only on trusted browser profiles, keep tokens in shell variables when possible, delete temporary session and response files promptly, and avoid world-readable storage.

Risk: The documented message-sending flow can send real vendor emails.

Mitigation: Use the skill primarily for read workflows, and require explicit user intent before any message-sending flow.

Risk: Expired sessions, stale API versions, rate limits, and pagination can make responses fail or appear incomplete.

Mitigation: Check HTTP status and HoneyBook error bodies, refresh the API version or recapture the session as documented, retry once after 429 responses, and handle pagination when complete results are required.

## Reference(s):

- [HoneyBook requests for fpx + curl](artifact/references/requests.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/honeybook-fpx)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Code, Guidance]

**Output Format:** [Markdown with shell command snippets and jq examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a signed-in HoneyBook browser session, fpx/Transporter pairing, curl, jq, and a current HoneyBook API version.]

## Skill Version(s):

1.1.2 (source: server release metadata, released 2026-09-21)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

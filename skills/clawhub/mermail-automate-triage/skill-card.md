## Description:

Create, inspect, update, and delete Mermail task triagers and review recent triager runs for mailbox automation, task extraction, triager debugging, and triager-linked agent conversations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mermail](https://clawhub.ai/user/mermail)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and Mermail workspace operators use this skill to configure safe mailbox triage automation, troubleshoot recent triager runs, and prepare human-reviewed task extraction or auto-draft workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Inbound mailbox content can carry untrusted instructions, malicious active content, or misleading sender claims.

Mitigation: Require clean scan status, bounded sanitized content, sender authentication checks, and metadata-only attachment handling unless a specific attachment task is approved.

Risk: A triager change could unintentionally broaden sender scope, outputs, integrations, recipients, or external effects.

Mitigation: Show the exact configuration diff, keep automation disabled during review, use a minimum allowlist, and preserve existing configuration unless the user explicitly approves the change.

Risk: Deletion, sending, credential use, OTP or magic-link handling, or other high-impact effects could occur without adequate confirmation.

Mitigation: Require fresh human confirmation for high-impact effects, bind destructive deletion to a single-use approval token, and keep default triager selection out of scope.

## Reference(s):

- [Mermail AI Skills Documentation](https://docs.mermail.app/ai/skills)
- [Triager Security Boundary](references/security.md)
- [Triage Tool Map](references/tools.md)
- [Mermail MCP Server](https://console.mermail.app/mcp)

## Skill Output:

**Output Type(s):** [Text, Markdown, Configuration, Guidance]

**Output Format:** [Markdown with structured status reports, configuration diffs, and approval prompts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Mermail MCP access and MERMAIL_API_KEY; destructive deletion requires explicit approval.]

## Skill Version(s):

1.2.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

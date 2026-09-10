## Description:

Audits MCP and agent server configurations with 14 static checks for hardcoded credentials, command execution, writable mounts, SSRF exposure, plaintext endpoints, unpinned launchers, and related risks, returning severity-ranked findings with remediation advice.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dshcorrectover](https://clawhub.ai/user/dshcorrectover)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to review MCP or agent server configuration JSON before connecting servers to an agent, with local static checks that flag risky capabilities and provide remediation guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The optional online mode can submit full MCP configuration data, including credentials present in the config, to a hosted service.

Mitigation: Use the default local mode for sensitive configurations; use --online only when the user intentionally accepts hosted processing.

Risk: The hosted service endpoint can be overridden, which could route submitted configuration data to an untrusted host.

Mitigation: Do not use --endpoint or CCS_API_ENDPOINT unless the endpoint is trusted and expected for the review.

Risk: Payment proof and API token environment variables may be sent when online mode is used.

Mitigation: Clear CCS_API_TOKEN, CCS_PAYMENT_PROOF, and CCS_PAY_TOKEN unless they are needed for a trusted hosted check.

Risk: Static checks are a first-pass screen and do not assess live endpoint behavior, server implementation code, permission boundaries, or data flows.

Mitigation: Treat findings as triage input and perform qualified manual review before relying on a security decision.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dshcorrectover/skills/mcp-config-security-checkup)
- [Correctover homepage](https://correctover.com/?utm_source=clawhub&utm_medium=skill&utm_campaign=ccs_checkup)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Console text by default, with optional machine-readable JSON report output.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Severity-ranked CRIT/HIGH/MED/LOW findings include rule IDs, server names, redacted evidence, and remediation advice.]

## Skill Version(s):

1.0.1 (source: ClawHub server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

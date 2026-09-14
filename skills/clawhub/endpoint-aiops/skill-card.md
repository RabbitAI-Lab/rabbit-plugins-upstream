## Description:

Endpoint AIops helps agents operate managed endpoint fleets by gathering fleet health, inventory, login and boot sessions, login-storm analysis, drift and patch reports, and guarded profile assignment or reboot actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and endpoint operations teams use this skill to triage thin-client, VDI, or centrally managed endpoint fleets, diagnose login storms and drift, and prepare governed remediation actions such as profile assignment or reboot.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can reboot endpoints and change configuration profiles through an external endpoint-management package.

Mitigation: Use a read-only management account by default, enable write-capable credentials only for deliberate maintenance, and preview state-changing actions with dry-run before execution.

Risk: The connected endpoint-management account determines whether writes are permitted; the skill does not provide its own read-only authorization gate.

Mitigation: Enforce least privilege on the management server account and use the agent prompt or operating procedure to restrict write tools during observe-only sessions.

Risk: Legacy plaintext API-key environment variables are still honored as a fallback.

Mitigation: Prefer the encrypted secret store, avoid plaintext legacy environment variables, and migrate existing legacy secrets before production use.

Risk: The artifact states that REST paths are modeled generically and have not yet been exercised against a live management server.

Mitigation: Validate connectivity and behavior against a non-production endpoint-management server before relying on results or remediation actions in production.

## Reference(s):

- [Endpoint AIops repository](https://github.com/AIops-tools/Endpoint-AIops)
- [Capabilities reference](references/capabilities.md)
- [CLI reference](references/cli-reference.md)
- [Setup and security guide](references/setup-guide.md)
- [Agent guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and structured tool-result summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can include capped-list metadata, fleet counts, health scoring reasons, dry-run previews, and audit or undo references when supported by the tool.]

## Skill Version(s):

0.10.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

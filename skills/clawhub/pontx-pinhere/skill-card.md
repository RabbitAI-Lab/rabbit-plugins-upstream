## Description:

Integrate Pinhere safely through Pontx for private issue collaboration, browser-extension capture, project setup, Webhooks, PATs, OAuth, and explicitly approved state changes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pontjs](https://clawhub.ai/user/pontjs)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to integrate Pinhere through Pontx while preserving privacy boundaries, using least-privilege credentials, previewing direct calls, and requiring explicit approval for issue, token, OAuth, browser-extension, and Webhook changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pinhere workflows may expose private project data, issue content, DOM context, screenshots, token metadata, Webhook diagnostics, PATs, OAuth values, session cookies, or one-time secrets.

Mitigation: Minimize fetched and returned data, redact previews, keep credentials in caller-owned storage or local process context, and avoid logging or forwarding sensitive values.

Risk: State-changing issue, token, OAuth, browser-extension, or Webhook actions can affect persistent resources or security posture.

Mitigation: Resolve the exact target, present method, path, redacted input, and expected effect, then require explicit approval and a fresh preview if the operation changes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/pontjs/skills/pontx-pinhere)
- [ClawHub publisher profile](https://clawhub.ai/user/pontjs)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Code]

**Output Format:** [Markdown with inline shell commands and implementation guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Emphasizes redacted previews, local execution, minimal disclosure, and explicit approval before state-changing operations.]

## Skill Version(s):

1.0.0 (source: evidence.release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

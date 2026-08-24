## Description:

Create a Douyin shopping video, Douyin UGC ad, or AI creator product pitch from a product photo, product details, and an on-camera direction.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, and commerce teams use this skill to turn an inspectable product photo, merchant-approved product details, and a creator direction into a short vertical Douyin UGC-style product ad. The workflow helps an agent prepare a presenter frame, spoken pitch, narration, final video request, billing-aware confirmations, and recovery steps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill stores a shared local Beatra bearer credential with spending-related scope.

Mitigation: Authorize only accounts approved for this workflow, keep the credential file private, and revoke or reconnect access when the installation should no longer use that account.

Risk: The bundled client silently checks for and installs package updates by default.

Mitigation: Disable automatic updates with `python3 scripts/mcp_client.py update --auto off` when managed environments require explicit change control.

Risk: The skill sends installation telemetry and tracks local skill installs.

Mitigation: Review the installation behavior before deployment in sensitive environments and document whether local inventory tracking is acceptable.

Risk: Generation calls can consume Beatra credits and may involve retries after transport uncertainty.

Mitigation: Use the documented staged confirmations, stable request IDs, and polling recovery flow so changed work receives new approval and duplicate paid submissions are avoided.

## Reference(s):

- [Douyin UGC ad workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Bundled MCP Client diagnostics](references/mcp-connection.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)
- [Beatra top-up console](https://console.beatra.ai/topup)
- [Beatra MCP endpoint](https://mcp.beatra.ai/mcp)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API Calls, Markdown]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes staged paid-generation confirmations, task polling, artifact links, and billing facts.]

## Skill Version(s):

0.1.7 (source: release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

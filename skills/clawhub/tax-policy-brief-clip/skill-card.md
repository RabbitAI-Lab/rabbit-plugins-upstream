## Description:

Turn a dated tax-policy source into a policy-points still and a speakable brief, then into one short tax policy brief clip.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External bookkeeping firms and tax advisors use this skill to turn advisor-supplied, dated tax-policy source text into a policy-points still, a speakable brief, and one short client-facing update clip.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The package can use a shared Beatra device authorization that may spend Beatra credits and access Beatra task and artifact data.

Mitigation: Install only for users who accept that account authority, review the authorization scope, and require explicit approval before billable image, speech, or video generation.

Risk: Local media selected by the user may be uploaded to Beatra for generation workflows.

Mitigation: Inspect supplied files first, upload only intended media through the bundled client, and avoid using sensitive or unnecessary local files.

Risk: The package stores a persistent shared credential under the user's Beatra state directory.

Mitigation: Use the documented private-file handling, avoid exposing tokens in chat, logs, command arguments, or environment variables, and revoke access from the Beatra Console or uninstall flow when no longer needed.

Risk: The bundled client can silently update package files unless automatic updates are disabled.

Mitigation: Disable automatic updates with `scripts/mcp_client.py update --auto off` in managed or regulated environments and review updates before re-enabling them.

Risk: The security evidence classifies the release as suspicious because of broad account authority, shared credential handling, telemetry, uninstall account actions, and silent self-updating code.

Mitigation: Review the package and its security summary before deployment, especially in managed, regulated, or high-trust environments.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/tax-policy-brief-clip)
- [Beatra skill homepage](https://beatra.ai/skills/tax-policy-brief-clip)
- [Tax policy brief workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [MCP connection](references/mcp-connection.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces planning text and Beatra task guidance; generated media artifacts are created through the bundled client after user approval.]

## Skill Version(s):

0.1.1 (source: server release metadata and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

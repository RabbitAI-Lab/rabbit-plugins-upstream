## Description:

Turns a dated tax-policy source into a policy-points still, a speakable brief, and one short tax policy brief clip for bookkeeping-firm and tax-advisor updates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External tax advisors and bookkeeping firms use the skill to convert advisor-supplied, dated tax-policy sources into a policy-points still, speakable brief, and short client update clip. The workflow is limited to sourced policy points and avoids concrete tax-planning schemes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The package uses a shared Beatra account credential with broad generation and tool access.

Mitigation: Install only when that access is acceptable, keep the credential local, and revoke or reconnect the Beatra device authorization if the account or device should no longer be trusted.

Risk: Silent automatic package updates are enabled by default.

Mitigation: Use the documented update command to disable automatic updates when review-before-update is required, and rely only on verified package-owned file replacement.

Risk: Paid image, speech, and video calls can create charges or duplicate work if retried incorrectly.

Mitigation: Show the production card before each paid slot, use one opaque request ID per approved call, poll existing tasks, and retry only unchanged requests with the same request identity.

Risk: Tax-policy outputs could mislead users if the skill invents facts or drifts into tax-planning advice.

Mitigation: Require the user-supplied source and effective date, keep outputs to confirmed policy points, refuse concrete planning schemes, and state when the result is not a formal tax opinion.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/beatra-ai/skills/tax-policy-brief-clip)
- [Beatra Skill Homepage](https://beatra.ai/skills/tax-policy-brief-clip)
- [Tax policy brief workflow](artifact/references/workflow.md)
- [Installation and authentication](artifact/references/installation-and-auth.md)
- [Installation registration](artifact/references/installation-registration.md)
- [Tasks and results](artifact/references/tasks-and-results.md)
- [Billing, errors, and recovery](artifact/references/billing-errors-and-recovery.md)
- [Bundled MCP Client diagnostics](artifact/references/mcp-connection.md)
- [Automatic updates and safety](artifact/references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](artifact/references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON and shell command snippets; generated Beatra tasks can return image, audio, and video artifacts.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses asynchronous paid image, speech, and video tasks; terminal results should include returned usage, artifact metadata, and net charged credits when present.]

## Skill Version(s):

0.1.2 (source: server release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

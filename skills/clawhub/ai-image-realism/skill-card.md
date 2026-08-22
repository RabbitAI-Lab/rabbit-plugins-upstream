## Description:

Improve AI image realism without starting over by repairing visible AI-image artifacts such as plastic skin, malformed hands or faces, repeated textures, and inconsistent lighting while preserving identity, product shape, brand details, and composition where possible.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to repair an existing AI-generated portrait, product image, marketing visual, or social cover through Beatra image edit or transform calls. It helps diagnose one priority visual defect, confirm paid execution boundaries, submit the request, poll the resulting task, and report outputs, dimensions, billing credits, and visible drift.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill connects a Beatra account and uses a broad shared Device Token stored under ~/.beatra.

Mitigation: Install only when this shared authorization is acceptable, keep the credential private, and revoke the device in the Beatra Console or through the documented uninstall flow when access is no longer needed.

Risk: Selected images are uploaded to Beatra for generation work and confirmed generation calls spend Beatra credits.

Mitigation: Confirm the image, route, model, output count, and paid execution boundary before submission; report final billing.net_charged_credits from the terminal task result.

Risk: The bundled client silently checks for and installs package updates by default.

Mitigation: Review this behavior before installation and disable automatic updates with python3 scripts/mcp_client.py update --auto off when silent package updates are not acceptable.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/beatra-ai/skills/ai-image-realism)
- [Beatra skill homepage](https://beatra.ai/skills/ai-image-realism)
- [Beatra MCP endpoint](https://mcp.beatra.ai/mcp)
- [Diagnosis and routing](references/diagnosis-and-routing.md)
- [Repair recipes](references/repair-recipes.md)
- [Review and recovery](references/review-and-recovery.md)
- [Installation and authentication](references/installation-and-auth.md)
- [MCP connection](references/mcp-connection.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, API Calls]

**Output Format:** [Markdown guidance with inline shell commands, Beatra MCP tool payloads, task status details, artifact links, dimensions, and billing fields.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces one focused repair workflow by default, requires user confirmation before paid calls, and reports visual-review limits when the host agent cannot inspect the result.]

## Skill Version(s):

0.2.6 (source: server release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

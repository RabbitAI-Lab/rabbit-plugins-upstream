## Description:

Turn final manuscript or course text into ordered chapter audio with one consistent narrator, a representative sample, clear pricing, and focused refinements.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Authors, course creators, and production operators use this skill to turn final manuscript or course text into ordered chapter audio with one consistent narrator. It guides intake, pronunciation handling, narrator selection or cloning, pilot review, pricing confirmation, paid synthesis, recovery, and delivery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a broad reusable Beatra device token and stores local account state under `~/.beatra`.

Mitigation: Install only in environments where Beatra account access is acceptable, review the skill before managed deployment, and disconnect or uninstall when access is no longer needed.

Risk: Automatic package updates are enabled by default and can replace package files during normal use.

Mitigation: Disable silent updates with `python3 scripts/mcp_client.py update --auto off` where change control is required, and review updates before use in sensitive environments.

Risk: The workflow can initiate paid voice cloning, speech synthesis, and image generation operations.

Mitigation: Require explicit approval of the current production card for each paid operation and avoid automatic retries unless the original request identity and arguments are unchanged.

Risk: Package registration telemetry is part of the bundled client behavior.

Mitigation: Use the skill only where this registration behavior is acceptable under the organization's account and telemetry policies.

## Reference(s):

- [AI Audiobook Narration on ClawHub](https://clawhub.ai/beatra-ai/skills/ai-audiobook-narration)
- [Chapter production](references/chapter-production.md)
- [Performance, cost, and quality](references/performance-and-quality.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Delivery and recovery](references/delivery-and-recovery.md)
- [Installation and authentication](references/installation-and-auth.md)
- [MCP connection](references/mcp-connection.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with production cards, JSON argument examples, and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May direct paid Beatra voice clone, speech synthesis, image generation, task polling, and recovery flows after explicit user confirmation.]

## Skill Version(s):

0.1.9 (source: server release metadata and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

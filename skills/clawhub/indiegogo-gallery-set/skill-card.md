## Description:

Turn a written campaign and reward-tier plan into one gallery still per named slot.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External campaign writers, founders, and creative teams use this skill to plan and generate one crowdfunding gallery still per confirmed reward tier or campaign scene while keeping campaign facts, prices, and visual references grounded in the user's written plan.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill grants a Beatra device credential with broad account capabilities.

Mitigation: Review the approval scopes before authorizing, keep the device token only in the protected local credential file, and avoid uploading sensitive local files as image references.

Risk: The bundled client can silently replace package files through automatic updates from Beatra infrastructure.

Mitigation: Install only after review, rely on the packaged update verification and rollback controls, and disable automatic update checks with scripts/mcp_client.py update --auto off when a fixed package version is required.

Risk: Image generation is billable and transport uncertainty can otherwise lead to duplicate paid work.

Mitigation: Use one opaque client_request_id per approved still, retry only identical frozen payloads with the same request identity, and report billing.net_charged_credits from the terminal task result.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/beatra-ai/skills/indiegogo-gallery-set)
- [Publisher profile](https://clawhub.ai/user/beatra-ai)
- [Beatra skill homepage](https://beatra.ai/skills/indiegogo-gallery-set)
- [Crowdfunding gallery workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Tasks and results](references/tasks-and-results.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Files, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and returned image artifacts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [One still is generated per named slot; delivered results include the gallery plan, task IDs, resolved models, observed dimensions and formats, and net charged credits.]

## Skill Version(s):

0.1.2 (source: server evidence and packaged manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

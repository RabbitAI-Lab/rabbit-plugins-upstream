## Description:

Turn one public-education legal topic into a labeled digital-human still, a speakable explainer script, and one talking clip.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Lawyers, firm marketing teams, and agent operators use this skill to turn a general public-education legal topic into a short, labeled digital-human explainer workflow with a still plan, narration script, generated still, speech, and one talking clip. It is not for case-specific legal conclusions, win predictions, or identifiable party facts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a shared Beatra credential stored under ~/.beatra with broad account authority for remote MCP calls.

Mitigation: Install and authorize only in trusted environments, keep the credential file private, and use the documented uninstall or revocation flow when access should end.

Risk: The bundled client silently auto-updates package code by default.

Mitigation: Review the package before sensitive deployment and disable automatic updates with python3 scripts/mcp_client.py update --auto off when change control is required.

Risk: User-selected local files can be uploaded when used as look references.

Mitigation: Inspect files before upload, avoid sensitive or case-identifying material, and upload only the specific file needed for the approved workflow.

Risk: Billable image, speech, and video operations can spend Beatra credits.

Mitigation: Require the documented approval cards, use fresh model and price reads, and reuse request identities only for byte-identical retries.

Risk: Legal explainer content could be mistaken for case-specific legal advice or a real lawyer presentation.

Mitigation: Keep scripts limited to firm-supplied public-education facts, refuse live-matter conclusions, and require the non-lawyer presenter label in the still and clip.

## Reference(s):

- [Legal explainer workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [MCP connection](references/mcp-connection.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)
- [Beatra Legal Explainer Clip](https://beatra.ai/skills/legal-explainer-clip)
- [ClawHub skill listing](https://clawhub.ai/beatra-ai/skills/legal-explainer-clip)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with command examples, JSON payload examples, approval cards, and generated media task results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses Beatra MCP calls for image, speech, video, wallet, upload, task, and installation workflows; generated media artifacts and billing facts come from terminal task responses.]

## Skill Version(s):

0.1.2 (source: server release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

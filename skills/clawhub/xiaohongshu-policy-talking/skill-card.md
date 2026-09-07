## Description:

Turn Xiaohongshu policy-question notes into separate 2 to 15 second talking policy clips from desk-supplied public-policy lines and still images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External service desks and civil-affairs operators use this skill to turn public Xiaohongshu policy questions and approved public-policy wording into short, separate talking clips for each still image.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The package uses a shared Beatra device credential with broad media, artifact, task, and wallet-related authority.

Mitigation: Install only when that authority is acceptable, keep the credential private, and require explicit user approval for paid or canceling operations.

Risk: The bundled client can silently self-update executable package files.

Mitigation: Review the update behavior before installation and disable automatic checks with the documented update command when silent updates are not acceptable.

Risk: Lookup, speech, clone, and video operations can consume credits or create duplicate paid work if retried incorrectly.

Mitigation: Use the skill's six-field approval cards, one opaque client_request_id per approved request, and byte-identical retry rules for uncertain transport outcomes.

Risk: Generated policy clips could misstate policy details or use a likeness or voice without proper rights.

Mitigation: Use only desk-supplied public-policy wording, avoid invented subsidy or eligibility claims, and require likeness and voice rights before cloning or animating a person.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/xiaohongshu-policy-talking)
- [Beatra skill homepage](https://beatra.ai/skills/xiaohongshu-policy-talking)
- [Policy talking workflow](artifact/references/workflow.md)
- [Xiaohongshu policy-question note lookup](artifact/references/note-lookup.md)
- [Installation and authentication](artifact/references/installation-and-auth.md)
- [Installation registration](artifact/references/installation-registration.md)
- [Tasks and results](artifact/references/tasks-and-results.md)
- [Billing, errors, and recovery](artifact/references/billing-errors-and-recovery.md)
- [MCP connection](artifact/references/mcp-connection.md)
- [Automatic updates and safety](artifact/references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](artifact/references/uninstall-and-disconnect.md)
- [Beatra MCP endpoint](https://mcp.beatra.ai/mcp)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration, files]

**Output Format:** [Markdown guidance with command examples, approval cards, task status details, and generated media artifact references.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces separate 2 to 15 second talking clip files and does not stitch them.]

## Skill Version(s):

0.1.2 (source: release evidence and artifact/manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

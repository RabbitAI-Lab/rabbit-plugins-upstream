## Description:

Turn Xiaohongshu policy-question notes into one talking policy clip per still.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External teams such as street-office or civil-affairs desks use this skill to turn public Xiaohongshu policy-question notes and desk-supplied public-policy lines into separate short talking clips. It supports planning, note lookup, speech generation, video animation, task polling, and delivery checks without inventing policy facts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requests broad persistent Beatra device authorization that can spend credits, upload selected media, read and write Beatra artifacts, manage tasks, and be reused by other Beatra skills.

Mitigation: Install only when this account-level access is acceptable, keep the device token private, confirm each paid stage before execution, and use the documented uninstall or disconnect workflow when access is no longer needed.

Risk: The bundled client silently checks for and installs package updates by default.

Mitigation: Review the automatic update behavior before use in controlled environments and run the documented command to disable automatic updates when change control requires manual review.

Risk: The workflow can create paid lookups, voice cloning, speech, and video animation tasks.

Mitigation: Use the required six-field confirmation cards, fresh client request IDs, live price checks, and task polling before each paid stage; do not retry chargeable work unless the recovery guidance allows it.

Risk: Policy clips or cloned voices could misstate public benefits or use a likeness without proper permission.

Mitigation: Use only desk-supplied public-policy facts, do not invent subsidy or eligibility details, inspect source stills, and require likeness and voice rights before cloning or animation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/xiaohongshu-policy-talking)
- [Policy talking-clip workflow](references/workflow.md)
- [Xiaohongshu policy-question note lookup](references/note-lookup.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [MCP connection](references/mcp-connection.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline JSON and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides paid Beatra lookup, speech, and video tasks that may return media artifacts, task metadata, MIME type, duration, size, and billing fields.]

## Skill Version(s):

0.1.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

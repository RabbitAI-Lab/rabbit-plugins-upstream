## Description:

Turn one authorized founder or expert portrait and a weekly script into a talking-head IP video in that person's likeness and voice.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, founders, experts, and brand teams use this skill to create authorized recurring talking-head avatar videos from a portrait, script or approved speech, and voice consent. The skill guides consent checks, paid generation boundaries, task recovery, and review of identity, clarity, and lip timing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill stores a shared Beatra Device Token that can access multiple Beatra capabilities, upload selected portrait or voice files, and spend credits for approved generation work.

Mitigation: Install only when that authorization scope is acceptable, keep the credential private, use the bundled authorization flow, and revoke the device authorization when the skill is no longer needed.

Risk: Silent package updates are enabled by default and can replace package-owned files.

Mitigation: Use the documented update controls to disable automatic updates or check available updates before replacement.

Risk: Avatar and voice generation can misuse a person's likeness or voice if consent and rights are not confirmed.

Mitigation: Require explicit likeness and voice rights, confirm clone consent before uploading samples, and stop before generation when authorization is missing.

Risk: Billable generation steps can create unintended credit charges if retried or submitted before the user approves the paid boundary.

Mitigation: Show clone, narration, and video admission details before paid calls, use one request identity per approved paid step, and recover uncertain responses only with the same unchanged request identity.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/founder-ip-avatar-studio)
- [Beatra skill homepage](https://beatra.ai/skills/founder-ip-avatar-studio)
- [Founder avatar workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [MCP connection](references/mcp-connection.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration, API calls]

**Output Format:** [Markdown guidance with inline JSON and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides asynchronous Beatra voice, speech, video, wallet, task, authorization, update, and uninstall operations.]

## Skill Version(s):

0.1.2 (source: server release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

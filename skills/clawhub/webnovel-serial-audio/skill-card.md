## Description:

Turns serialized web novel chapters into chapter-by-chapter audiobook audio with one consistent narrator for the current chapter and later updates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, publishers, and developers use this skill to produce serialized web novel audiobook chapters, manage narrator selection or consented voice cloning, confirm pronunciation and pricing, and continue later chapters with the same voice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requests one shared Beatra device token with broad media and spending scopes.

Mitigation: Install only in environments where those scopes are acceptable, keep the token in the documented local credential file, and revoke or reconnect the device if account access should change.

Risk: Selected files and chapter text may be sent to Beatra for media generation.

Mitigation: Submit only content the user is authorized to process, avoid secrets or unrelated private material, and confirm consent before any voice cloning request.

Risk: Silent package updates are enabled by default.

Mitigation: Disable automatic checks with `python3 scripts/mcp_client.py update --auto off` in sensitive environments, or use `python3 scripts/mcp_client.py update --check` to inspect updates manually.

Risk: Paid clone and speech requests can consume Beatra credits.

Mitigation: Confirm the voice, pronunciation table, and current estimate before paid submission, then reuse the same frozen request identity only for recovery of uncertain delivery.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/webnovel-serial-audio)
- [Beatra skill homepage](https://beatra.ai/skills/webnovel-serial-audio)
- [Webnovel serial-audio workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, JSON payloads, audio artifact links]

**Output Format:** [Markdown guidance with inline shell commands and JSON request examples; generated results reference audio artifacts, duration, usage, and billing fields.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses Beatra tasks for speech synthesis and optional consented voice cloning; paid generation requires user confirmation before submission.]

## Skill Version(s):

0.1.1 (source: release evidence and artifact/manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

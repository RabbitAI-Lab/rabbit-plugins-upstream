## Description:

Turn one shop portrait and short welcome, product, FAQ, and close scripts into talking-avatar clips a store can loop overnight.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External shop operators and their supporting agents use this skill to prepare authorized overnight talking-avatar clip sets for welcome, product, FAQ, and close segments. It guides consent, media checks, generation, billing review, and delivery of loop-ready avatar clips.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a shared Beatra device token with broad media-generation and spending-related permissions.

Mitigation: Install only in trusted agent environments, keep the token out of logs and prompts, monitor credit usage, and revoke connected-agent access from the Beatra Console when needed.

Risk: Installed code can silently self-update before ordinary commands.

Mitigation: Review the update posture before deployment and disable silent checks with `python3 scripts/mcp_client.py update --auto off` when routine use requires explicit update control.

Risk: Portraits and cloned voices can create likeness or consent issues.

Mitigation: Use only portraits and voices the user owns or is authorized to use, confirm consent before cloning, and stop before generation when rights are not established.

Risk: Voice, speech, and video generation consume Beatra credits and may incur charges.

Mitigation: Show live admission and billing information before paid stages, reuse request identities only for unchanged recovery, and report terminal usage and billing values after task completion.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/beatra-ai/skills/unattended-live-avatar)
- [Beatra skill homepage](https://beatra.ai/skills/unattended-live-avatar)
- [Unattended live avatar workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [MCP connection](references/mcp-connection.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, API calls]

**Output Format:** [Markdown guidance with JSON payloads, shell command snippets, and Beatra task or artifact references.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May result in Beatra-generated speech, voice, and talking-avatar video artifacts plus usage and billing summaries.]

## Skill Version(s):

0.1.2 (source: server release metadata, manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

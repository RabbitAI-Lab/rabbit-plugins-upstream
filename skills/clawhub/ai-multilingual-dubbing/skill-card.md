## Description:

Create multilingual voice-over audio from prepared scripts for videos, product launches, e-learning, training libraries, creator content, and international campaigns.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, localization teams, training teams, marketers, and developers use this skill to plan multilingual narration, select locale-ready voices, confirm paid text-to-speech scope, and deliver reviewable audio results grouped by language, market, and segment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The Beatra shared token can authorize more than speech generation.

Mitigation: Install only with Beatra credentials intended for shared Beatra skill use, keep the credential file private, and reconnect only when the user explicitly chooses to do so.

Risk: Package files may update automatically before ordinary Beatra commands.

Mitigation: Review the package before installation and disable silent update checks with `python3 scripts/mcp_client.py update --auto off` when automatic replacement is not acceptable.

Risk: Paid synthesis can spend credits or duplicate work if scope and retries are handled loosely.

Mitigation: Confirm the complete paid render matrix before synthesis, use one stable request identity per approved cell, and poll existing tasks instead of submitting replacements.

## Reference(s):

- [Dubbing matrix design](references/matrix-design.md)
- [Locale readiness and quality](references/locale-readiness-and-quality.md)
- [Recovery and delivery](references/recovery-and-delivery.md)
- [Installation and authentication](references/installation-and-auth.md)
- [MCP connection](references/mcp-connection.md)
- [Installation registration](references/installation-registration.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [AI Multilingual Dubbing on ClawHub](https://clawhub.ai/beatra-ai/skills/ai-multilingual-dubbing)
- [Beatra AI Multilingual Dubbing](https://beatra.ai/skills/ai-multilingual-dubbing)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, structured task details, and audio artifact links when generation succeeds]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May report locale, segment, voice, task identity, MIME type, size, duration, sample rate when returned, usage, and billing fields.]

## Skill Version(s):

0.1.8 (source: server release metadata and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

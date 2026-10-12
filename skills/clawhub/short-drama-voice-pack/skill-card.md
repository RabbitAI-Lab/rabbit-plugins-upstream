## Description:

Turns a short-drama episode script into labeled voiceover clips with a consistent voice for each role.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and video editors use this skill to turn an attributed short-drama episode script into ordered, role-labeled dialogue clips with consistent character voices.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authorization grants Beatra a shared device token with broad media-generation and wallet authority.

Mitigation: Review the approval page before granting access; use the uninstall procedure when removing the package so shared credentials are handled safely.

Risk: Automatic updates can replace package files without a separate confirmation.

Mitigation: Disable automatic updates with `python3 scripts/mcp_client.py update --auto off` if you need to review releases before installing them.

## Reference(s):

- [Short-drama voice-pack workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Beatra skill homepage](https://beatra.ai/skills/short-drama-voice-pack)

## Skill Output:

**Output Type(s):** [Audio files, Text]

**Output Format:** [Numbered MP3 clips with a labeled text ledger and result links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Clips follow script order and report role, line, duration, MIME type, resolved model, and charged credits.]

## Skill Version(s):

0.1.7 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

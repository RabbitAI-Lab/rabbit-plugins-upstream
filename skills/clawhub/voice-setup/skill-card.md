## Description:

Voice Setup helps agents build, measure, edit, switch, and validate personal writing voice profiles for the rabbit-writes plugin using writing samples, interview answers, or both.

This skill is ready for commercial/non-commercial use.

## Publisher:

[whit3rabbit](https://clawhub.ai/user/whit3rabbit)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, writers, and agents use this skill to create reusable writing voice profiles, measure samples, maintain style rules, switch active voices, and correct drafts that do not match a saved voice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional Claude Code installation adds persistent hooks that inspect prose writes and can rewrite Git commit or GitHub PR command text.

Mitigation: Install only when persistent integration is desired; run --status and --install --dry-run first, inspect the exact files and hook commands, and prefer project scope where possible.

Risk: Optional --apply-model use can send flagged passages and rules to a configured remote model endpoint.

Mitigation: Avoid --apply-model on sensitive documents unless the user controls and trusts the configured endpoint; there is no default endpoint and endpoint variables should be set deliberately.

## Reference(s):

- [ClawHub voice-setup skill page](https://clawhub.ai/whit3rabbit/skills/voice-setup)
- [Voice reference](artifact/references/voice.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands plus Markdown, JSON, and configuration file outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or update voice profile files, rules JSON, fingerprints, and optional Claude Code host configuration when the user explicitly runs the installer.]

## Skill Version(s):

0.5.0 (source: evidence release and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

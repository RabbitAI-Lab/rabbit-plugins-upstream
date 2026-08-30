## Description:

Turn a short, redacted Session summary into a collaboration-safe Context excerpt. Use before sharing an agent or meeting handoff when the original Session may contain private details that do not belong in the next task.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chengyixu](https://clawhub.ai/user/chengyixu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill before handoffs to convert a short, already redacted Session summary into a compact Context excerpt. The workflow helps identify what to retain, what to redact, freshness limits, sharing authority, safe next steps, and when a person should review the handoff.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may treat the generated Context excerpt as permission to share or act on private material.

Mitigation: Use the output only as a review aid; when sharing authority is missing or unclear, mark the Context as needing review and return it to a person.

Risk: Raw private material could be exposed if users provide full transcripts, credentials, contact details, client data, financial information, or health information.

Mitigation: Provide only a short, redacted Session summary and remove sensitive personal, credential, transcript, client, financial, and health details before using the skill.

Risk: Retained facts may become stale or be mistaken for verified decisions.

Mitigation: Preserve source and freshness notes for retained facts, include invalidators, and return to a person when context conflicts or judgment is required.

## Reference(s):

- [Klik pre-launch direction](https://pre.hiklik.ai/?utm_source=clawhub&utm_medium=companion_skill&utm_campaign=kickstarter_prelaunch&utm_content=session_redaction_check)
- [ClawHub skill page](https://clawhub.ai/chengyixu/skills/klik-session-redaction-check)
- [Publisher profile](https://clawhub.ai/user/chengyixu)

## Skill Output:

**Output Type(s):** [Markdown, Guidance, Analysis]

**Output Format:** [Markdown checklist]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Non-executing review aid; no account access, tool execution, messages, commitments, or authorization.]

## Skill Version(s):

1.0.0 (source: package.json and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

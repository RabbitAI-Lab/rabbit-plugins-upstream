## Description:

Rabbit Writes helps agents audit, edit, or draft prose in a saved human voice, remove machine-writing patterns, and produce findings or rewrites without treating style signals as authorship proof.

This skill is ready for commercial/non-commercial use.

## Publisher:

[whit3rabbit](https://clawhub.ai/user/whit3rabbit)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to scan drafts, clean up machine-like prose, convert text into an active saved voice, or draft new prose while preserving facts and author intent.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill reads drafts selected by the user and can modify files when explicit write modes are used.

Mitigation: Use detect-only mode for review, run write modes only on intended files, and review changed text before publishing.

Risk: The optional apply-model path can send flagged passages to a configured model endpoint.

Mitigation: Keep apply-model local for private drafts or verify the endpoint, model, and API-key handling before use.

Risk: Changing the active voice can affect later drafting or rewrite outputs.

Mitigation: Confirm the active voice before voice-mode work and switch profiles only when that change is intended.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/whit3rabbit/skills/rabbit-writes)
- [Security notes](SECURITY.md)
- [Injection handling](references/injection.md)
- [Voice guidance](references/voice.md)
- [Craft guidance](references/craft.md)
- [Simplified Technical English guidance](references/ste.md)
- [Scanner API](scripts/rwlib/API.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown prose, findings reports, edited text, and optional shell commands.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can modify files only in explicit write modes; optional model endpoint use requires user configuration.]

## Skill Version(s):

0.5.0 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

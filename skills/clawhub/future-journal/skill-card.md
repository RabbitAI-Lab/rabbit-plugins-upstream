## Description:

Future Journal generates an offline, single-file daily journal page for a 49-day guided writing cycle with original prompts, optional encrypted sync, and local quality-check scripts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bonniegeng-max](https://clawhub.ai/user/bonniegeng-max)

### License/Terms of Use:

MIT

## Use Case:

External users and agent operators use this skill to create a fillable or printable future-journal page, get the current day's guided sentence, and maintain the bundled prompt library. It is intended for journaling guidance only and does not provide task management, scheduling, mental-health diagnosis, crisis support, or decisions on the user's behalf.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional sync loads a pinned third-party SDK and sends login email or session data to the backend configured by the user.

Mitigation: Keep sync disabled for fully offline use; before enabling it, verify the configured backend and rely on the documented pinned-version and SRI loading behavior.

Risk: Journal data is stored in browser localStorage by default and can be lost if the browser clears site data or the user changes browsers.

Mitigation: Use the built-in export and import flow for backups before clearing browser data or moving devices.

Risk: The optional sync encryption key is stored locally, and losing the sync password can make the cloud copy unreadable.

Mitigation: Record the sync password separately and keep a local export; the documented behavior states the local record is unaffected if the cloud copy cannot be decrypted.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/bonniegeng-max/skills/future-journal)
- [Future Journal design system](references/DESIGN.md)
- [Skill README](README.md)

## Skill Output:

**Output Type(s):** [Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with HTML, JavaScript, and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces an offline journal HTML file, prompt-selection command output, quality-check results, and optional sync setup guidance.]

## Skill Version(s):

1.0.3 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

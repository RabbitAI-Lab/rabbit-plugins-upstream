## Description:

Finds `ponytail:` shortcut comments in a repository and reports a one-shot technical-debt ledger.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dietrichgebert](https://clawhub.ai/user/dietrichgebert)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to collect marked shortcuts into a technical-debt ledger and identify entries missing a trigger for revisiting them.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A ledger entry without an upgrade trigger may leave a shortcut unaddressed.

Mitigation: Review entries tagged no-trigger and add a concrete condition for revisiting each shortcut.

Risk: Persisting the ledger creates or updates a project file.

Mitigation: Keep reporting read-only unless the user explicitly requests a saved ledger.

## Reference(s):

- [Project homepage listed in skill metadata](https://github.com/DietrichGebert/ponytail)
- [ClawHub skill release](https://clawhub.ai/dietrichgebert/skills/ponytail-debt)

## Skill Output:

**Output Type(s):** [Markdown, Text, Files]

**Output Format:** [File-grouped ledger with source locations, shortcut details, and summary counts; optional Markdown file on request]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Tags markers lacking an upgrade trigger as no-trigger; otherwise reports read-only.]

## Skill Version(s):

4.13.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

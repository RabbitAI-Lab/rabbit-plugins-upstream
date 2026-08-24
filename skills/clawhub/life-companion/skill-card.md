## Description:

A personal AI companion that supports one person over time with destiny charts, daily fortune and journaling, career fit, and relationship reflection grounded in a private on-device profile and journal.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dong845](https://clawhub.ai/user/dong845)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agent operators use this skill as a local-first personal companion for reflective chart readings, journaling, career exploration, and relationship processing. It is intended to keep computation separate from interpretation, preserve user agency, and avoid medical, financial, or legal advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can keep sensitive long-term profile, birth, relationship, mood, and journal data on the user's device.

Mitigation: Keep COMPANION_HOME in a private directory, grant consent only for needed categories, and use the documented forget commands to remove birth data, monthly journal entries, or all companion data.

Risk: The first run may install Python dependencies, which can require network access for package downloads.

Mitigation: Set LIFE_COMPANION_NO_AUTOINSTALL=1 in stricter environments and install dependencies manually before use.

Risk: Reflective destiny, fortune, career, or relationship readings could be misused as predictions or as the basis for high-stakes decisions.

Mitigation: Keep the computation-versus-interpretation boundary visible, avoid medical, financial, and legal advice, verify high-stakes external facts from current sources, and run the skill's selfcheck before sending substantive replies.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dong845/skills/life-companion)
- [Safety rules](artifact/references/safety.md)
- [Onboarding and consent](artifact/references/onboarding.md)
- [Profile and journal schema](artifact/references/profile-schema.md)
- [Destiny module](artifact/references/modules/destiny.md)
- [Daily fortune module](artifact/references/modules/daily-fortune.md)
- [Career module](artifact/references/modules/career.md)
- [Relationships module](artifact/references/modules/relationships.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and plain text with optional JSON or shell command snippets from local helper scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write local profile, journal, consent, state, and cache files under COMPANION_HOME when the user consents.]

## Skill Version(s):

1.0.0 (source: server release metadata and target metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

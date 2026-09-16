## Description:

Life Companion is a local-first personal companion skill that supports one user over time with reflective chart readings, daily journaling, career-fit analysis, and relationship reflection while keeping computation separate from interpretation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dong845](https://clawhub.ai/user/dong845)

### License/Terms of Use:

MIT-0

## Use Case:

External users and assistant operators use this skill to maintain a private, on-device profile and journal, compute supported reflective lenses, and receive grounded guidance for daily check-ins, career fit, chart readings, and relationship reflection. It is intended for personal reflection and productivity support, not medical, financial, legal, hiring, or crisis counseling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill stores sensitive profile, journal, mood, birth, and relationship data locally under COMPANION_HOME.

Mitigation: Use only in an environment where local persistent storage is acceptable; review consent and profile data after setup and use the documented forget flows to remove stored data when needed.

Risk: First-run dependency installation can download packages before the user has reviewed or pinned them.

Mitigation: Set LIFE_COMPANION_NO_AUTOINSTALL=1 and install reviewed, pinned dependencies manually before running the skill.

Risk: The optional localhost onboarding or career form is unauthenticated and can affect sensitive stored profile data while active.

Mitigation: Prefer chat onboarding when practical; if using the form, keep it open only briefly, avoid untrusted webpages during use, close it after submission, and review stored data afterward.

Risk: Reflective readings could be mistaken for predictions or advice in high-stakes areas.

Mitigation: Keep computed facts visibly separate from interpretation, preserve the skill's safety framing, and route medical, financial, legal, hiring, or crisis matters to appropriate real-world support.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dong845/skills/life-companion)
- [README](README.md)
- [Safety, honesty, and privacy](references/safety.md)
- [Profile and journal schemas](references/profile-schema.md)
- [Onboarding](references/onboarding.md)
- [Destiny module](references/modules/destiny.md)
- [Daily fortune module](references/modules/daily-fortune.md)
- [Career module](references/modules/career.md)
- [Relationship module](references/modules/relationships.md)
- [Forms](references/forms.md)
- [Fact-checking](references/factcheck.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown and plain text, with JSON and shell-command output from local helper scripts when computation is required]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses local files under COMPANION_HOME for profile, consent, journal, and module state; optional localhost forms can collect onboarding or career inputs.]

## Skill Version(s):

2.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

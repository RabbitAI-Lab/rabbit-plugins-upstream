## Description:

Provides accurate current time, market hours, timezone conversions, and stale-data prevention for time-sensitive agent responses.

This skill is ready for commercial/non-commercial use.

## Publisher:

[geoffguides](https://clawhub.ai/user/geoffguides)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to answer current-time, timezone-conversion, and market-hours questions while reducing stale or timezone-incorrect responses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Future runtime implementations could store timezone preferences.

Mitigation: Review preference storage behavior if implementation files are added after this release.

Risk: Market-hours answers may be used for time-sensitive decisions.

Mitigation: Verify current time, exchange holidays, and early closes before acting on market-status guidance.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/geoffguides/skills/time-awareness)
- [Artifact README](artifact/README.md)
- [Artifact skill documentation](artifact/SKILL.md)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown or plain text responses with timezone, date, market-hours, and configuration guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [No external API keys are required by the inspected artifact.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

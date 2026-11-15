## Description:

Creates a labeled pack of 8 to 15 original instrumental music beds for short-drama scenes such as tension, romance, comedy, and heartbreak.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Editors and short-form drama production teams use it to plan a set of labeled instrumental cues for an episode or season, covering the moods needed across its scenes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security assessment flags broad shared permissions and persistent credentials that may reach beyond music scoring.

Mitigation: Review the requested access before connecting, keep the credential private, and disconnect when it is no longer needed.

Risk: The security assessment reports that installation and runtime details are sent to the service.

Mitigation: Review the documented data flow before installation and avoid connecting if that reporting is not acceptable.

Risk: The security assessment notes a possible uninstall-state concern.

Mitigation: Follow the documented uninstall and disconnect steps, which check whether other installed skills still use the shared connection.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/beatra-ai/skills/short-drama-score-pack)
- [Beatra skill homepage](https://beatra.ai/skills/short-drama-score-pack)
- [Short-drama score workflow](references/workflow.md)
- [Music editing and audio](references/music-editing-and-audio.md)
- [Updates and security](references/updates-and-security.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [Audio files, Markdown]

**Output Format:** [Instrumental music beds with a labeled Markdown score]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [8 to 15 scene cues; actual durations and file details depend on returned results.]

## Skill Version(s):

0.2.6 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

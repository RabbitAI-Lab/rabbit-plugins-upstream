## Description:

Extracts calendar plans from recent voice and keyboard transcripts, sends individual event cards to HiJavis chat, and adds events to the calendar as pending until confirmed.

This skill is ready for commercial/non-commercial use.

## Publisher:

[samuel-wei](https://clawhub.ai/user/samuel-wei)

### License/Terms of Use:

MIT-0

## Use Case:

HiJavis users use this skill to find meetings and appointments mentioned in recent recordings or typed transcripts, review proposed calendar entries, and receive event cards in chat. It can run on request or after a completed transcript.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Enabling the skill can automatically process recent voice and keyboard transcripts and send event details to chat without approval before each run.

Mitigation: Review the HiJavis privacy, retention, and disable controls before enabling it; avoid capturing conversations you do not want processed.

Risk: Extracted plans may be incorrect or include sensitive details, and pending entries are created before confirmation.

Mitigation: Review each event card and pending calendar entry; correct or discard inaccurate entries before relying on them.

## Reference(s):

- [Calendar Extractor on ClawHub](https://clawhub.ai/samuel-wei/skills/calendar-extractor)
- [HiJavis iPhone app](https://apps.apple.com/us/app/hijavis/id6745134765)

## Skill Output:

**Output Type(s):** [Markdown, Text]

**Output Format:** [Individual markdown event cards and a text reply for on-demand requests]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Extracted entries appear as pending calendar items until confirmed or discarded; chat edits can confirm an entry.]

## Skill Version(s):

0.7.3 (source: ClawHub release metadata, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

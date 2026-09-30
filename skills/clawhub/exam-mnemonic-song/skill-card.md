## Description:

Turns exam facts supplied by a learner or teacher into a labeled mnemonic lyric sheet and, with approval, a generated song for each knowledge point.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Exam candidates, teachers, and coaches use this skill to turn supplied bar-exam, certification, accounting, or other exam facts into memorable lyrics and optional songs, beginning with one knowledge point before creating a set.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Beatra connection uses a shared full-scope device token stored locally.

Mitigation: Review account permissions before approving the connection and keep the token private.

Risk: The bundled client silently installs verified package updates by default.

Mitigation: Review update behavior before installation; disable automatic updates with the documented command if unwanted.

Risk: Music generation consumes credits, and incorrect exam facts could become memorable lyrics.

Mitigation: Confirm the live price and approve each paid batch; check lyrics and audible facts against the supplied study material.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/beatra-ai/skills/exam-mnemonic-song)
- [Beatra skill homepage](https://beatra.ai/skills/exam-mnemonic-song)
- [Exam mnemonic workflow](artifact/references/workflow.md)
- [Installation and authentication](artifact/references/installation-and-auth.md)
- [Automatic updates and safety](artifact/references/automatic-updates-and-safety.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Shell commands]

**Output Format:** [Labeled lyric sheet and Markdown guidance, followed by generated-song links and task details when approved]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Song generation requires explicit approval and Beatra credits; report actual duration and charges from the completed task.]

## Skill Version(s):

0.1.7 (source: server-resolved release, manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

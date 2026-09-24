## Description:

Organizes student class notes into reusable Cornell-style records with cue questions, note content, short summaries, subject/topic indexing, consent-gated retrieval, and limited LearningDNA summary sharing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External students and learning assistants use this skill to transform uploaded or typed class notes into Cornell-style review material, retrieve related notes during study, and produce consent-gated note usage summaries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persistent note archives and cross-skill summaries can contain student learning data.

Mitigation: Confirm the locale and consent model before installation; enable archive, sharing, and reminders only after the relevant consents are set, and share only summary note fields rather than note text.

Risk: The workflow is designed for Chinese K12 Cornell-note use and may not fit unsupported grades or locales.

Mitigation: Confirm the learner's grade band and locale before use, apply the simplified flow for supported younger students, and avoid using the skill where its consent or grade assumptions do not apply.

Risk: Student safety disclosures such as self-harm, abuse, or severe distress are outside the note-taking workflow.

Mitigation: Stop the note workflow and follow the bundled crisis referral protocol, including referral to trusted adults or local emergency resources when appropriate.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-cornell-notes)
- [Cornell format guide](artifact/references/cornell-format-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown and structured text guidance for Cornell-style notes, cue questions, summaries, indexes, and consent-gated handoffs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [No executable output; may maintain a note archive, share only summary note fields with LearningDNA, and queue review reminders when the required consents are present.]

## Skill Version(s):

2.3.0 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

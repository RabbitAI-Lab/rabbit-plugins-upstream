## Description:

Qingtian Psychology Self Study is an agent skill for psychology counselors and counselors-in-training to practice counseling dialogue, transcript supervision, assessment administration, case conceptualization, ethics decisions, and self-study progress tracking.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wangdaozhenren](https://clawhub.ai/user/wangdaozhenren)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill as a local education and training aid for counseling practice. It helps psychology counselors and counselors-in-training rehearse dialogue techniques, review transcripts, run assessment exercises, and track learning progress while preserving clear clinical boundaries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Built-in assessments can miss crisis answers.

Mitigation: Use only as a local training and education aid until crisis metadata is reviewed and fixed for all self-harm, violence, and severe-risk items.

Risk: Assessment reports can overstate clinical care advice.

Mitigation: Review report language before use with real people and make advice scale-specific, especially for FFMQ and other nonclinical trait measures.

Risk: Users may confuse simulated counseling practice with real clinical support.

Mitigation: Keep the skill framed as education and practice; direct real distress, diagnosis, medication, triage, and crisis needs to qualified professionals and crisis resources.

## Reference(s):

- [ClawHub skill release page](https://clawhub.ai/wangdaozhenren/skills/qingtian-psychology-self-study)
- [Publisher profile](https://clawhub.ai/user/wangdaozhenren)
- [Skill README](artifact/README.md)
- [Practice runbook](artifact/practice/RUNBOOK.md)
- [Assessment runbook](artifact/assessment/RUNBOOK.md)
- [Crisis resources](artifact/resources/crisis-resources.md)
- [Assessment safety protocol](artifact/assessment/references/safety_protocol.md)
- [Scale authority notes](artifact/assessment/references/scale_authority.md)
- [Distribution manifest](artifact/manifest/manifest.json)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown, structured text, JSON progress data, HTML assessment reports, and local command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write local progress, backup, migration, flashcard, and assessment report files in the user's workspace.]

## Skill Version(s):

2.1.0 (source: evidence release, SKILL.md frontmatter, manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

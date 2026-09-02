## Description:

Audit corporate text for jargon/evasion and compute bullshit-to-content ratio.

This skill is ready for commercial/non-commercial use.

## Publisher:

[stanestane](https://clawhub.ai/user/stanestane)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external reviewers, communications teams, and agents use this skill to audit emails, memos, job ads, press releases, transcripts, and other corporate copy for jargon, evasion, and missing accountability, then rewrite it in plain language.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may be used on confidential internal communications or recordings, and a separate transcription tool could send audio to an external service.

Mitigation: Review data sensitivity before use, avoid unnecessary confidential material, and use only approved transcription tools for audio or video.

Risk: The skill is intentionally opinionated and blunt, which can be unsuitable for sensitive employee-facing material.

Mitigation: Choose a professional tone for sensitive contexts and critique the language and its effect rather than accusing a writer of bad faith.

Risk: Legitimate technical or business terms can be over-flagged if they are used precisely in context.

Mitigation: Apply the skill's calibration guidance: flag terms only when they hide responsibility, avoid specifics, inflate routine work, or replace concrete details.

## Reference(s):

- [Corporate Bullshit Phrase Reference](artifact/references/corpo-bullshit-phrases.md)
- [The MBA Jargon Exhaustive List](https://bullshitgenerator.blogspot.com/2010/01/mba-jargon-exhaustive-list.html)
- [58 awful corporate jargon phrases you can't escape](https://www.techtarget.com/whatis/feature/Awful-corporate-jargon-phrases-you-cant-escape)
- [Decoding Corporate BS: 27 Phrases That Expose Bad Managers](https://read.thegoodboss.com/p/decoding-corporate-bullsht-27-phrases)
- [Corporate Bullshit Dictionary](https://bsdict.com/dictionary)
- [ClawHub Skill Page](https://clawhub.ai/stanestane/skills/corpo-bullshit-audit)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown audit with verdict, ratio calculations, findings, phrase hits, plain-English rewrite, and questions.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May use transcripts for audio or video; short-text ratios should be treated as directional.]

## Skill Version(s):

1.0.0 (source: ClawHub server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

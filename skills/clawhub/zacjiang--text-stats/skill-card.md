## Description:

Analyze text documents for word count, reading time, readability scores (Flesch-Kincaid, Gunning Fog), keyword density, and sentence statistics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zacjiang](https://clawhub.ai/user/zacjiang)

### License/Terms of Use:


## Use Case:

Developers, writers, and content teams use this skill to inspect text files for counts, reading time, readability estimates, keyword density, and sentence-level statistics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill reads document paths explicitly passed to it, so sensitive files may be processed if selected by the user.

Mitigation: Run the skill only on files intended for local text analysis, and avoid passing confidential documents unless their contents are appropriate to process in the current Codex session.

Risk: English readability scores may be misleading for non-English or multilingual documents.

Mitigation: Treat Flesch-Kincaid, Gunning Fog, and Flesch Reading Ease as English-only estimates and use CJK counts or other language-appropriate review for non-English text.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zacjiang/skills/text-stats)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Plain text terminal reports with command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports word, character, sentence, paragraph, reading-time, readability, keyword-density, and CJK character statistics.]

## Skill Version(s):

1.0.0 (source: SKILL.md frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

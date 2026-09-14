## Description:

ia-writing edits, rewrites, humanizes, proofreads, and audits human-facing prose for natural tone while preserving meaning, factual accuracy, and the writer's voice.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external contributors, developers, and other writers use this skill to improve human-facing prose, including copy, documentation, blog posts, emails, changelogs, and PR descriptions. It can also audit drafts for AI-like patterns without assigning authorship.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Edited prose could accidentally change meaning, remove useful nuance, or alter a writer's voice.

Mitigation: Review the corrected text against the original before publishing, with attention to factual meaning, voice preservation, and proportionality of edits.

Risk: Citation artifacts, URL tracking parameters, or rewritten references could create provenance or link-quality issues.

Mitigation: Mechanically check citation artifacts and AI-referrer URL parameters before publication, and retain accurate citations or delete unsupported claims.

Risk: AI-pattern detection could be mistaken for an authorship judgment.

Mitigation: Use detect mode to report observable writing patterns and fixes only; do not score the draft or claim whether AI wrote it.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/iliaal/skills/compound-eng-writing)
- [SKILL.md](artifact/SKILL.md)
- [SPEC.md](artifact/SPEC.md)
- [Two-Phase Audit Workflow](artifact/references/audit-workflow.md)
- [editing and voice](artifact/references/editing-and-voice.md)
- [Before/After Examples](artifact/references/examples.md)
- [language and patterns](artifact/references/language-and-patterns.md)
- [Extended Phrase Reference](artifact/references/phrases.md)
- [PR and MR Description Style](artifact/references/pr-descriptions.md)
- [publication surfaces](artifact/references/publication-surfaces.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown or plain text, depending on the requested writing surface]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include corrected prose, audit findings, concise changelogs, PR descriptions, or publication-ready text.]

## Skill Version(s):

4.5.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

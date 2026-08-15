## Description:

XReading turns a book title or local PDF/EPUB/text file into a Chinese reading card that triages whether to continue, explains the book's core claim and reasoning chain, extracts actionable rules, checks for major red flags, and updates local reading records.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cutd](https://clawhub.ai/user/cutd)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to process books into concise Chinese reading artifacts: a triage decision, a structured book card, optional verification notes, and local reading-log updates. It is intended for book understanding and practical rule extraction, not general article summarization, literary criticism, or single-fact lookup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Book files and generated reading notes may contain sensitive personal, professional, or investment information.

Mitigation: Review generated files before syncing, publishing, or pushing them to shared storage.

Risk: When only a book title is supplied, the skill may rely on incomplete model knowledge plus web checks and miss edition-specific details.

Mitigation: Prefer local source files when available; otherwise record the content source and note likely omissions in the card.

Risk: A reading-derived rule could be over-applied to real investment decisions.

Mitigation: Keep reading validation separate from investment action; use independent due diligence, valuation, risk budgeting, position sizing, and exit criteria before any trade.

## Reference(s):

- [XReading ClawHub skill page](https://clawhub.ai/cutd/skills/xreading)
- [Card template](references/card-template.md)
- [Project context](references/project-context.md)
- [Quality rules](references/quality-rules.md)
- [Workspace files](references/workspace-files.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Chinese Markdown files, concise Chinese chat summaries, and shell commands for ratio validation]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write a book card, optional verification notes, a book list, and a usage log; uses a ratio-check script to keep content, application, and red-flag sections balanced.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

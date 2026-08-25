## Description:

Humanizer reviews and rewrites prose to remove common AI-writing tells while preserving the source text's facts and genre.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dennisrongo](https://clawhub.ai/user/dennisrongo)

### License/Terms of Use:

MIT

## Use Case:

External users, developers, and writing teams use this skill to review or rewrite drafts, documentation, memos, emails, resumes, and longform prose so they sound less like LLM output without adding new facts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: File mode can edit user-selected prose files in place.

Mitigation: Use file mode only on intended documents and review the resulting changes before relying on them.

Risk: A rewrite can accidentally change meaning or add unsupported detail if the fact-preservation rule is not followed.

Mitigation: Audit rewritten text against the source and remove any fact, name, number, date, quote, or citation that was not present in the input.

## Reference(s):

- [AI-writing patterns](references/patterns.md)
- [Word tiers and cliches](references/word-tiers.md)
- [Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing)

## Skill Output:

**Output Type(s):** [text, markdown, files, guidance]

**Output Format:** [Plain text or Markdown, with in-place prose file edits when File mode is selected]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Preserves source facts and reports short change summaries for file rewrites]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Humanizer reviews or rewrites prose to remove common AI-writing patterns while preserving facts and matching the requested genre.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dennisrongo](https://clawhub.ai/user/dennisrongo)

### License/Terms of Use:

MIT

## Use Case:

Writers, editors, developers, and agents use this skill to review or rewrite drafts, documentation, PR descriptions, emails, resumes, and essays so they sound less like LLM-generated prose without adding unsupported facts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: File mode can modify user-selected prose files in place.

Mitigation: Use version control, review diffs, and limit File mode to intended prose files before accepting changes.

Risk: A rewrite could accidentally change meaning or omit source claims.

Mitigation: Review rewritten text against the original for fact preservation, especially for names, numbers, dates, quotes, and citations.

## Reference(s):

- [AI-writing patterns](references/patterns.md)
- [Word tiers and cliches](references/word-tiers.md)
- [Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing)

## Skill Output:

**Output Type(s):** [text, markdown, guidance, files]

**Output Format:** [Plain text or Markdown, depending on source input and invocation mode]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May rewrite user-selected prose files in place in File mode; preserves code, data, frontmatter, and link targets.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

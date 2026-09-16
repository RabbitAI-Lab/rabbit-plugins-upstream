## Description:

Prose editing, rewriting, and humanizing text for natural tone, plus audit-only detection of AI writing tells for copy, docs, blog posts, emails, and PRs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Writers, developers, and reviewers use this skill to edit human-facing prose while preserving meaning, factual accuracy, and voice. It also supports audit-only review for AI writing tells without claiming authorship.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Edited prose can accidentally change factual meaning, citations, URLs, or PR issue references.

Mitigation: Review the final text against the original source material before using it in docs, releases, emails, or PRs.

Risk: Audit findings identify writing patterns but do not prove whether text was written by AI.

Mitigation: Use detect-mode output as review guidance, not as an authorship verdict.

Risk: The skill can prepare publishable text but does not grant authority to post or publish it.

Mitigation: Confirm the user or deployment workflow has the required approval before publishing any edited content.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/iliaal/skills/compound-eng-writing)
- [ia-writing Specification](SPEC.md)
- [Two-Phase Audit Workflow](references/audit-workflow.md)
- [Editing and Voice](references/editing-and-voice.md)
- [Before/After Examples](references/examples.md)
- [Language and Patterns](references/language-and-patterns.md)
- [Extended Phrase Reference](references/phrases.md)
- [PR and MR Description Style](references/pr-descriptions.md)
- [Publication Surfaces](references/publication-surfaces.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Plain text or Markdown with corrected text, audit findings, and concise changelog notes.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Review outputs before use where factual accuracy, citations, URLs, PR issue references, or posting authority matter.]

## Skill Version(s):

4.5.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

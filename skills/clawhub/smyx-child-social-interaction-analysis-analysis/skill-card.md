## Description:

Analyzes videos of children in group settings to summarize social-interaction frequency, duration, and patterns for educators.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Educators and developers use this skill to review children's interactions in classroom or play-area video, including interaction counts, durations, and report history. Results are educational aids, not developmental or medical diagnoses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Children's video is sent to a remote service for processing.

Mitigation: Use only with explicit guardian and institutional approval for remote processing; confirm retention, access controls, and deletion practices before use.

Risk: The skill silently creates or reuses persistent account identity and tokens, linking report history and exports.

Mitigation: Review the provider's credential handling and controls for account-linked history and exported reports before installation.

Risk: Social-interaction summaries could be mistaken for developmental diagnoses or autism screening.

Mitigation: Treat results as educational observations only; seek qualified clinical evaluation for developmental concerns.

## Reference(s):

- [Skill API documentation](references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured analysis report or JSON, with optional report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can display account-linked report history or save results to a file.]

## Skill Version(s):

1.0.12 (source: server-resolved ClawHub release; bundled skill frontmatter says 1.0.15)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

This skill helps agents draft, revise, condense, format, and review Chinese official documents, workplace materials, and news-style releases.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gongyu0918-debug](https://clawhub.ai/user/gongyu0918-debug)

### License/Terms of Use:

MIT

## Use Case:

Employees and external users use this skill to prepare Chinese official documents, workplace materials, institutional rules, meeting minutes, reports, requests, notices, speeches, news releases, and related review comments. It is intended for drafting, rewriting, condensation, style cleanup, format checks, document-genre checks, and human-facing quality review of supplied materials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may process sensitive official drafts or internal workplace materials.

Mitigation: Use it only in a trusted agent environment and avoid providing confidential drafts unless the surrounding environment is approved for that material.

Risk: Generated or revised official documents may contain unsupported facts, incorrect document-genre choices, or authority mismatches if source material is incomplete.

Mitigation: Review outputs against the user's source materials, organizational templates, required approvals, and applicable office or legal rules before use.

Risk: Optional public-source checks can introduce unverified or time-sensitive information.

Mitigation: Require source, date, and verification notes for external facts, and have a human confirm them before including them in a final document.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/gongyu0918-debug/skills/chinese-official-writing)
- [Writing workflow](references/workflow.md)
- [Document genre routing](references/genre-routing.md)
- [Official style guide](references/official-style.md)
- [Handling elements](references/handling-elements.md)
- [Argument chains](references/argument-chains.md)
- [GB/T 9704 formatting reference](references/format-gbt9704.md)
- [Review checklist](references/review-checklist.md)
- [Final review layers](references/final-review-layers.md)
- [External research and public-source checks](references/external-research.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Plain text or Markdown, with occasional shell commands or configuration guidance when document tooling or local linting is requested.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are based on user-provided draft material; public web checks are limited to explicit or time-sensitive fact checks.]

## Skill Version(s):

1.6.29 (source: frontmatter, ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

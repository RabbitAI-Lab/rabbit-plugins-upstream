## Description:

Reviews UTF-8 text or Markdown against versioned PIPL and data-export rules, producing evidence-linked reports for human review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and compliance reviewers use the skill to check privacy policies and data-processing clauses, create reproducible reports, and optionally gate CI on findings. Treat its results as a starting point for qualified human review, not legal advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reports can contain excerpts from reviewed documents.

Mitigation: Keep reports private; use stdout or a private output folder.

Risk: Rule matches and coverage labels may be mistaken for complete legal or framework conclusions.

Mitigation: Have a qualified person review the findings and coverage limits; do not use custom mapping-only packs for CI decisions until their handling is corrected.

Risk: Some installer and remotely fetched package behavior remains unverified.

Mitigation: Use a verified, pinned release, select the intended installation directory, and back up local skill customizations before reinstalling.

## Reference(s):

- [Coverage and scope](artifact/references/coverage.md)
- [Report format](artifact/references/report-format.md)
- [Rule authoring](artifact/references/rule-authoring.md)
- [Project homepage](https://github.com/YottaMeta/yotta-compliance)
- [ClawHub release](https://clawhub.ai/yottameta/skills/yotta-compliance)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, JSON]

**Output Format:** [Markdown or JSON compliance review report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports include source excerpts, rule identifiers, framework coverage labels, and items for manual review. Results are deterministic apart from generation time.]

## Skill Version(s):

0.1.2 (source: target metadata, SKILL.md frontmatter, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

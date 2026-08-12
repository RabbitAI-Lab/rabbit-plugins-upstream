## Description:

Compare two or more materials on the same topic or event before publication to identify mismatched numbers, product names, fact wording, terminology, source attributions, structural promises, and cross-platform expression drift, then produce a severity-rated diff matrix and unified-wording recommendations without modifying originals.

This skill is ready for commercial/non-commercial use.

## Publisher:

[haiyangchenbj](https://clawhub.ai/user/haiyangchenbj)

### License/Terms of Use:

MIT-0

## Use Case:

Editorial, PR, product, and communications teams use this skill to compare related drafts or localized materials before publication, find consistency drift across key claims, and decide which wording should be unified. It is audit-only and leaves original materials unchanged.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow reads user-provided publication materials that may contain confidential or pre-release information.

Mitigation: Provide only materials appropriate for the runtime environment and avoid placing secrets in the optional product-term environment variable or watchlist file.

Risk: Generated unified wording could be applied incorrectly if reviewers treat recommendations as final edits.

Mitigation: Review generated reports before acting on recommendations and require human confirmation for P0/P1 decisions.

Risk: Unreadable charts, images, or embedded content can leave consistency issues unexamined.

Mitigation: Flag unparseable content and obtain text extraction or manual checks before publication decisions.

## Reference(s):

- [Consistency Checklist Reference](references/consistency-checklist.md)
- [Replay References](references/replay-references.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, JSON, Files, Guidance]

**Output Format:** [Markdown audit report with diff tables and JSON claim or wording files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces local audit artifacts and requires human confirmation for P0/P1 disposition before source materials are changed.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Checks Chinese-language claims against specific sources, dates, and scope, then prepares attributed citation text and an evidence ledger.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xxjrq](https://clawhub.ai/user/xxjrq)

### License/Terms of Use:

MIT-0

## Use Case:

Writers, researchers, and content teams use this skill to check the support and limits for claims in Chinese-language articles, distinguish vendor statements from independent evidence, and produce attributed citations with an evidence ledger.

### Deployment Geography for Use:

Global; focused on Chinese-language sources.

## Known Risks and Mitigations:

Risk: A claim could be overstated beyond the source's subject, date, or scope.

Mitigation: Keep the publisher attribution and applicable dates and limits in the evidence table and citation text; leave unsupported claims pending or omit them.

Risk: Follow-up publishing or signed-in browsing could expose content or publish to unintended destinations.

Mitigation: Before any requested follow-up, review the installation and provider data handling, and confirm the article, destination accounts, and publication visibility.

Risk: Repeated exports replace three named files in the target folder.

Mitigation: Export to a dedicated folder for each run.

## Reference(s):

- [Evidence ledger format](references/evidence-format.md)
- [Source selection guide](references/source-selection.md)
- [aimeGeo content production guide](https://geo.aimmme.com/docs/content-production/)
- [aimeGeo publishing workflow](https://geo.aimmme.com/docs/publish-flow/)

## Skill Output:

**Output Type(s):** [Analysis, Files, Markdown, CSV, JSON]

**Output Format:** [CSV evidence table, attributed Markdown paragraphs, Markdown verification-gap list, and JSON evidence ledger]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs preserve source attribution, dates, scope, and verification limits; scripts export files locally.]

## Skill Version(s):

1.0.2 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

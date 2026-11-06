## Description:

Cite Holmes supports deep research and standalone citation checks by searching scholarly sources, verifying references against registries, and producing research reports and bibliography exports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

External researchers, writers, and developers use Cite Holmes to discover literature, check whether citations resolve and match registry metadata, and prepare research reports or bibliography exports. Citation verification does not establish that a source supports a claim, so review source text and flagged references before relying on a report.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Checking submitted links can reach private services.

Mitigation: Use network isolation before checking untrusted links, and restrict access to the destinations appropriate for the review.

Risk: Citation checks can overstate what they verified.

Mitigation: Independently inspect source text and confirm citation metadata and retraction status before publication or medical use; treat verification as evidence about the reference, not a guarantee that it supports a claim.

Risk: Optional judging can send claims and evidence to configured endpoints, and URL handling for optional API keys needs care.

Mitigation: Use trusted configured endpoints, avoid optional API keys until URL handling is fixed, and pin installation revisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/docsor1212/skills/cite-holmes)
- [Search strategies](artifact/references/search-strategies.md)
- [Verification details](artifact/references/verification-details.md)
- [Security and behavior declaration](artifact/references/security.md)
- [Medical mode guidance](artifact/references/medical-mode.md)
- [Honest limits and out-of-scope uses](artifact/references/out-of-scope.md)
- [Report template](artifact/references/report-template.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown reports, JSON workpapers, Bibliography exports (BibTeX, RIS, CSV, and GB/T 7714 text)]

**Output Format:** [Markdown and structured JSON, with optional bibliography export files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports include per-reference verification verdicts and human-review flags; verification is a point-in-time result.]

## Skill Version(s):

6.2.0 (source: server release evidence, SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

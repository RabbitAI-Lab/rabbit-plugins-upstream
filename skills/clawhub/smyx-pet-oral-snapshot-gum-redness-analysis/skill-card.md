## Description:

Analyzes pet oral snapshot images or videos through the publisher's cloud APIs to report visible gum color, gum redness level, tartar coverage, and oral-care observations without making a veterinary diagnosis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill in pet cameras, smart pet products, and pet health platforms to turn oral images, videos, or URLs into structured oral-health observations. It can also retrieve account-linked historical oral-health reports from the publisher's cloud service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet oral media or network URLs are sent to the publisher's cloud service for analysis.

Mitigation: Use only media you are permitted to share and review the publisher's privacy terms before installation or use.

Risk: The skill can create or reuse local identity state, store service tokens locally, and retrieve account-linked historical reports.

Mitigation: Use separate workspaces or accounts on shared systems and remove local credential or report state when it is no longer needed.

Risk: The output is an oral-health observation and may be incomplete or misleading when the media is unclear or the pet's mouth is not visible.

Mitigation: Treat results as non-diagnostic screening support and consult a veterinarian for diagnosis or treatment decisions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-pet-oral-snapshot-gum-redness-analysis)
- [Pet Oral Snapshot API Documentation](references/api_doc.md)
- [Shared Analysis API Documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, json, guidance]

**Output Format:** [JSON or Markdown-style structured report with optional report export links.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can write report output to a file when requested; history queries return account-linked report lists.]

## Skill Version(s):

1.0.11 (source: release metadata; artifact frontmatter is 1.0.10 and _meta.json is 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

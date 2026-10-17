## Description:

Identifies common crop pests in supplied images or videos and returns pest types, estimated counts, confidence scores, and report links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Farmers, agronomists, and agricultural advisers use crop images or videos to identify possible pest infestations and review current or historical analysis reports. Results are observational and are not pesticide or treatment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Crop images, videos, or supplied URLs are sent to remote LifeEmergence services for analysis.

Mitigation: Use only media and URLs approved for external processing; avoid private farm imagery, signed URLs, and sensitive local files unless the service and retention terms are acceptable.

Risk: The skill silently creates or reuses a local identity and stores service tokens in a workspace data database for report history access.

Mitigation: Review local data retention and access controls before use, and clear stored identity and tokens when no longer needed.

Risk: Pest classifications and counts may be uncertain and could influence treatment decisions.

Mitigation: Confirm consequential findings with an agricultural specialist and follow local plant-protection guidance before treatment.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-crop-pest-identification-analysis)
- [Pest analysis API reference](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, JSON, Markdown]

**Output Format:** [Structured pest analysis reports or Markdown history tables, with optional saved result files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes pest types, estimated counts, confidence scores, and report links; supports basic, standard, and JSON detail settings.]

## Skill Version(s):

1.0.12 (source: server-resolved ClawHub release; supplied artifact frontmatter states 1.0.15)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

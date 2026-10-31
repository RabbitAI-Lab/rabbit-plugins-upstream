## Description:

Analyzes video clips and images to generate a natural language scene summary.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

People reviewing visual media can provide an image or video to receive a scene description and structured analysis report, or request a listing of previous reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may upload media even when using its export-only option.

Mitigation: Verify export-only behavior before use and avoid sending sensitive images or videos until confirmed.

Risk: The skill may automatically register accounts and retain credentials without clear disclosure.

Mitigation: Require explicit account onboarding and protected credential storage, and confirm which account owns report history.

Risk: Authenticated requests and uploaded media involve configured destinations and provider retention practices.

Mitigation: Restrict authenticated request destinations and confirm provider media-retention practices before sharing media.

## Reference(s):

- [API reference](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, Text, Markdown, JSON]

**Output Format:** [Natural-language scene summaries and structured analysis results; report listings can be presented as Markdown tables.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Output detail can be basic, standard, or JSON; results may include report links.]

## Skill Version(s):

1.0.19 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

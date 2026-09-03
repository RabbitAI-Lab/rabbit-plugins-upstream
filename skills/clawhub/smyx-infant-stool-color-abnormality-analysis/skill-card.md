## Description:

Analyzes infant diaper or stool images to classify stool color patterns, flag clay-pale or bloody stool risk, and produce screening-oriented recommendations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External caregivers, pediatric-care workflows, and developers integrating infant-care tooling can use this skill to analyze infant diaper or stool images from local files or URLs for stool color categories, risk level, recommended action, and history reports. It provides screening-oriented guidance and report links, not medical diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive infant diaper or stool images and URLs may be sent to the Life Emergence cloud service.

Mitigation: Use only with explicit guardian consent, avoid unnecessary identifying context, and review the service privacy and retention terms before deployment.

Risk: Reports may be associated with automatically managed local identity records and locally stored tokens.

Mitigation: Review token storage and history retrieval behavior, restrict access to the runtime environment, and clear stored identity data when no longer needed.

Risk: Visual stool color classification can be affected by lighting, filters, image quality, and clinical context.

Mitigation: Capture images under natural white or cool white light without filters, treat outputs as screening prompts rather than diagnoses, and route warning or urgent results to qualified pediatric care.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-infant-stool-color-abnormality-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API interface documentation](references/api_doc.md)
- [SMYX analysis API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, guidance]

**Output Format:** [Markdown-formatted text with structured JSON analysis content and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can write the returned report text to an output file when requested.]

## Skill Version(s):

1.0.8 (source: ClawHub release evidence; artifact frontmatter: 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

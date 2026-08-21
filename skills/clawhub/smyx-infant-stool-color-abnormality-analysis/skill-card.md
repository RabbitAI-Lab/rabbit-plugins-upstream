## Description:

Analyzes infant diaper or stool images to classify stool color, flag clay-pale or bloody patterns, and return structured risk guidance and report links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users, caregivers, pediatric clinics, postpartum care centers, and developers integrating infant-care workflows can use this skill to analyze infant stool images or URLs, classify abnormal colors, and surface next-step guidance. It is a screening aid and does not replace pediatric or clinical evaluation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive infant images or health records may be sent to a remote analysis service.

Mitigation: Use only with explicit guardian consent and in environments approved for those data flows.

Risk: The skill creates or reuses a local identity and stores returned tokens in a workspace database.

Mitigation: Review identity, token storage, and retention behavior before using the skill with real users or regulated records.

Risk: The release currently defaults to dev/private HTTP endpoints.

Mitigation: Deploy only after confirming trusted production endpoints and acceptable network exposure.

Risk: Image-based stool color classification can be wrong under poor lighting, filters, or color casts, and it is not a medical diagnosis.

Mitigation: Ask users to capture images under natural white or cool white light, treat results as screening guidance, and direct urgent or uncertain cases to pediatric clinical evaluation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-infant-stool-color-abnormality-analysis)
- [API documentation](references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown and JSON-like structured text with optional report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can output analysis results to stdout, list cloud history as structured records, or save a result file when an output path is provided.]

## Skill Version(s):

1.0.7 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

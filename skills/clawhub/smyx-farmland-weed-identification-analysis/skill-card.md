## Description:

Identifies weed species and coverage density from field top-view images, and outputs a weed distribution heatmap dataset to support precision weeding decisions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Farmers and agronomists can use this skill to assess weeds in top-view field images or videos, review species and coverage-density estimates, and support precision weeding decisions. Results are for field-management reference and do not provide herbicide recommendations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected field images and videos leave the device for LifeEmergence processing.

Mitigation: Submit only intended media and avoid unrelated or sensitive content in the selected files.

Risk: Account selection and automatic account creation can mix report histories, while credentials are stored locally.

Mitigation: Use reliable per-user account binding and protect locally stored credentials, especially on shared agents.

Risk: The --export-env-only option still permits uploads and history requests and may incur service charges.

Mitigation: Do not treat this option as preventing network activity or charges; review the service behavior before use.

## Reference(s):

- [API interface documentation](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, Structured data, Markdown, Report links]

**Output Format:** [Structured analysis with weed species, coverage-density estimates, distribution heatmap data, and report links; JSON or Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results are estimates for field-management reference; no herbicide recommendations are provided.]

## Skill Version(s):

1.0.15 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

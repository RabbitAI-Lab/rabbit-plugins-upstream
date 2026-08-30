## Description:

Assesses medicinal-herb leaf images or videos to estimate active-ingredient accumulation trends and harvest timing from visual features such as color, chlorophyll-related indices, and leaf thickness.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External growers, herb cooperatives, GAP cultivation bases, and pharmaceutical raw-material teams use this skill to analyze medicinal-plant imagery and receive a trend level, harvest-window guidance, structured results, and report links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Input images, videos, URLs, and history queries may be sent to external LifeEmergence-style cloud services and associated with a local identity.

Mitigation: Review the cloud service, identity, and storage model before installation; avoid sensitive media unless the service is approved for that data.

Risk: The skill can silently create or reuse a local identity and persist account tokens in a workspace SQLite database.

Mitigation: Run it in an isolated workspace, restrict access to the workspace data directory, and clear stored local identity data when the skill is no longer needed.

Risk: The artifact contains pet/video remnants and development endpoint configuration that may confuse behavior or route data unexpectedly.

Mitigation: Review and correct endpoint configuration and obsolete labels before relying on the skill in production workflows.

Risk: The trend estimate is based on visual features and does not provide chemical assay data.

Mitigation: Use the output as harvest-decision support only and confirm formal quality evaluations with HPLC, national standards, pharmacopoeia methods, or other appropriate chemical testing.

## Reference(s):

- [API documentation](references/api_doc.md)
- [Analysis API documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-chinese-herbal-ingredient-trend-analysis)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown report text with structured JSON content and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can save the generated report text to a user-specified output file.]

## Skill Version(s):

1.0.10 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Analyzes images and video for electric motorcycles and e-bikes in restricted areas, then produces violation counts, alerts, and management suggestions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Security and facility teams can review surveillance images or video for electric vehicles in restricted areas, count suspected parking or driving violations, and receive alerts and management suggestions. Treat findings as screening results and have a person confirm violations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected footage is sent to Life Emergence’s cloud service for processing.

Mitigation: Confirm organizational approval before uploading footage, and avoid sensitive footage until the service's controls are reviewed.

Risk: Accounts and tokens may be created and retained automatically, and the export-only option is broken.

Mitigation: Confirm account creation and retention behavior, credential separation, and permitted credential destinations with the provider; do not rely on export-only mode until it is corrected.

## Reference(s):

- [API documentation](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-electric-vehicle-detection-analysis)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown]

**Output Format:** [Structured JSON detection reports and Markdown report lists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports may include vehicle counts, violation levels, warnings, and suggestions; a person should confirm findings.]

## Skill Version(s):

9.9.20 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

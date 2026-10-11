## Description:

Estimates a relative transpiration-rate index and plant water-stress indicators from indoor leaf images or video, with optional environmental measurements.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Plant-care users and greenhouse operators use leaf imagery and optional temperature and humidity readings to assess relative transpiration and possible water stress, and to retrieve past analysis reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote analysis may expose uploaded plant imagery and account-linked report history to lifeemergence.com services.

Mitigation: Use only with trusted services and informed user consent; explain what is uploaded and retained before analysis or history lookup.

Risk: The skill silently creates or reuses an identity and stores account tokens in the workspace.

Mitigation: Require explicit consent for account-linked operations and protect or remove local credentials when no longer needed.

Risk: Pet-health remnants in the plant-analysis workflow could confuse reports or expectations.

Mitigation: Review outputs for plant relevance and remove the unrelated pet-health material before deployment.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-transpiration-rate-estimation-analysis)
- [Bundled API reference](artifact/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Structured text or JSON-formatted analysis; Markdown table for historical reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Relative 0–100% index, plant-care suggestions and report links; optional saved output file. Results are for care guidance, not direct soil-moisture measurement.]

## Skill Version(s):

1.0.13 (source: ClawHub release metadata; bundled SKILL.md declares 1.0.15)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

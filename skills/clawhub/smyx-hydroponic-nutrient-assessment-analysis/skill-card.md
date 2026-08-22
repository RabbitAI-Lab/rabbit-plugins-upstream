## Description:

Assesses hydroponic nutrient concentration qualitatively from root and leaf images or videos, identifying visual stress indicators and returning structured adjustment guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External hydroponic growers, plant factory operators, researchers, and developers use this skill to inspect root and leaf media for signs of nutrient solution imbalance. It supports qualitative care decisions such as dilution, nutrient supplementation, water changes, and follow-up observation without producing EC or ppm measurements.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Plant images, videos, supplied URLs, report history requests, and account-linked metadata may be sent to configured Lifeemergence/API endpoints.

Mitigation: Review the configured API endpoints before use and avoid submitting sensitive local files or private/internal URLs.

Risk: The skill may silently create or reuse an account identity and store tokens locally.

Mitigation: Inspect the workspace data directory for retained user and token records and deploy only where this storage behavior is acceptable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-hydroponic-nutrient-assessment-analysis)
- [API documentation](references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown or JSON structured analysis report with findings, adjustment advice, and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Accepts local image/video paths or public media URLs; history queries return API-derived report lists.]

## Skill Version(s):

1.0.7 (source: server release evidence; artifact frontmatter lists 1.0.12)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

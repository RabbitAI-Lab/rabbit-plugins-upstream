## Description:

Analyzes greenhouse plant images or videos and optional environmental readings to provide prioritized climate-control recommendations and structured reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Greenhouse operators and developers use plant imagery and environmental readings to assess plant stress and review suggested irrigation, shading, ventilation, and heating actions. They can also retrieve historical analysis reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Greenhouse media or supplied URLs are sent to a cloud service for analysis.

Mitigation: Install only if cloud processing of these inputs is acceptable; avoid submitting sensitive media or URLs.

Risk: The skill silently creates or reuses a workspace-local identity and stores service tokens.

Mitigation: Review the local identity store and restrict access to its tokens before installation.

Risk: Incorrect irrigation, shading, fan, wet-curtain or heater recommendations could affect crops or equipment.

Mitigation: Treat recommendations as advisory and require human approval and local safety controls before operating equipment.

## Reference(s):

- [Greenhouse analysis API documentation](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)
- [ClawHub skill release](https://clawhub.ai/smyx-sunjinhui/skills/smyx-greenhouse-climate-plant-feedback-analysis)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Text]

**Output Format:** [Markdown or JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Structured findings, prioritized action suggestions, historical report tables and links; optional saved result file.]

## Skill Version(s):

1.0.13 (source: ClawHub server-resolved release; bundled SKILL.md lists 1.0.16)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

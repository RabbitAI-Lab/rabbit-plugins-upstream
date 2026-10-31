## Description:

Analyzes greenhouse plant images or videos alongside environmental readings and returns structured reports with prioritized climate-control recommendations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Greenhouse operators use the skill to review plant images or videos and optional sensor readings for signs of water, light, or heat stress, then receive prioritized recommendations such as irrigation, shading, ventilation, or heating. It can also retrieve historical analysis reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may silently register an account and retain login tokens locally.

Mitigation: Confirm the service may receive account identity and protect the local token database.

Risk: Media may be uploaded to Lifeemergence even when a no-analysis option is used.

Mitigation: Before running, confirm that Lifeemergence may receive the footage and clarify retention and charges.

Risk: The --export-env-only option does not prevent uploads, and --api-url does not change the destination.

Mitigation: Do not rely on these options to limit data transfer or redirect the service.

Risk: Climate-control recommendations may influence greenhouse equipment operation.

Mitigation: Keep equipment operation behind existing controller safeguards.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-greenhouse-climate-plant-feedback-analysis)
- [Greenhouse analysis API documentation](references/api_doc.md)
- [Usage demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown, Guidance]

**Output Format:** [Structured analysis report with prioritized action recommendations; JSON or Markdown presentation]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Recommendations include action and priority, not specific control values; apply equipment changes through existing controller safeguards.]

## Skill Version(s):

1.0.14 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

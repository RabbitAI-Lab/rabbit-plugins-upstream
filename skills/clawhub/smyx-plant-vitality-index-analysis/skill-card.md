## Description:

Evaluates plant images and optional environmental or growth data to produce a 0–100 vitality score and a rising, stable, or declining trend.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Home gardeners and plant-monitoring operators can use plant images, optionally with environmental readings or growth measurements, to review a vitality score and recent trend. The results are intended as a care reference rather than a substitute for expert assessment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected plant media is sent to Life Emergence, and the export-only option may still upload media.

Mitigation: Avoid the export-only option until its behavior is fixed. Before submitting private footage, confirm what is sent and review the provider’s retention terms and account-deletion process.

Risk: Account credentials remain stored locally, and credential destination safeguards need review.

Mitigation: Wait for fixes to credential destination restrictions; verify where credentials are stored and sent before use.

## Reference(s):

- [Plant Vitality Index API reference](artifact/references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)
- [ClawHub release page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-plant-vitality-index-analysis)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown, Text]

**Output Format:** [Structured JSON report or Markdown summary/table]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes vitality scores and trend indicators; scores can vary with camera angle and lighting, so multi-day comparisons are more informative.]

## Skill Version(s):

1.0.15 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

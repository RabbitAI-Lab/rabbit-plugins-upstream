## Description:

Analyzes plant images and video for early signs of wilting and provides early warnings to support precision irrigation and disease control.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Growers, agronomists, and agricultural teams can submit plant images or video to screen for early wilting, assess possible causes, and support irrigation or disease-control decisions. Treat results as early-warning guidance and check them against field conditions and expert judgment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security summary flags account creation and credential handling beyond the stated monitoring purpose.

Mitigation: Review identity initialization and credential use before installation and execution; use only an approved API credential.

Risk: The security summary notes possible video uploads and incomplete scanner coverage.

Mitigation: Avoid sending sensitive media until the receiving service and retention terms are understood, and review the skill because scan coverage was partial.

Risk: The security summary also flags export-only behavior and weakly scoped triggers and execution controls.

Mitigation: Inspect any generated environment-variable commands and keep execution limited to plant-monitoring tasks.

## Reference(s):

- [ClawHub release](https://clawhub.ai/smyx-sunjinhui/skills/smyx-plant-wilting-monitoring-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [Analysis API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown]

**Output Format:** [Structured analysis report with monitoring results, warnings, recommendations, and report links; JSON content may be presented in Markdown.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Early-warning reference; final plant-health decisions should account for field conditions and expert judgment.]

## Skill Version(s):

1.0.20 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Diagnoses content-commerce metric fluctuations by tracing GMV, conversion, ROI, cost ratio, new-customer, repeat-purchase, and content-efficiency changes to the first abnormal child metric and a testable operating action.

This skill is ready for commercial/non-commercial use.

## Publisher:

[handsomeng](https://clawhub.ai/user/handsomeng)

### License/Terms of Use:

MIT-0

## Use Case:

Ecommerce operators and growth teams use this skill to lock metric definitions, compare baselines, rule out false fluctuations, drill into platform-specific metric trees, and produce a diagnostic card with the first verifiable operating action.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may create a local onboarding marker and write project-local diagnostic notes after a completed diagnosis.

Mitigation: Confirm the active project directory before allowing archive writes, and skip file-writing behavior when the user opts out or the environment cannot write safely.

Risk: The onboarding text includes optional external WeChat support contacts.

Mitigation: Treat those contacts as optional support channels and avoid sharing private business data off-platform unless the user independently trusts that channel.

Risk: Incomplete platform, account, metric, time-window, or baseline data can lead only to preliminary diagnostic hypotheses.

Mitigation: Label such outputs as preliminary, request the minimum missing fields, and avoid presenting a root cause or operating action as confirmed until comparable evidence is available.

## Reference(s):

- [内容电商指标树与公式](references/metric-trees.md)
- [子指标与运营动作映射](references/action-map.md)
- [ClawHub skill page](https://clawhub.ai/handsomeng/skills/ljh-zhibiao)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown diagnostic questions, preliminary judgments, diagnostic cards, and operating-action recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose project-local diagnostic notes only after a completed diagnosis and according to the skill's archive protocol.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

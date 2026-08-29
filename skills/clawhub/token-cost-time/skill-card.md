## Description:

Estimate LLM task token usage, cost, and duration using rule-based classification and optional local profile data without external dependencies.

This skill is ready for commercial/non-commercial use.

## Publisher:

[highnoonoffice](https://clawhub.ai/user/highnoonoffice)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to estimate token usage, cost, duration, and model tradeoffs for planned LLM tasks, with optional local profile data to calibrate future estimates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Recorded executions may be stored locally under ~/.token-cost-time and can include sensitive objectives or execution details.

Mitigation: Avoid recording sensitive objectives or execution details unless local storage of that information is acceptable.

Risk: Rule-based cost, token, and duration estimates can be inaccurate for tasks or models that differ from the available priors and profile data.

Mitigation: Treat estimates as planning guidance and calibrate them with recorded runs before relying on them for budgeting or scheduling decisions.

## Reference(s):

- [Project homepage](https://github.com/highnoonoffice/hno-skills)
- [ClawHub listing](https://clawhub.ai/highnoonoffice/skills/token-cost-time)

## Skill Output:

**Output Type(s):** [text, guidance, shell commands, configuration]

**Output Format:** [Markdown or plain text with command examples and estimate details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May refer to optional local profile and execution-log files under ~/.token-cost-time.]

## Skill Version(s):

0.1.4 (source: server release metadata; artifact frontmatter reports 0.1.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

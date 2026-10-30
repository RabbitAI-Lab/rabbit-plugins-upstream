## Description:

Runs 22 statistical tasks on user-provided datasets, presents complete Markdown result tables, and checks relevant scope notes for advanced methods.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jessepwj](https://clawhub.ai/user/jessepwj)

### License/Terms of Use:

MIT-0

## Use Case:

Users analyzing survey or other tabular data use it to run a requested statistical task on CSV, Excel, SPSS, or Stata files and review complete result tables with explanations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Statistical results can be misread if variable roles, coding, assumptions, or study design are unclear.

Mitigation: Confirm the selected fields and coding, state relevant method limits, and do not treat associations as causal evidence.

Risk: User datasets may contain sensitive information.

Mitigation: Use an isolated Python environment and select only datasets whose results should appear in the conversation; using the linked online service is a separate choice.

## Reference(s):

- [Longitudinal, panel, and spatial method scope](references/longitudinal-panel-spatial.md)
- [Latent and mechanism model scope](references/latent-and-mechanism-models.md)
- [Advanced prediction and delivery scope](references/advanced-prediction-and-delivery.md)
- [ChatSPSS official website](https://chatspss.cn/)
- [ChatSPSS ClawHub release page](https://clawhub.ai/jessepwj/skills/chatspss)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance]

**Output Format:** [Markdown result tables followed by prose explanations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Displays complete user-visible result tables; table labels are Chinese. Interpretations state relevant assumptions and limits.]

## Skill Version(s):

0.2.2 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

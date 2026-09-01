## Description:

Using fixed cameras in a smart greenhouse to analyze plant morphology in real time, combined with environmental sensors, an AI decision model outputs climate control commands including irrigation, shade-net opening, fan/wet-curtain on-off, and heater on-off.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, greenhouse operators, and agricultural automation teams use this skill to analyze greenhouse plant images or videos with optional environmental sensor context and produce structured climate-control recommendations. It can also retrieve cloud-hosted historical greenhouse control reports for the current internally resolved user.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends greenhouse media, URLs, identity context, and report queries to configured remote endpoints.

Mitigation: Review endpoint configuration and data-handling expectations before installation, and use only approved backends for production greenhouse data.

Risk: The skill can create or reuse local account state and store tokens for cloud report history.

Mitigation: Run it in an environment where local state and credentials are acceptable, and review stored identity or token data according to the operator's access-control policy.

Risk: Returned irrigation, fan, shade, wet-curtain, and heater recommendations could affect physical greenhouse equipment if automated directly.

Mitigation: Require human approval, controller-side bounds checks, and fail-safes before using recommendations to actuate equipment.

## Reference(s):

- [Greenhouse climate plant feedback API documentation](artifact/references/api_doc.md)
- [Shared analysis API documentation](artifact/skills/smyx_analysis/references/api_doc.md)
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-greenhouse-climate-plant-feedback-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown text with structured JSON analysis content, command recommendations, report links, and history lists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs action recommendations and priorities only; the artifact states that concrete PID values or actuator opening percentages should not be produced.]

## Skill Version(s):

1.0.9 (source: server release metadata; artifact frontmatter lists 1.0.10)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

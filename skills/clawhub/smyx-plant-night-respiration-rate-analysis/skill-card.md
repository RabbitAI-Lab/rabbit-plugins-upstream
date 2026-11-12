## Description:

In a plant factory, a fixed thermal imaging camera continuously captures thermal images of the plant canopy leaves at night (no-light period), analyzes leaf temperature trends (respiration releases heat, causing leaf temperature to be slightly higher than air temperature), and combined with optional ambient CO₂ sensor data (respiration releases CO₂ raising concentration), an AI model estimates the relative respiration. | 通过植物工厂内的固定热成像摄像头，在夜间（无光照时段）连续采集植物冠层叶片的热图像，分析叶片温度变化趋势（呼吸作用释放热量导致叶片温度略高于气温），结合可选的环境CO₂传感器数据（呼吸作用释放CO₂浓度升高），利用AI模型估算整株或群体的呼吸强度相对值（0-100%）。

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Plant-factory operators, growers, and agricultural researchers can use the skill to estimate relative nighttime respiration from canopy thermal images and optional CO₂ measurements, then review the resulting activity level and environmental guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review flags unexplained identity and token handling, external media transfer, and payment-related behavior that does not clearly match the plant-analysis purpose.

Mitigation: Avoid installation or sharing sensitive images and account data until the publisher explains these behaviors and their connection to plant analysis.

Risk: Security evidence is incomplete because one referenced local path was missing; the completed scan reporting no findings does not establish that the skill is safe.

Mitigation: Treat the assessment as incomplete and request clarification from the publisher before relying on the skill.

## Reference(s):

- [Plant Night Respiration Analysis API notes](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-plant-night-respiration-rate-analysis)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown, Report links]

**Output Format:** [Structured JSON analysis results and Markdown report listings with links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Estimates a relative respiration index from thermal image or video input, with optional CO₂ context; results are for research and care reference and do not replace measurement with professional agricultural instruments.]

## Skill Version(s):

1.0.13 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

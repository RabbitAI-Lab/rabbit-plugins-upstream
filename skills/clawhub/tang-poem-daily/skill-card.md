## Description: <br>
每日唐诗推送每天从内置唐诗数据集中选择一首诗，生成包含诗文、深度赏析和作者介绍的飞书推送内容。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cantoneyes](https://clawhub.ai/user/cantoneyes) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and teams use this skill to schedule a daily Tang poem selection and generate a structured Chinese literary appreciation message for Feishu. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Daily scheduled delivery can send generated poem content to the configured Feishu channel. <br>
Mitigation: Confirm the schedule, destination channel, and generated message behavior before deployment. <br>
Risk: Generated literary appreciation may contain interpretive or factual inaccuracies. <br>
Mitigation: Review generated analysis for accuracy and tone before sharing it with an audience. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/cantoneyes/skills/tang-poem-daily) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, Shell commands, Guidance] <br>
**Output Format:** [Plain text Feishu message with JSON poem-selection input] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses the current date as the deterministic daily selection seed for the scheduled post.] <br>

## Skill Version(s): <br>
1.0.0 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

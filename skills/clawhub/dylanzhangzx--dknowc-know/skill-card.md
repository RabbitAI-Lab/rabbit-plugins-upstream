## Description: <br>
深知晓，为工作场景提供可信安全、精准无幻觉的咨询导办的知识服务，涉及税务社保、法规政策、行业标准；以及申办各类证照、补贴、资质；还有买房购车、养老育儿、上学就业等各种公共服务。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dylanzhangzx](https://clawhub.ai/user/dylanzhangzx) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to answer Chinese government-service, policy, tax, social security, compliance, subsidy, and public-service questions with source-traceable responses. It can also collect trusted source materials and support complex research, comparison, and drafting workflows when evidence from the remote service is available. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts and questions may be sent to dknowc's remote knowledge service. <br>
Mitigation: Use the skill only for questions appropriate for that provider, and avoid sending sensitive information unless the user accepts the provider exposure. <br>
Risk: Registration uses the user's phone number and SMS verification code. <br>
Mitigation: Run registration only after explicit user consent, and pause for the user-provided verification code instead of inventing or storing it elsewhere. <br>
Risk: API keys are stored locally in config.ini and may be reused from related dknowc skills with consent. <br>
Mitigation: Keep config.ini out of public packages, do not display full keys, and approve key reuse only for trusted same-family skills. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/dylanzhangzx/skills/dknowc-know) <br>
- [DKnowC platform](https://platform.dknowc.cn) <br>
- [DKnowC open service](https://open.dknowc.cn) <br>
- [Trusted unification API endpoint](https://open.dknowc.cn/chat/trusted/unification) <br>
- [Trusted search API endpoint](https://open.dknowc.cn/dependable/search) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Human-readable text or Markdown, with optional JSON output from script modes.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Responses may include trusted source report links or knowledge-base links; first use requires local API key configuration.] <br>

## Skill Version(s): <br>
1.3.0 (source: release evidence, _meta.json, and CHANGE_log.md released 2026-07-28) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

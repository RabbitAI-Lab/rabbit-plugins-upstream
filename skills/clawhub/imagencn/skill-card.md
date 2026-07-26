## Description: <br>
Multi-platform AI image generation via DashScope/Ark/Hunyuan/Zhipu/StepFun, specializing in Chinese text rendering and photorealistic images. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[agents365-ai](https://clawhub.ai/user/agents365-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users use imagenCN to refine image prompts, choose Chinese-oriented image generation or editing models, run provider API calls, and save generated image files. <br>

### Deployment Geography for Use: <br>
Global; DashScope defaults to a China-region endpoint unless the operator selects another supported endpoint. <br>

## Known Risks and Mitigations: <br>
Risk: Prompts and any supplied input images are sent to the selected third-party image provider. <br>
Mitigation: Do not include secrets or sensitive private content in prompts or input images, and review the selected provider API key and endpoint before generation. <br>
Risk: The skill writes generated image files to local paths chosen by the operator or by its automatic naming logic. <br>
Mitigation: Use an explicit output path in an appropriate workspace and review generated files before sharing or relying on them. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/agents365-ai/skills/imagencn) <br>
- [Alibaba Cloud Bailian console](https://bailian.console.aliyun.com/) <br>
- [Volcano Ark API keys](https://console.volcengine.com/ark/region:ark+cn-beijing/apikey) <br>
- [Tencent Hunyuan TokenHub API keys](https://console.cloud.tencent.com/tokenhub/apikey) <br>
- [Zhipu BigModel](https://bigmodel.cn) <br>
- [StepFun API keys](https://platform.stepfun.com/interface-key) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, Files] <br>
**Output Format:** [Markdown guidance with Python command lines; the CLI can emit JSON status and save generated image files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs depend on selected provider, model, prompt, size, optional input image, and local output path.] <br>

## Skill Version(s): <br>
1.7.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

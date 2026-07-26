## Description: <br>
Analyzes local or remote video with Alibaba Cloud Qwen multimodal models, using configurable prompts and frame sampling to produce scene descriptions, object and action analysis, summaries, content review, and Q&A-style answers. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, content teams, media asset managers, educators, and operations reviewers use this skill to inspect videos, summarize scenes, identify objects or actions, and ask targeted questions about local files or public video URLs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Video content and prompts may be sent to Alibaba Cloud DashScope/Qwen, including sensitive or regulated footage. <br>
Mitigation: Use only videos and prompts approved for that provider, and avoid private or regulated footage unless organizational policy allows it. <br>
Risk: DashScope API keys can be exposed if commands print configuration files or secrets to terminal output or chat logs. <br>
Mitigation: Read keys only from the configured local file, avoid commands that echo or grep secrets, and redact any accidental secret output. <br>
Risk: The skill uses shell execution to drive analysis workflows. <br>
Mitigation: Review proposed commands before execution and run only commands needed for the requested video analysis. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/analyze-video-by-qwen) <br>
- [Skill homepage](https://skillhub.cn) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include Qwen video analysis results, execution notes, configuration guidance, and structured JSON-style examples.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

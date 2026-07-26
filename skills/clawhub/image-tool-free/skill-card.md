## Description: <br>
图像处理基础版 helps an agent inspect, convert, crop, resize, compress, and manage metadata for image files in lightweight personal workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to guide common image processing work such as Web image optimization, screenshot cleanup, format conversion, compression, and EXIF or ICC metadata handling. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill combines local privacy claims with unclear external API or network behavior. <br>
Mitigation: Use it on non-sensitive images or local-only workflows until the publisher documents which features contact external services and what data is transmitted. <br>
Risk: The artifact asks agents to use command execution and file writing for image operations. <br>
Mitigation: Review proposed commands before execution and run them on copied input files in a controlled working directory. <br>
Risk: API keys or callback URLs could expose credentials or image-processing results if used without clear data-flow documentation. <br>
Mitigation: Do not provide API keys or callback URLs unless the publisher documents the receiving service, purpose, and transmitted data. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/image-tool-free) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/thcjp) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown, JSON examples, and inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce image-processing command suggestions and structured status-style responses for review before execution.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

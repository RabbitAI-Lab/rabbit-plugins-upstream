## Description: <br>
Generate images with Seedream4.5 and videos with Kling via the LiblibAI API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xtaq](https://clawhub.ai/user/xtaq) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and content creators use this skill to submit image, text-to-video, and image-to-video generation jobs to LiblibAI and poll for result URLs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts and media URLs are sent to LiblibAI. <br>
Mitigation: Avoid submitting confidential prompts, private image URLs, or sensitive media unless you are comfortable sharing that content under LiblibAI data-handling terms. <br>
Risk: The skill uses LiblibAI API credentials to submit generation and status requests. <br>
Mitigation: Provide credentials through environment variables and avoid exposing them in prompts, shared logs, or generated examples. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/xtaq/skills/liblib-ai-gen) <br>
- [LiblibAI API endpoint](https://openapi.liblibai.cloud) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, JSON, guidance] <br>
**Output Format:** [Markdown guidance with bash examples and JSON CLI output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires LIB_ACCESS_KEY and LIB_SECRET_KEY; prompts and media URLs are sent to LiblibAI.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

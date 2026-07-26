## Description: <br>
Use when generating video clips with Chinese video models across text-to-video, image-to-video, first/last-frame, and reference-to-video workflows on Bailian, Jimeng, MiniMax, and Hunyuan. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[agents365-ai](https://clawhub.ai/user/agents365-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to plan, configure, and run short Chinese video generation jobs from prompts or selected image inputs. It helps choose a provider and model, preview requests with dry-run output, submit asynchronous jobs, poll completion, and report the downloaded MP4 path. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts and selected images may be sent to third-party video APIs. <br>
Mitigation: Use dry-run to preview requests, avoid private or sensitive media unless provider terms are acceptable, and provide only files intended for generation. <br>
Risk: Generated results are downloaded from provider-hosted URLs after asynchronous processing. <br>
Mitigation: Review the output file path and generated media before reuse or publication. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/agents365-ai/skills/videogencn) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, JSON, files] <br>
**Output Format:** [Markdown guidance and shell commands; JSON envelopes for CLI introspection or non-TTY output; downloaded MP4 files for successful generations.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses provider API keys from environment variables, supports dry-run previews, and may submit prompts or selected media to third-party video APIs.] <br>

## Skill Version(s): <br>
2.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

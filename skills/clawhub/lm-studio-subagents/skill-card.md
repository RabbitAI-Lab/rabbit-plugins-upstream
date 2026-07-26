## Description: <br>
Reduces token usage from paid providers by offloading suitable work to local LM Studio models for summarization, extraction, classification, rewriting, first-pass review, brainstorming, and privacy-sensitive processing. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[t-sinclair2500](https://clawhub.ai/user/t-sinclair2500) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agent users use this skill to discover local LM Studio models, select an appropriate model, and offload suitable tasks to local inference when quality is sufficient. It is useful for reducing paid API usage and keeping selected work on a trusted local LM Studio server. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive prompts, responses, or conversation identifiers may be retained locally when optional logging or stateful mode is enabled. <br>
Mitigation: Use a trusted local LM Studio endpoint, avoid --log and --stateful for sensitive work unless retention is acceptable, and review any retained local files. <br>
Risk: Broad task-offloading triggers could route sensitive documents or code to an untrusted LM Studio endpoint if the API URL is changed. <br>
Mitigation: Confirm LM_STUDIO_API_URL or --api-url points to localhost or another trusted endpoint before processing sensitive material. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/t-sinclair2500/skills/lm-studio-subagents) <br>
- [LM Studio](https://lmstudio.ai) <br>
- [OpenClaw Documentation](https://docs.openclaw.ai) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON responses from helper scripts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include local LM Studio response content, model_instance_id, response_id, and token usage statistics when helper scripts are used.] <br>

## Skill Version(s): <br>
1.0.3 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

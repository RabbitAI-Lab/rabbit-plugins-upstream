## Description: <br>
Generate images with GPT Image 2 inside Claude Code through the local Codex CLI, using the user's existing ChatGPT Plus or Pro subscription for text-to-image, image editing, style transfer, and multi-reference composition. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[permew](https://clawhub.ai/user/permew) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill to route explicit GPT Image 2 requests through their local Codex CLI session and produce image files from text prompts or reference images. It is intended for users who already have Codex installed, are logged in, and have a ChatGPT plan with image-generation entitlement. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill invokes the local Codex CLI under the user's logged-in ChatGPT account. <br>
Mitigation: Install and run it only where use of the user's ChatGPT subscription and image-generation entitlement is acceptable. <br>
Risk: The helper reads newly created Codex session rollout files to recover generated image data. <br>
Mitigation: Review the skill before deployment and avoid sharing session files or logs outside the local environment. <br>
Risk: The decoded image is written to the caller-provided output path. <br>
Mitigation: Choose output paths deliberately and keep generated files in project-controlled directories. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/permew/skills/gpt-image-2) <br>
- [Publisher profile](https://clawhub.ai/user/permew) <br>
- [Agentspace](https://agentspace.so) <br>
- [Skill repository path](https://github.com/agentspace-so/skills/tree/main/gpt-image-2) <br>
- [OpenAI Codex CLI](https://github.com/openai/codex) <br>
- [RunComfy GPT Image 2 text-to-image](https://www.runcomfy.com/models/openai/gpt-image-2/text-to-image) <br>
- [RunComfy GPT Image 2 image edit](https://www.runcomfy.com/models/openai/gpt-image-2/edit) <br>


## Skill Output: <br>
**Output Type(s):** [Files, Shell commands, Guidance] <br>
**Output Format:** [Image file path and generated PNG, JPEG, or WebP file; Markdown guidance for invocation and failures] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires local codex and python3 binaries plus access to ~/.codex/sessions; writes the decoded image to the requested output path.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

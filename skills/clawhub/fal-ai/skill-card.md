## Description: <br>
Generate images, videos, and audio via fal.ai API (FLUX, SDXL, Whisper, etc.). <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[agmmnn](https://clawhub.ai/user/agmmnn) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill to submit fal.ai media generation and transcription jobs, poll for completion, and return generated media URLs or transcript results. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts, uploaded media URLs, and generation or transcription requests are sent to fal.ai. <br>
Mitigation: Avoid submitting secrets, confidential media, private customer data, or regulated personal data unless your policies allow use of fal.ai for that content. <br>
Risk: The skill requires a fal.ai API key for external API requests. <br>
Mitigation: Store FAL_KEY in the environment or approved configuration and avoid placing credentials in prompts, shared files, generated output, or logs. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/agmmnn/skills/fal-ai) <br>
- [fal.ai API Key Dashboard](https://fal.ai/dashboard/keys) <br>
- [fal.ai Queue API](https://queue.fal.run) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, code, configuration, guidance] <br>
**Output Format:** [Markdown, terminal text, and returned media URLs or transcription text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires FAL_KEY and sends generation or transcription requests to fal.ai.] <br>

## Skill Version(s): <br>
0.1.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

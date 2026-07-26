## Description: <br>
Search, explore, and run fal.ai generative AI models (image generation, video, audio, 3D). Use when user wants to generate images, videos, or other media with AI models. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[apekshik](https://clawhub.ai/user/apekshik) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, creators, and external users use this skill to find fal.ai models, inspect model schemas, submit generation jobs, check status, retrieve results, and upload selected media for model inputs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires access to a fal.ai API key. <br>
Mitigation: Install and use it only when the agent is allowed to access FAL_KEY, and avoid exposing the key in prompts, logs, or shared shell history. <br>
Risk: Prompts and selected media may be sent to fal.ai, and uploaded media can be used as model inputs. <br>
Mitigation: Review prompts and file paths before running or uploading, and avoid sensitive media unless fal.ai handling and retention policies are acceptable for the use case. <br>
Risk: Running fal.ai models can consume fal account credits. <br>
Mitigation: Confirm model choice and generation parameters before submitting jobs, especially for video, training, or multi-output requests. <br>
Risk: Generated outputs are saved locally under ~/.fal/sessions. <br>
Mitigation: Review generated files before sharing them and clean up session folders when outputs should not remain on disk. <br>


## Reference(s): <br>
- [fal.ai Models](https://fal.ai/models) <br>
- [fal.ai Docs](https://docs.fal.ai) <br>
- [Popular fal.ai Models Quick Reference](models-reference.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/apekshik/skills/fal) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, API Calls, Files, Configuration instructions, Guidance] <br>
**Output Format:** [Markdown guidance with bash commands and JSON API payloads] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Generated media may be downloaded to ~/.fal/sessions/${CLAUDE_SESSION_ID}/ when commands are executed.] <br>

## Skill Version(s): <br>
1.0.1 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

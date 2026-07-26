## Description: <br>
Use when someone wants light instrumental background music, such as an ambient bed under dialogue or underscore for reels and explainers. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[pruna-ai](https://clawhub.ai/user/pruna-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers and content-production agents use this skill to prepare prompts, environment setup, and Replicate API calls for generating understated instrumental background music. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Replicate API use may consume paid or quota-limited generation capacity. <br>
Mitigation: Confirm the prompt, duration, steps, and cfg_scale before making prediction requests. <br>
Risk: API tokens can be exposed if pasted into shared prompts, logs, or generated text. <br>
Mitigation: Keep REPLICATE_API_TOKEN in the environment and avoid writing token values into shared text. <br>
Risk: Generated music can interfere with dialogue or include unwanted vocal elements if the prompt is underspecified. <br>
Mitigation: Lead prompts with instrumental and no vocals, and keep mix volume around the documented background-bed range. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/pruna-ai/skills/stable-audio-2-5) <br>
- [Replicate Stable Audio 2.5 predictions endpoint](https://api.replicate.com/v1/models/stability-ai/stable-audio-2.5/predictions) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, API calls] <br>
**Output Format:** [Markdown with curl examples and environment-variable setup guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires REPLICATE_API_TOKEN for Replicate requests and ffmpeg/ffprobe for mix steps; generated audio is downloaded from the Replicate prediction output.] <br>

## Skill Version(s): <br>
1.0.7 (source: server release evidence and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

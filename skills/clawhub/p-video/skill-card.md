## Description: <br>
Use when someone wants one short video clip from text or images, including B-roll, start/end frame animation, or a quick motion shot. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[pruna-ai](https://clawhub.ai/user/pruna-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use p-video to generate one short video clip from a prompt, image anchors, frame pair, or uploaded audio through Pruna's API. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts, uploaded images, and uploaded audio can be sent to Pruna using PRUNA_API_KEY. <br>
Mitigation: Use only prompts and media that are acceptable to upload to Pruna, and confirm credential handling before making API calls. <br>
Risk: Optional related-skill installs can add broader Pruna suite behavior than this single-clip helper requires. <br>
Mitigation: Install only the related Pruna skills needed for the requested video workflow. <br>
Risk: A generation request can spend API resources on a prompt or mode the user did not intend. <br>
Mitigation: Show and confirm the drafted prompt, mode, duration, resolution, fps, and draft setting before submitting the prediction. <br>


## Reference(s): <br>
- [ClawHub skill page for p-video](https://clawhub.ai/pruna-ai/skills/p-video) <br>
- [Pruna file upload API endpoint](https://api.pruna.ai/v1/files) <br>
- [Pruna predictions API endpoint](https://api.pruna.ai/v1/predictions) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration] <br>
**Output Format:** [Markdown with curl examples and JSON request bodies] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces one p-video prediction per invocation; audio-conditioned clips are capped at 20 seconds.] <br>

## Skill Version(s): <br>
1.0.9 (source: server release metadata and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

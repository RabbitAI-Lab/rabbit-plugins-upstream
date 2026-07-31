## Description: <br>
Use when someone wants one short video clip from text or images — B-roll, start/end frame animation, or a quick motion shot. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[pruna-ai](https://clawhub.ai/user/pruna-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and creative operators use this skill to prepare and submit a single Pruna p-video generation request for short text-to-video, image-to-video, frame-pair, or audio-conditioned clips. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated-video requests may upload prompts, images, and audio to Pruna using PRUNA_API_KEY. <br>
Mitigation: Review user inputs before submission and avoid sending sensitive or unauthorized media. <br>
Risk: Optional fields such as disable_safety_filter can affect provider and policy safeguards. <br>
Mitigation: Leave safety-related options at their defaults unless the user has reviewed and accepted the policy implications. <br>
Risk: The workflow depends on referenced helper skills for prompt diversity, video prompting, audio prompting, and Pruna API handling. <br>
Mitigation: Review the referenced helper skills before installation or use in the same agent environment. <br>


## Reference(s): <br>
- [ClawHub p-video skill page](https://clawhub.ai/pruna-ai/skills/p-video) <br>
- [Pruna files API endpoint](https://api.pruna.ai/v1/files) <br>
- [Pruna predictions API endpoint](https://api.pruna.ai/v1/predictions) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, API calls, Configuration] <br>
**Output Format:** [Markdown with inline bash and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires PRUNA_API_KEY and guides one async p-video prediction per invocation.] <br>

## Skill Version(s): <br>
1.0.8 (source: release evidence and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

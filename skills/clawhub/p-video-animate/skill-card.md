## Description: <br>
Guides an agent through using Pruna's p-video-animate API to animate a reference image with motion from a source video. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[pruna-ai](https://clawhub.ai/user/pruna-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and creative operators use this skill to prepare prompts, upload source media, and call Pruna's API for motion-transfer video generation from one image and one motion-template video. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Using the skill sends selected images and videos to Pruna's API with the user's PRUNA_API_KEY. <br>
Mitigation: Use only media the user is allowed to upload and confirm credentials before making API calls. <br>
Risk: Generated prompts or optional fields can change outputs or trigger paid API calls. <br>
Mitigation: Review generated prompts and key parameters before submission, especially when the instruction prompt is not already locked. <br>
Risk: The artifact exposes an optional disable_safety_checker field. <br>
Mitigation: Be cautious with safety-check settings and keep default protections enabled unless the user has a justified need. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with inline curl examples and parameter notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a PRUNA_API_KEY and user-provided image and video URLs or uploaded Pruna file URLs.] <br>

## Skill Version(s): <br>
1.0.7 (source: server release metadata and artifact metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

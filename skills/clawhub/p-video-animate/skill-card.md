## Description: <br>
Use when someone wants a photo to move like another video - motion transfer, dance remixes, or performance variations from a template clip. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[pruna-ai](https://clawhub.ai/user/pruna-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, creators, and developers use this skill to animate a still image with motion from a reference video through Pruna's p-video-animate model. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uploads selected images, videos, and possibly audio to Pruna for generation. <br>
Mitigation: Use only media the user is comfortable sending to Pruna and disclose the upload before making API calls. <br>
Risk: Generated motion-transfer videos can involve likenesses, copyrighted source media, or audio the user may not have rights to use. <br>
Mitigation: Confirm the user has rights to the provided media and likenesses before generation. <br>
Risk: The workflow uses a paid Pruna API key and supports async or quick-test prediction calls. <br>
Mitigation: Confirm PRUNA_API_KEY availability and required inputs before the first POST, and prefer the async path for normal use. <br>
Risk: The optional disable_safety_checker field can alter safety behavior. <br>
Mitigation: Use disable_safety_checker only when deliberately requested and appropriate for the user's content policy context. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/pruna-ai/skills/p-video-animate) <br>
- [Pruna file upload API endpoint](https://api.pruna.ai/v1/files) <br>
- [Pruna predictions API endpoint](https://api.pruna.ai/v1/predictions) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, API Calls, Configuration] <br>
**Output Format:** [Markdown guidance with curl examples and JSON request bodies] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces instructions for uploading media, creating a Pruna prediction, polling, and downloading generated video.] <br>

## Skill Version(s): <br>
1.0.8 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

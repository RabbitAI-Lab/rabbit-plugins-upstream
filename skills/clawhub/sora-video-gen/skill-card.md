## Description: <br>
Generate videos using OpenAI's Sora API from text prompts or reference images, with automatic resizing for image-to-video workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[pauldelavallaz](https://clawhub.ai/user/pauldelavallaz) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers, creators, and agents use this skill to submit Sora video-generation jobs from text prompts or optional reference images and save the resulting MP4 file locally. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Video prompts, optional reference images, and request metadata are sent to OpenAI and may include sensitive or regulated content. <br>
Mitigation: Use OPENAI_API_KEY from the environment, avoid passing secrets on the command line, and do not submit sensitive, regulated, or unauthorized images. <br>
Risk: Video generation can incur API costs and generated videos expire after a short retention window. <br>
Mitigation: Confirm model, duration, and resolution before running requests, monitor API usage, and download generated MP4 files promptly. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/pauldelavallaz/skills/sora-video-gen) <br>
- [OpenAI Videos API endpoint](https://api.openai.com/v1/videos) <br>
- [OpenAI video content endpoint](https://api.openai.com/v1/videos/{video_id}/content) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, API Calls, Files, Guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and MP4 file output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires an OpenAI API key; optional reference images are resized and sent to OpenAI; generated videos should be downloaded promptly because they expire.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

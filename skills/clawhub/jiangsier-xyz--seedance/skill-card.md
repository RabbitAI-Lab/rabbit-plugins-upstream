## Description: <br>
Generate text-to-video, image-to-video, and first/last-frame-to-video outputs with the doubao-seedance-2.0 model through a synchronous wrapper around asynchronous Volcengine Ark and OpenAI-style video APIs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jiangsier-xyz](https://clawhub.ai/user/jiangsier-xyz) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and external users use this skill to generate short videos from text prompts, reference images, or first and last frames through the doubao-seedance-2.0 video-generation API. The skill helps an agent collect required options, confirm quota-consuming generation, run the wrapper, and return the generated video URL or saved file path. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts and provided image files may be sent to Volcengine/Ark, and local image files may be staged in Alibaba OSS. <br>
Mitigation: Confirm that the input data is appropriate for those services before use, avoid sensitive local images, and use least-privilege OSS credentials scoped to a dedicated bucket or prefix. <br>
Risk: Video generation can consume API quota and may take several minutes. <br>
Mitigation: Confirm the prompt, image inputs, duration, ratio, resolution, model, and API type before running generation. <br>
Risk: The optional OSS dependency is not pinned by a lockfile. <br>
Mitigation: Pin the dependency or use a lockfile before production deployment when local image uploads are required. <br>


## Reference(s): <br>
- [Volcengine Ark video generation documentation](https://docs.volcengine.com/docs/82379/2298881) <br>
- [ClawHub skill page](https://clawhub.ai/jiangsier-xyz/skills/seedance) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, files] <br>
**Output Format:** [Markdown guidance with shell commands, JSON task results, a video URL, and an optional saved MP4 file path] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May call external video-generation APIs, poll for task completion, and optionally upload local image inputs to Alibaba OSS as short-lived signed URLs.] <br>

## Skill Version(s): <br>
1.1.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

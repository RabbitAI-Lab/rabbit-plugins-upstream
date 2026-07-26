## Description: <br>
Increase a video's resolution and restore lost detail, up to 4K, covering video super-resolution and temporal detail restoration rather than still images. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[runware](https://clawhub.ai/user/runware) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to route video-to-video super-resolution jobs, choose among supported upscaler models, and verify asynchronous results for sharper clips up to 4K. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Videos selected for upscaling are sent to external model services. <br>
Mitigation: Use the skill only when that provider use is acceptable, and avoid private or sensitive footage unless the user has approved that handling. <br>
Risk: Longer or higher-resolution video upscaling jobs may take time or incur cost. <br>
Mitigation: Confirm the target resolution or factor, model choice, and asynchronous polling expectations before running the job. <br>
Risk: Model availability and accepted parameters can change over time. <br>
Mitigation: Confirm the live model and schema before calling, and verify that the returned video URL meets the requested resolution and quality bar. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/runware/skills/video-upscale) <br>


## Skill Output: <br>
**Output Type(s):** [text, guidance, api calls] <br>
**Output Format:** [Markdown guidance with model-routing and API-call instructions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May guide asynchronous video jobs that return a video URL after polling.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

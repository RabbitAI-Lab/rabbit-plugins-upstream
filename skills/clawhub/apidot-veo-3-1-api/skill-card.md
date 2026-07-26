## Description: <br>
Use APIDot for Veo 3.1 API workflows, including Google Veo API, veo3.1-lite, veo3.1-fast, veo3.1-quality, text-to-video API, image-to-video API, reference image video, async task submission, task_id handling, polling, task status, and webhook integration based on APIDot docs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jiehao71727](https://clawhub.ai/user/jiehao71727) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to plan APIDot Veo 3.1 integrations, route users to current APIDot documentation, and optionally submit reviewed video-generation payloads from a trusted server-side shell. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Live APIDot requests require an API key and may submit sensitive prompts, media URLs, callback URLs, task IDs, or generated video URLs. <br>
Mitigation: Keep APIDOT_API_KEY server-side, avoid logging sensitive request data, and run the submit script only from a trusted server-side shell after payload review. <br>
Risk: Incorrect or stale model details could lead to invalid payloads or misleading integration guidance. <br>
Mitigation: Use current APIDot model pages and documentation for model-specific fields, limits, availability, and commercial terms. <br>
Risk: The security evidence notes powerful operations tied to release and operational workflows. <br>
Mitigation: Use least-privilege tokens, review configured remotes and prompts, and confirm destructive, moderation, release, or email actions before execution. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/jiehao71727/skills/apidot-veo-3-1-api) <br>
- [Local APIDot Veo 3.1 Reference](references/api.md) <br>
- [APIDot Documentation](https://apidot.ai/docs) <br>
- [APIDot Veo 3.1 Documentation](https://apidot.ai/docs/veo-3-1) <br>
- [APIDot Veo 3.1 Model Page](https://apidot.ai/models/veo-3-1) <br>
- [APIDot Quickstart](https://apidot.ai/docs/quickstart) <br>
- [APIDot Webhooks](https://apidot.ai/docs/webhooks) <br>
- [APIDot Veo 3.1 Examples](https://github.com/APIDotAI/veo-3.1-api) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration] <br>
**Output Format:** [Markdown guidance with optional shell command usage] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May reference APIDOT_API_KEY and curl for user-initiated server-side submissions.] <br>

## Skill Version(s): <br>
1.0.4 (source: server-resolved release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

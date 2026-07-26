## Description: <br>
Use APIDot for Hailuo 02 API workflows, including MiniMax Hailuo 02, Hailuo 02 Pro, text-to-video API, image-to-video API, first frame and last frame guidance, physics-aware short video, async task submission, task_id handling, polling, task status, webhook integration, and APIDot docs routing. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jiehao71727](https://clawhub.ai/user/jiehao71727) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this documentation-only skill to route Hailuo 02 integration questions to APIDot docs, model pages, async task patterns, polling guidance, and webhook guidance. It helps plan text-to-video, image-to-video, first-frame, and first-and-last-frame workflows without making network requests or storing credentials. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Real APIDot usage can expose API keys or private prompt, media, generated video, and callback URLs if they are handled in client code or logs. <br>
Mitigation: Keep APIDOT_API_KEY in a server-side secret store and avoid logging private prompts, media URLs, generated video URLs, callback URLs, or API keys. <br>
Risk: APIDot request fields, limits, model availability, and commercial terms may change over time. <br>
Mitigation: Verify request fields and current product details against the live APIDot documentation before submitting jobs. <br>


## Reference(s): <br>
- [APIDot Documentation](https://apidot.ai/docs) <br>
- [APIDot Hailuo 02 Model Page](https://apidot.ai/models/hailuo-02) <br>
- [APIDot Hailuo 02 API Docs](https://apidot.ai/docs/hailuo-02) <br>
- [APIDot Quickstart](https://apidot.ai/docs/quickstart) <br>
- [APIDot Webhooks](https://apidot.ai/docs/webhooks) <br>
- [APIDot Examples](https://github.com/APIDotAI/apidot-examples) <br>
- [ClawHub Skill Page](https://clawhub.ai/jiehao71727/skills/apidot-hailuo-02-api) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance, configuration] <br>
**Output Format:** [Markdown guidance with links and integration planning notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Documentation-only output; no executable files, shell automation, live API calls, or stored credentials.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

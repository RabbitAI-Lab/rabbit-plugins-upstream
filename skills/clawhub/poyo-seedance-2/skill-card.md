## Description: <br>
Seedance 2 video generation on PoYo through the disclosed PoYo generation API for text-to-video, first/last-frame image-to-video, multimodal reference workflows, optional audio, and seed control. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[coolhackboy](https://clawhub.ai/user/coolhackboy) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to prepare and submit Seedance 2 video-generation requests to PoYo, including model selection, payload construction, API submission, and follow-up polling guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends user-provided prompts, media URLs, and callback URLs to PoYo's external API. <br>
Mitigation: Use it only when PoYo API use is approved, and avoid submitting secrets, confidential prompts, private media, or internal-only callback URLs. <br>
Risk: API keys may be exposed if passed directly on the command line or pasted into shared logs. <br>
Mitigation: Prefer the POYO_API_KEY environment variable and avoid including the key in prompts, payload files, shell history, or shared transcripts. <br>


## Reference(s): <br>
- [PoYo Seedance 2 Model Page](https://poyo.ai/models/seedance-2) <br>
- [PoYo Seedance 2 API Docs](https://docs.poyo.ai/api-manual/video-series/seedance-2) <br>
- [PoYo Seedance 2 OpenAPI JSON](https://docs.poyo.ai/api-manual/video-series/seedance-2.json) <br>
- [PoYo Task Status Docs](https://docs.poyo.ai/api-manual/task-management/status) <br>
- [Local API Reference](references/api.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration instructions, API Calls] <br>
**Output Format:** [Markdown with JSON payloads and inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include selected model id, request mode, payload summary, generated audio or seed settings, returned task_id, and polling or webhook next steps.] <br>

## Skill Version(s): <br>
1.0.1 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

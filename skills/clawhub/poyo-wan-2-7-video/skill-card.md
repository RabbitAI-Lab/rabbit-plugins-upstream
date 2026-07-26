## Description: <br>
Wan 2.7 video generation and editing on PoYo via the PoYo generate submit API for text-to-video, image-to-video, reference-to-video, and video editing workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[coolhackboy](https://clawhub.ai/user/coolhackboy) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to prepare PoYo Wan 2.7 video-generation payloads, choose the right model variant, submit trusted async API jobs, and explain polling or webhook follow-up. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: PoYo API keys could be exposed if copied into browser code, public repositories, logs, screenshots, or chat output. <br>
Mitigation: Keep POYO_API_KEY in a server-side environment or secret manager and avoid echoing the key in generated examples or command output. <br>
Risk: Prompts, private media URLs, or callback URLs may contain sensitive information submitted to PoYo or webhook receivers. <br>
Mitigation: Review payloads before submission and avoid sending confidential prompts, private media URLs, or sensitive callback URLs unless the user trusts PoYo and the callback receiver. <br>
Risk: Live API calls may create external video-generation jobs using user-provided inputs. <br>
Mitigation: Submit requests only from a trusted shell when the user explicitly asks to make the live API call and has provided a safe server-side environment. <br>


## Reference(s): <br>
- [PoYo Wan 2.7 Video Model Page](https://poyo.ai/models/wan-2-7-video) <br>
- [PoYo Wan 2.7 Video API Docs](https://docs.poyo.ai/api-manual/video-series/wan-2-7-video) <br>
- [API Reference](references/api.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/coolhackboy/skills/poyo-wan-2-7-video) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Code, Shell commands, Configuration instructions, Guidance] <br>
**Output Format:** [Markdown with JSON payload examples and inline bash or curl commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include model id, workflow type, payload summary, submitted task_id, and next-step polling or webhook guidance.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

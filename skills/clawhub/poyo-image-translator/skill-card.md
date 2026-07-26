## Description: <br>
Image Translator on PoYo / poyo.ai helps agents prepare image translation payloads, submit async tasks, and explain server-side polling or webhook handling for the poyo-ai/image-translator model. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[coolhackboy](https://clawhub.ai/user/coolhackboy) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to prepare PoYo Image Translator requests, generate server-side curl or integration guidance, submit trusted payloads when explicitly requested, and track asynchronous task status or callbacks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: PoYo API keys, authorization headers, task IDs, callback URLs, image URLs, or generated output URLs may be exposed through client-side code, logs, screenshots, repositories, or chat output. <br>
Mitigation: Keep POYO_API_KEY in server-side environment variables or a backend secret manager, avoid browser exposure, and suppress unnecessary logging of sensitive request and response details. <br>
Risk: Submitting private image URLs or source images to PoYo may conflict with organizational data-handling policy. <br>
Mitigation: Review payloads before submission and send private image URLs only when the user's policy permits use of PoYo for those images. <br>
Risk: A live API request could be made before the user has confirmed the provider, payload, and execution environment. <br>
Mitigation: Make live PoYo calls only after explicit user direction and confirmation that the payload should be submitted from a safe server-side environment. <br>


## Reference(s): <br>
- [PoYo Image Translator model page](https://poyo.ai/models/image-translator) <br>
- [ClawHub skill page](https://clawhub.ai/coolhackboy/skills/poyo-image-translator) <br>
- [PoYo Image Translator API Reference](artifact/references/api.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown with JSON payloads and bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include model id, image URL summary, source and target language choices, payload details, returned task_id when submitted, and next-step polling or webhook guidance.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

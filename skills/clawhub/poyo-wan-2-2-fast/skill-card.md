## Description: <br>
Helps agents prepare and submit PoYo Wan 2.2 Fast text-to-video and image-to-video generation tasks, including payload guidance, polling, and webhook follow-up. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[coolhackboy](https://clawhub.ai/user/coolhackboy) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to build PoYo Wan 2.2 Fast video generation requests, choose the correct text-to-video or image-to-video model, submit asynchronous tasks, and plan polling or webhook follow-up. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: PoYo API keys can be exposed if copied into browser code, public repositories, logs, screenshots, or chat output. <br>
Mitigation: Keep POYO_API_KEY in server-side environment variables or a backend secret manager, and avoid printing credentials in examples or command output. <br>
Risk: Prompts, source image URLs, callback URLs, task identifiers, or generated media URLs may contain private information that is sent to or returned by PoYo. <br>
Mitigation: Only submit non-confidential data unless the user explicitly trusts PoYo and the callback receiver for that workflow. <br>
Risk: The packaged shell helper performs a live curl submission when run with a payload file and POYO_API_KEY. <br>
Mitigation: Run the helper only from a trusted shell after reviewing the payload and confirming the user asked to submit a live task. <br>


## Reference(s): <br>
- [PoYo Wan 2.2 Fast model page](https://poyo.ai/models/wan-2-2-fast) <br>
- [PoYo Wan 2.2 text-to-video API docs](https://docs.poyo.ai/api-manual/video-series/wan2.2-text-to-video-fast) <br>
- [PoYo Wan 2.2 image-to-video API docs](https://docs.poyo.ai/api-manual/video-series/wan2.2-image-to-video-fast) <br>
- [Packaged API reference](references/api.md) <br>
- [ClawHub skill page](https://clawhub.ai/coolhackboy/skills/poyo-wan-2-2-fast) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with JSON payload examples and shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include the chosen model id, request payload, polling next step, and returned task_id when a live submission is requested.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

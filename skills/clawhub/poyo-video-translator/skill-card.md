## Description: <br>
Helps agents prepare PoYo Video Translator payloads, submit async video translation tasks, and guide status polling or webhook handling. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[coolhackboy](https://clawhub.ai/user/coolhackboy) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to integrate PoYo's video translation API into server-side workflows, including payload creation, submission, task tracking, callbacks, and subtitle or translated media handling. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: API keys, private media URLs, callback URLs, task IDs, or generated output links could be exposed during integration or troubleshooting. <br>
Mitigation: Keep POYO_API_KEY server-side, review payloads before submission, and avoid logging or sharing private URLs, task IDs, authorization headers, or generated outputs unless allowed by the user's data policy. <br>
Risk: The skill can submit video URLs to PoYo's external API when explicitly used for execution. <br>
Mitigation: Install and run it only for intended PoYo video translation workflows, and make live API calls only after the user confirms the payload and execution environment. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/coolhackboy/skills/poyo-video-translator) <br>
- [PoYo Video Translator Model Page](https://poyo.ai/models/video-translator) <br>
- [PoYo API Key Page](https://poyo.ai/dashboard/api-key) <br>
- [PoYo Video Translator API Reference](references/api.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration instructions, Guidance] <br>
**Output Format:** [Markdown with JSON payload examples and inline bash or curl commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include model id, media URL summary, language choices, payload details, returned task_id, and polling or webhook next steps.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

## Description: <br>
Poyo Wan Animate helps agents prepare, submit, and follow up on PoYo Wan Animate character animation and character replacement video generation jobs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[coolhackboy](https://clawhub.ai/user/coolhackboy) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to build PoYo Wan Animate payloads, choose between character replacement and character animation workflows, submit async generation tasks, and guide polling or webhook follow-up. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can send user-provided video and image URLs to PoYo for generation. <br>
Mitigation: Use it only when the user intends to share those media URLs with PoYo and has the needed consent for likenesses or private content. <br>
Risk: The skill depends on POYO_API_KEY for authenticated API calls. <br>
Mitigation: Keep POYO_API_KEY in a server-side environment or secret manager, and do not expose it in browser code, logs, screenshots, repositories, or chat output. <br>
Risk: Submitted jobs may consume PoYo credits or incur costs. <br>
Mitigation: Make live submissions only after the user explicitly asks and understands that API usage may be billable. <br>
Risk: Callback URLs may reveal private workflow endpoints or receive sensitive job results. <br>
Mitigation: Use callback URLs only with trusted receivers and avoid sensitive callback endpoints unless the user has accepted that data flow. <br>


## Reference(s): <br>
- [PoYo Wan Animate model page](https://poyo.ai/models/wan-animate) <br>
- [PoYo Wan Animate API documentation](https://docs.poyo.ai/api-manual/video-series/wan-animate) <br>
- [Local API reference](references/api.md) <br>
- [ClawHub skill page](https://clawhub.ai/coolhackboy/skills/poyo-wan-animate) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, API Calls] <br>
**Output Format:** [Markdown with JSON payloads and bash or curl examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce a PoYo task_id when a user-requested submission is actually made.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

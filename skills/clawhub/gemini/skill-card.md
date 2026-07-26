## Description: <br>
Gemini CLI for one-shot Q&A, summaries, and generation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[steipete](https://clawhub.ai/user/steipete) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and external users use this skill to route one-shot prompts to Gemini CLI for question answering, summaries, content generation, extension management, and optional JSON output. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts or explicitly referenced files may be sent through Gemini CLI under that tool's account and privacy terms. <br>
Mitigation: Install and use the skill only when those terms are acceptable, and avoid sending sensitive content unless approved for that environment. <br>
Risk: The Gemini CLI --yolo mode can change safety posture. <br>
Mitigation: Avoid using --yolo unless its effects are fully understood and acceptable for the task. <br>
Risk: The skill depends on installing Gemini CLI through Homebrew. <br>
Mitigation: Install only when Homebrew installation of gemini-cli is approved for the target system. <br>


## Reference(s): <br>
- [Gemini developer documentation](https://ai.google.dev/) <br>
- [ClawHub Gemini skill page](https://clawhub.ai/steipete/skills/gemini) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Plain text or Markdown guidance with inline Gemini CLI commands; Gemini CLI can also be requested to return JSON.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires the gemini binary; authentication may require a one-time interactive login.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

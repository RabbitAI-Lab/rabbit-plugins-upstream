## Description: <br>
Ai Video Director helps an agent plan and execute short-form video generation workflows, including script preparation, marketing copy injection, text-to-speech fallback, lip-sync digital-human videos, engine routing, subtitle burn-in, and delivery checks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External creators, marketers, and developers use this skill to turn short-video ideas, product details, or digital-human prompts into guided video generation and publishing workflows with structured status output. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can use local command execution for video processing and diagnostics. <br>
Mitigation: Run it in a trusted workspace, review proposed commands before execution, and ensure ffmpeg-style processing only touches intended media files. <br>
Risk: Generated workflows can depend on external AI, TTS, video, and optional publishing services. <br>
Mitigation: Confirm provider terms, API destinations, and publish targets before processing sensitive media or releasing generated content. <br>
Risk: Outputs and logs may contain product plans, private likeness data, or other sensitive creative material. <br>
Mitigation: Avoid confidential inputs unless the storage location, logs, and external service handling are acceptable for the intended release. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/ai-video-director) <br>
- [Skill homepage](https://skillhub.cn) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, Files, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with JSON status objects and generated media file or URL references] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May reference local video outputs, logs, route metadata, fallback status, and optional publishing results.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

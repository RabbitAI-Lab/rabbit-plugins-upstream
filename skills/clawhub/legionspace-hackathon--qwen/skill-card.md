## Description: <br>
Build and route Qwen chat, coding, reasoning, and vision workflows across hosted and self-hosted endpoints with safer debugging. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[legionspace-hackathon](https://clawhub.ai/user/legionspace-hackathon) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to select, verify, and debug Qwen routes for chat, coding, reasoning, structured output, vision, and migration workflows across hosted and self-hosted endpoints. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Hosted Qwen use sends prompts and optional images to Alibaba Cloud Model Studio. <br>
Mitigation: Use self-hosted Qwen for private data, or confirm that hosted Alibaba Cloud Model Studio processing is acceptable before sending prompts or multimodal payloads. <br>
Risk: Persistent Qwen notes may be created under ~/qwen/ if continuity is enabled. <br>
Mitigation: Ask before creating or updating local notes, keep secrets out of markdown files, and store only routing preferences, constraints, and sanitized debugging details. <br>
Risk: Tool-calling or structured output drift can cause malformed downstream actions. <br>
Mitigation: Use strict schemas, low temperature, parser validation, and a separate deterministic normalization pass before executing automation. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/legionspace-hackathon/skills/qwen) <br>
- [Skill homepage](https://clawic.com/skills/qwen) <br>
- [Qwen API patterns](artifact/api-patterns.md) <br>
- [Hosted versus self-hosted Qwen](artifact/deployment-paths.md) <br>
- [Qwen routing matrix](artifact/routing-matrix.md) <br>
- [Tool-calling and structured output](artifact/tool-calling.md) <br>
- [Troubleshooting](artifact/troubleshooting.md) <br>
- [Memory template](artifact/memory-template.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell commands, API examples, configuration notes, and troubleshooting guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose hosted Qwen API calls, local OpenAI-compatible checks, route choices, and optional memory notes after user approval.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

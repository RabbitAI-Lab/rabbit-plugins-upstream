## Description: <br>
Integrates Modellix's unified API and CLI for async image, video, and audio generation through model selection, task submission, waiting, and download workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[modellix](https://clawhub.ai/user/modellix) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to route Modellix media-generation requests through the preferred CLI workflow or REST fallback, including authentication checks, model defaults, task execution, waiting, and output download. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts, media URLs, and generation inputs may be sent to Modellix during task execution. <br>
Mitigation: Review inputs before submission and avoid sending sensitive or unauthorized media through this workflow. <br>
Risk: Generation requests can create paid Modellix tasks, and duplicate submissions may incur duplicate charges. <br>
Mitigation: Use the CLI wait/recovery flow, check task history after unknown outcomes, and avoid blind retries of paid submissions. <br>
Risk: The CLI can use an existing saved Modellix profile rather than only a session environment variable. <br>
Mitigation: Confirm the intended profile or use session-only MODELLIX_API_KEY when isolation is required. <br>
Risk: Downloaded task resources may expire if not persisted promptly. <br>
Mitigation: Download and store result files soon after successful task completion. <br>


## Reference(s): <br>
- [Modellix Skill Page](https://clawhub.ai/modellix/skills/modellix) <br>
- [Modellix AI Onboarding](https://docs.modellix.ai/get-started.md) <br>
- [Modellix REST API](https://docs.modellix.ai/ways-to-use/api.md) <br>
- [Modellix Models Index](https://docs.modellix.ai/llms.txt) <br>
- [Modellix Docs MCP](https://docs.modellix.ai/mcp) <br>
- [modellix-cli Package](https://www.npmjs.com/package/modellix-cli) <br>
- [Capability Matrix](references/capability-matrix.md) <br>
- [CLI Playbook](references/cli-playbook.md) <br>
- [REST Playbook](references/rest-playbook.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands, JSON examples, and optional generated files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce local media output files after Modellix task completion and download.] <br>

## Skill Version(s): <br>
1.0.20 (source: ClawHub release metadata; artifact frontmatter reports 3.7.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

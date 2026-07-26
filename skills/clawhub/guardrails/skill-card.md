## Description: <br>
Guardrails helps users configure, review, and monitor security guardrails for an OpenClaw workspace through discovery, risk classification, an interview flow, and generated policy files. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dgriffin831](https://clawhub.ai/user/dgriffin831) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent-workspace users use this skill to create and maintain workspace-specific guardrail policies. It scans the workspace context, asks targeted safety questions, generates GUARDRAILS.md and guardrails-config.json, and reports when later changes need review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Workspace metadata, selected file previews, memory-log matches, and interview answers may include sensitive context. <br>
Mitigation: Run setup and review only in workspaces where that data may be processed, avoid entering secrets, and inspect generated guardrails-config.json before retaining or sharing it. <br>
Risk: Question generation and GUARDRAILS.md generation can send workspace-derived data to OpenAI or Anthropic when provider API keys are configured. <br>
Mitigation: Use the skill only when third-party LLM processing is allowed, and remove or redact sensitive workspace content before running LLM-backed setup or review flows. <br>
Risk: Generated guardrails are policy guidance and are not automatic enforcement. <br>
Mitigation: Review the generated GUARDRAILS.md before use, require explicit confirmation for writes, and run monitor or review after installing or removing skills. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/dgriffin831/skills/guardrails) <br>
- [README.md](artifact/README.md) <br>
- [SKILL.md](artifact/SKILL.md) <br>
- [CHANGELOG.md](artifact/CHANGELOG.md) <br>
- [Guardrails configuration schema](artifact/schemas/config.schema.json) <br>
- [Risk classification schema](artifact/schemas/risks.schema.json) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, shell commands, guidance] <br>
**Output Format:** [Markdown policy files, JSON configuration, JSON monitoring reports, and conversational guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Setup and review modes write GUARDRAILS.md and guardrails-config.json only after user confirmation; monitor mode emits a JSON status report.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata and CHANGELOG, released 2026-02-02) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

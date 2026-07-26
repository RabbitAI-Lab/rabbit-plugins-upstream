## Description: <br>
EmoClaw builds a persistent, memory-informed emotional state for AI agents that shifts across conversations, decays between sessions, and can be injected into the system prompt. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[fenrirlabsnl](https://clawhub.ai/user/fenrirlabsnl) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent builders use EmoClaw to add a local, persistent emotional-state layer to an AI agent by extracting configured identity or memory files, training a lightweight model, and injecting an [EMOTIONAL STATE] block into prompts. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Configured identity or memory files may include sensitive passages that are extracted for training. <br>
Mitigation: Review the configured bootstrap source files and inspect extracted_passages.jsonl before labeling or training. <br>
Risk: Optional auto-labeling can send extracted passages to Anthropic. <br>
Mitigation: Keep ANTHROPIC_API_KEY unset unless external labeling is intended, and review extracted passages before enabling labeling. <br>
Risk: The daemon and setup scripts create local files, dependencies, and a Unix socket. <br>
Mitigation: Avoid running the daemon as root, review generated files, and pin or constrain dependencies in stricter environments. <br>


## Reference(s): <br>
- [EmoClaw ClawHub listing](https://clawhub.ai/fenrirlabsnl/skills/emoclaw) <br>
- [Model Architecture](references/architecture.md) <br>
- [Configuration Reference](references/config-reference.md) <br>
- [Emotion Dimensions](references/dimensions.md) <br>
- [Calibration Guide](references/calibration-guide.md) <br>
- [Upgrade Guide](references/upgrading.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell, Python, JSON, and YAML snippets; runtime output is an [EMOTIONAL STATE] text block or daemon JSON response.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Local training and inference write configured state, data, and checkpoint files; optional bootstrap labeling can call Anthropic when ANTHROPIC_API_KEY is set and user consent is provided.] <br>

## Skill Version(s): <br>
1.0.6 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

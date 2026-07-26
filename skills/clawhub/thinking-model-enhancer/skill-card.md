## Description: <br>
Advanced thinking model that improves decision-making speed and accuracy. Integrates with memory system to compare and integrate previous thinking models for continuous enhancement. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xqicxx](https://clawhub.ai/user/xqicxx) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent users use this skill to apply a structured thinking process for decision-making, troubleshooting, skill creation, and comparing current reasoning approaches with stored historical models. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill automatically stores thinking-session content and local state under ~/.claude/thinking_models. <br>
Mitigation: Install only if local history storage is acceptable, avoid using the skill with secrets or sensitive business data, and periodically inspect or delete the stored JSON history. <br>
Risk: Stored reasoning history may influence later recommendations in ways users have not reviewed. <br>
Mitigation: Review or disable auto-store behavior before routine use and scan generated guidance before acting on it. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/xqicxx/skills/thinking-model-enhancer) <br>
- [Publisher profile](https://clawhub.ai/user/xqicxx) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and structured text, with optional Python execution output and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create local JSON state and history under ~/.claude/thinking_models when memory features are active.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and artifact CHANGELOG, released 2026-01-31) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

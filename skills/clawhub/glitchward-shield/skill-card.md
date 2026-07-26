## Description: <br>
Scan prompts for prompt injection attacks before sending them to any LLM. Detect jailbreaks, data exfiltration, encoding bypass, multilingual attacks, and 25+ attack categories using Glitchward's LLM Shield API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[eyeskiller](https://clawhub.ai/user/eyeskiller) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agent builders use this skill to check user input, external content, and agent workflow text for prompt-injection patterns before sending that content to an LLM. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompt text or prompt excerpts are sent to Glitchward for scanning. <br>
Mitigation: Confirm policy permits that external processing before use, and avoid sending sensitive or regulated data unless approved. <br>
Risk: The Shield API token is required for use. <br>
Mitigation: Store GLITCHWARD_SHIELD_TOKEN as an environment secret and avoid committing or exposing it in logs. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/eyeskiller/skills/glitchward-shield) <br>
- [Glitchward Shield](https://glitchward.com/shield) <br>
- [LLMPI Database](https://glitchward.com/llmpi) <br>
- [Glitchward Skill Analyzer](https://glitchward.com/shield/skill-analyzer) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with curl command examples and JSON API response descriptions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires curl, jq, and GLITCHWARD_SHIELD_TOKEN; prompt text is sent to Glitchward's external Shield API for scanning.] <br>

## Skill Version(s): <br>
1.0.1 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

## Description: <br>
Evaluates conversation emotion state, stores compact inferred history, and injects an emotion_state block into the OpenClaw system prompt. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tashfeenahmed](https://clawhub.ai/user/tashfeenahmed) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and OpenClaw operators use this skill to add emotion-aware context to agent bootstrap prompts. It is intended for environments where storing inferred emotion history and sending conversation text to a configured classifier are acceptable. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Conversation text may be sent to OpenAI or a configured classifier endpoint. <br>
Mitigation: Enable the hook only for workloads where that disclosure is acceptable, and avoid untrusted classifier URLs. <br>
Risk: Inferred emotional history is stored across sessions and can be read from other agents by default. <br>
Mitigation: Set EMOTION_MAX_OTHER_AGENTS to 0 for sensitive use, and periodically inspect or delete emotion-state.json files. <br>
Risk: Emotion summaries are injected into future prompts and may influence agent behavior. <br>
Mitigation: Review the injected emotion_state block and disable the hook where emotion-derived context is inappropriate. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/tashfeenahmed/skills/emotion-state) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration] <br>
**Output Format:** [Markdown documentation plus an injected emotion_state text block] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Node; may call OpenAI or a configured classifier endpoint and writes emotion-state.json files in the OpenClaw agent state directory.] <br>

## Skill Version(s): <br>
1.2.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

## Description: <br>
Emotion Router is a Markdown-first soft router for coding agents when the current prompt shows clear urgency, anger or frustration, or workflow confusion signals. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gongyu0918-debug](https://clawhub.ai/user/gongyu0918-debug) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agent platform teams use this skill to choose a cautious response route for coding-agent work when visible prompts show urgency, frustration, or workflow confusion. It helps convert pressure signals into bounded execution guidance without modeling hidden user state or long-term personality. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may influence how an agent phrases and prioritizes work when it detects urgency, frustration, or confusion. <br>
Mitigation: Review the selected route guidance before enabling it in production, especially for teams that do not want tone or workflow routing based on inferred work-state cues. <br>
Risk: Misrouting an ordinary task as urgency, frustration, or confusion could add unnecessary constraints to the agent response. <br>
Mitigation: Apply the skill only when the current prompt has clear active signals, and stop at ordinary work when emotion words are merely topics, quotes, field names, or neutral instructions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/gongyu0918-debug/skills/emotion-skill) <br>
- [Urgency route reference](artifact/references/urgency-route.md) <br>
- [Anger or frustration route reference](artifact/references/anger-frustration-route.md) <br>
- [Confusion route reference](artifact/references/confusion-route.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown routing guidance with route-specific response patterns and examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Markdown-only guidance; it does not access private data, run commands, persist memory, or change files by itself.] <br>

## Skill Version(s): <br>
2.0.5 (source: target metadata, release evidence, SKILL.md frontmatter, agents/openai.yaml) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

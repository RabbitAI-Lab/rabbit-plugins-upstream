## Description: <br>
Markdown-first soft router for coding agents that activates only for clear urgency, strong anger or frustration, or confusion about the active workflow. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gongyu0918-debug](https://clawhub.ai/user/gongyu0918-debug) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and coding-agent users use this skill to choose one cautious response route when a current prompt shows urgency, anger or frustration, or workflow confusion. It helps the agent adjust response style without labeling the user or widening the task. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Automatic invocation may route an agent response when a message sounds urgent, frustrated, or workflow-confused. <br>
Mitigation: Review the trigger behavior before deployment, especially if explicit skill invocation is preferred. <br>
Risk: Misrouting could change response style for ordinary tasks or quoted emotional content. <br>
Mitigation: Keep the skill's cautious trigger gate and single-route priority rules intact during review. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/gongyu0918-debug/skills/emotion-skill) <br>
- [Urgency Route](references/urgency-route.md) <br>
- [Anger Or Frustration Route](references/anger-frustration-route.md) <br>
- [Confusion Route](references/confusion-route.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Routes at most one active work-state signal and asks the agent to load exactly one matching reference when active.] <br>

## Skill Version(s): <br>
2.0.6 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

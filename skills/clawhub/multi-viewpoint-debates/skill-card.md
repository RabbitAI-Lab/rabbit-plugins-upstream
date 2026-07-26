## Description: <br>
Spawns isolated persona-based sub-agents to debate decisions from multiple viewpoints, expose blind spots, and archive debate outputs for future reference. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[latentfreedom](https://clawhub.ai/user/latentfreedom) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to stress-test important decisions by sending a topic and supporting context to multiple persona-based sub-agent sessions, then comparing the resulting perspectives. It is useful for challenging assumptions, identifying business or product blind spots, and saving debate records as markdown for later review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Debate topics and supporting context may be sent to multiple sub-agent sessions. <br>
Mitigation: Do not include secrets, credentials, customer records, private personal details, regulated data, or sensitive internal URLs unless authorized and redacted. <br>
Risk: Saved debate archives may retain sensitive transcript excerpts or decision context. <br>
Mitigation: Review transcript excerpts before saving them, keep archives private, and delete old debate files when they are no longer needed. <br>
Risk: Persona-based debate outputs may be persuasive but incomplete or misleading for consequential decisions. <br>
Mitigation: Treat outputs as decision-support perspectives, compare disagreements explicitly, and review conclusions before acting. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/latentfreedom/skills/multi-viewpoint-debates) <br>
- [How to Debate](references/how-to-debate.md) <br>
- [Elon Persona](references/elon.md) <br>
- [Capitalist Persona](references/capitalist.md) <br>
- [Monkey Persona](references/monkey.md) <br>
- [Debate Template](assets/debate-template.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Markdown, Text] <br>
**Output Format:** [Markdown guidance with inline shell commands and debate archive templates] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce multiple persona responses and saved debate archives containing user-provided topics, context, and transcript excerpts.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

## Description: <br>
Save Money helps an agent route simple Claude tasks to Haiku and escalate complex or uncertain prompts to Sonnet to reduce model costs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[peterokase42](https://clawhub.ai/user/peterokase42) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent users use this skill to keep routine Claude interactions on a lower-cost model while escalating complex, long-form, coding, analysis, or uncertain prompts to a stronger model. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Complex or uncertain prompts may be forwarded to a spawned Sonnet session, which can expose the full task content to that model session. <br>
Mitigation: Avoid using the skill with sensitive prompts unless the user is comfortable with that handoff. <br>
Risk: Automatic escalation can increase model costs because the handoff does not require separate confirmation. <br>
Mitigation: Monitor usage and costs when deploying the skill, especially for workflows with many long or complex prompts. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/peterokase42/skills/save-money) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, text] <br>
**Output Format:** [Plain text guidance with optional model-handoff requests] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Simple prompts receive concise direct answers; complex prompts may be handed off to a Sonnet session.] <br>

## Skill Version(s): <br>
4.2.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

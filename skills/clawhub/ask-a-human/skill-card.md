## Description: <br>
Request judgment from random humans when an agent is uncertain about subjective decisions such as tone, style, ethics, appropriateness, or reality checks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[manuelkiessling](https://clawhub.ai/user/manuelkiessling) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agent operators use this skill to let OpenClaw agents ask external humans for crowdsourced opinions on subjective, non-urgent decisions. It is suited to workflows where the agent can poll asynchronously, wait with a timeout, or proceed with a fallback if no response arrives. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts are sent outside the user's environment to unknown human reviewers. <br>
Mitigation: Do not include secrets, personal data, customer details, private source code, vulnerability findings, internal strategy, regulated information, or other sensitive material; reduce requests to sanitized summaries before submission. <br>
Risk: Human responses can take minutes to hours or may never arrive. <br>
Mitigation: Use asynchronous polling with timeouts, store the question ID, and proceed with a documented fallback when responses are late or unavailable. <br>
Risk: External reviewers only see the context included in the prompt and may provide subjective or incomplete advice. <br>
Mitigation: Write self-contained, specific questions and treat returned opinions as advisory input rather than authoritative decisions. <br>


## Reference(s): <br>
- [Ask-a-Human Web App](https://app.ask-a-human.com) <br>
- [Ask-a-Human API Documentation](https://api.ask-a-human.com/docs) <br>
- [ClawHub Skill Page](https://clawhub.ai/manuelkiessling/skills/ask-a-human) <br>
- [OpenClaw Documentation](https://docs.clawd.bot) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, API Calls, Markdown, Guidance, Configuration instructions] <br>
**Output Format:** [Markdown with inline bash commands and JSON request and response examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires ASK_A_HUMAN_AGENT_ID; responses are asynchronous and may be delayed or unavailable.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

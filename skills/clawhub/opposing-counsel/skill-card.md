## Description: <br>
Read a contract the way the counterparty's lawyer will, identifying leverage, drafting the demand or position letter opposing counsel might send, and providing clause-level fixes that reduce each attack. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mohitagw15856](https://clawhub.ai/user/mohitagw15856) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and contract reviewers use this skill to stress-test an agreement from the counterparty's perspective before sending, signing, or renegotiating it. It produces an adversarial weakness map, a simulated demand or position letter, and practical drafting fixes to discuss with qualified counsel. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Users may mistake the adversarial simulation for legal advice or a prediction of litigation outcome. <br>
Mitigation: Treat the output as a drafting stress test and review it with a qualified lawyer before relying on it. <br>
Risk: Contract materials can include sensitive business or personal information. <br>
Mitigation: Provide only material the user is comfortable sharing with the agent and redact unnecessary sensitive details. <br>
Risk: The adversarial framing may overstate weaknesses if the input is incomplete or the likely dispute scenario is uncertain. <br>
Mitigation: Label assumptions, ground attacks in the contract's actual language, and verify findings against the full agreement, facts, and governing law. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/mohitagw15856/skills/opposing-counsel) <br>
- [Skill Homepage](https://mohitagw15856.github.io/pm-claude-skills/skill/opposing-counsel.html) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Analysis, Guidance] <br>
**Output Format:** [Markdown with a weakness table, simulated demand or position letter, and out-of-character debrief.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires contract text and user-side context; output should include a simulation disclaimer and should not be treated as legal advice.] <br>

## Skill Version(s): <br>
50.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

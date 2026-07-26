## Description: <br>
Turns an AI agent with persistent memory into a quit-smoking sponsor that provides zero-shame, evidence-based guidance for quit decisions, cravings, slips, relapse recovery, check-ins, and private logbook continuity. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[metrox-eth](https://clawhub.ai/user/metrox-eth) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External adult users who are quitting smoking or other smoked tobacco use this skill to turn an agent into a persistent quit sponsor for cravings, slips, relapse recovery, check-ins, and a private logbook. It is designed to complement professional care, not replace clinicians, emergency services, or crisis support. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may store sensitive quit-smoking history in agent memory or a logbook. <br>
Mitigation: Use local or private memory, review what is stored, and delete the logbook or memory entries when the user requests deletion. <br>
Risk: Users may treat the sponsor role as medical, emergency, or crisis care. <br>
Mitigation: Keep the safety boundary explicit: clinicians handle medical questions, emergency services handle physical red flags, and human crisis lines handle acute distress or self-harm signals. <br>
Risk: A weak, untested, truncated, or bare model may mishandle live craving or relapse scenarios. <br>
Mitigation: Run the bundled model-fit test before crisis use and avoid models or routes that return empty, truncated, moralizing, or unsafe responses. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/metrox-eth/skills/quit-sponsor) <br>
- [Skill README](artifact/README.md) <br>
- [Safety rails](artifact/SAFETY.md) <br>
- [Model fit guidance](artifact/MODEL_FIT.md) <br>
- [Evidence references](artifact/references.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown or plain-text sponsor responses with optional logbook entries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires persistent memory or a user-owned logbook for continuity; crisis and medical escalation guidance must remain visible to the agent.] <br>

## Skill Version(s): <br>
0.6.0 (source: SKILL.md metadata, release evidence, README changelog) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

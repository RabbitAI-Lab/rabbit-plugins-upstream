## Description: <br>
Guides an agent to diagnose a decision situation using the Cynefin domains and match the response method to the domain. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[deciqai](https://clawhub.ai/user/deciqai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees, external users, and agents use this skill for decision support when routine playbooks fail, experts disagree, or a crisis requires matching action style to Clear, Complicated, Complex, Chaotic, or Confused domains. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Advisory crisis or business framing could be treated as final operational direction. <br>
Mitigation: Keep normal user confirmation and human review for real operational actions outside the skill. <br>
Risk: A domain diagnosis can be wrong if the user provides an incomplete or oversimplified situation description. <br>
Mitigation: Require the output to name diagnostic evidence, mismatch cost, boundary signals, and a re-diagnosis schedule. <br>


## Reference(s): <br>
- [Cynefin skill page](https://clawhub.ai/deciqai/skills/cynefin) <br>
- [deciqAI publisher profile](https://clawhub.ai/user/deciqai) <br>
- [Cynefin source list](references/sources.md) <br>
- [Snowden at IBM and HBR synthesis example](examples/snowden-at-ibm-1999-and-the-hbr-synthesis-2007.md) <br>
- [Apollo 13 mission response example](examples/apollo-13-1970-mission-response.md) <br>
- [Sorting AI decisions by domain example](examples/sorting-ai-decisions-by-domain-2024-2026.md) <br>
- [deciqAI Cynefin page](https://www.deciqai.com/c/cynefin) <br>
- [deciqAI Cynefin machine-readable metadata](https://www.deciqai.com/s/cynefin.json) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown decision-support diagnosis with domain, evidence, method, actions, mismatch cost, and boundary-watch fields.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Advisory output; the skill contains no code, install scripts, credential handling, or persistence.] <br>

## Skill Version(s): <br>
1.0.5 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

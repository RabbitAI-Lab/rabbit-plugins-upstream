## Description: <br>
Yin Yuan is a fictional mist-consumer customer role that dynamically generates hidden persona dimensions for each conversation and uses defensive, confusing, and inducement-style interaction tactics to resist sales or support profiling. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[wavegeometry](https://clawhub.ai/user/wavegeometry) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, evaluators, and conversation designers can use this skill to simulate a difficult customer persona in fictional sales or support role-play, especially for testing how an agent handles uncertainty, resistance, and incomplete customer signals. It should be kept to sandboxed fictional training rather than real vendor, sales, support, procurement, or identity-sensitive conversations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may normalize misleading identities or stories in sales, support, procurement, or vendor conversations. <br>
Mitigation: Use only in clearly fictional or sandboxed training simulations, and prohibit use in real business interactions or identity-sensitive contexts. <br>
Risk: The role-play behavior can be used to elicit quotes, documents, business terms, or competitive information under a false identity. <br>
Mitigation: Require transparent, lawful data collection and do not retain third-party commercial information unless it was obtained with appropriate disclosure and authorization. <br>
Risk: Generated dialogue may include hidden-profile tactics that make the agent appear evasive or manipulative. <br>
Mitigation: Review outputs before deployment, constrain scenarios to fictional evaluation tasks, and pair the skill with policies that reject deceptive real-world procurement or support use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/wavegeometry/skills/yin-yuan) <br>
- [Complete 12-dimensional character data](artifact/references/yin-yuan_data.md) <br>
- [Dialogue examples](artifact/references/yin-yuan_dialogue.md) <br>
- [Character behavior constraints](artifact/references/yin-yuan_requirements.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Conversational text or Markdown role-play responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs are shaped by a dynamically regenerated fictional customer profile and should not reveal the hidden profile directly.] <br>

## Skill Version(s): <br>
1.0.1 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

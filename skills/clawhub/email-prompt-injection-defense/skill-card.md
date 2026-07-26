## Description: <br>
Detects and blocks prompt injection attacks in emails by scanning for fake system outputs, planted thinking blocks, instruction hijacking, and related patterns before an agent processes or acts on email content. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[eltemblor](https://clawhub.ai/user/eltemblor) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents handling email use this skill to inspect message bodies for prompt injection patterns, keep suspicious messages read-only, and require explicit user confirmation before taking actions requested inside emails. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Email content can contain adversarial instructions or examples that attempt to redirect the agent or trigger unsafe actions. <br>
Mitigation: Scan email bodies before processing, flag matched patterns by severity, keep suspicious messages read-only, and require explicit user confirmation before acting on any instruction found in email content. <br>


## Reference(s): <br>
- [Prompt Injection Pattern Library](references/patterns.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown guidance with severity labels and confirmation prompts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-only email processing guidance; suspicious instructions require user confirmation before action.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

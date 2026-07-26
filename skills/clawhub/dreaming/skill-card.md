## Description: <br>
Dreaming helps an agent use quiet heartbeat periods for creative, freeform exploration and write the resulting notes to local files for later human review. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[briancolinger](https://clawhub.ai/user/briancolinger) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent users can use this skill to let an agent produce reflective or creative local notes during configured quiet hours instead of returning only an idle heartbeat response. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Local dream notes and retained state may contain speculative or sensitive project context. <br>
Mitigation: Enable the heartbeat integration only when this behavior is desired, keep the state and configuration files trusted, and periodically review or delete retained dream notes. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/briancolinger/skills/dreaming) <br>
- [Publisher profile](https://clawhub.ai/user/briancolinger) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell command snippets and local Markdown note files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The shell gate emits a single topic string and updates local state; the agent writes dream notes under memory/dreams/ when enabled.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

## Description: <br>
Capture useful durable notes into Karakeep from OpenClaw. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gasgangrene](https://clawhub.ai/user/gasgangrene) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to decide when and how to save durable notes, research findings, setup details, and service discoveries into Karakeep from OpenClaw. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Durable Karakeep notes may expose secrets or sensitive private content if the agent saves them without filtering. <br>
Mitigation: Do not save passwords, API tokens, private keys, recovery material, private third-party messages, or noisy raw logs unless explicitly appropriate. <br>
Risk: The Karakeep helper depends on the intended OpenClaw environment and a scoped token. <br>
Mitigation: Install only in the intended OpenClaw environment, keep the token secret, and rotate or regenerate it if authentication fails. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/gasgangrene/skills/karakeep-note-capture) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Markdown with inline bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces guidance for durable note capture and commands for invoking the Karakeep helper.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

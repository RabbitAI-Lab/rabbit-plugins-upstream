## Description: <br>
LYRA 3-Brain Memory helps agents keep working, library, and outer-reference memory through session snips, local memory growth, recall, and heartbeat workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[deepseekoracle](https://clawhub.ai/user/deepseekoracle) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill when they want an agent to remember completed work, append compact session logs, grow a local memory graph, and recall prior task context from a configured LYRA_CORE workspace. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can create persistent local memory, and the security scan says that storage behavior needs review before installation. <br>
Mitigation: Confirm where LYRA_CORE_ROOT points, what content will be stored, and how to disable or delete memory before enabling session logging or memory growth. <br>
Risk: Session snips and grow commands may capture sensitive operational details if users provide secrets or tokens. <br>
Mitigation: Do not pass API keys, Discord tokens, moltx_sk_* values, or other secrets into memory commands; review snip lines before writing them. <br>
Risk: Running the skill against the wrong shared workspace could append memory to another user's tree. <br>
Mitigation: Set LYRA_CORE_ROOT explicitly to the intended local LYRA_CORE directory and require consent before writing to shared or external workspaces. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/deepseekoracle/skills/lyra-brain) <br>
- [Project link from metadata](https://github.com/DeepSeekOracle/lygo-protocol-stack) <br>
- [Agent contract](references/AGENT_CONTRACT.md) <br>
- [Memory layout](references/MEMORY_LAYOUT.md) <br>
- [Security notes](references/SECURITY.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and local file outputs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May append markdown memory files, reference stubs, and graph entries under the configured LYRA_CORE_ROOT.] <br>

## Skill Version(s): <br>
2.0.0 (source: server release metadata and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

## Description: <br>
Public hybrid LYRA and OpenClaw map for browser, Discord, Moltbook/MoltX, Clawnch economy, memory layers, and local Ollama workflows, with runtime secrets omitted and external actions consent-gated. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[deepseekoracle](https://clawhub.ai/user/deepseekoracle) <br>

### License/Terms of Use: <br>
LYGO Sovereign License v2.0 <br>


## Use Case: <br>
External operators and developers use this skill as a public installation and orchestration map for a broader LYRA/OpenClaw agent stack. It helps agents propose install commands, configuration steps, consent checks, and security boundaries without embedding credentials. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Credentials could be exposed if users paste tokens, private keys, guild secrets, or API keys into prompts, logs, or memory. <br>
Mitigation: Keep credentials in a local vault, environment variables, OS keychain, or other operator-controlled store outside the skill package and public logs. <br>
Risk: Companion stack actions such as browser writes, social posts, token launches, or memory writes can affect external systems. <br>
Mitigation: Require explicit human approval before those actions and review separately installed companion skills before use. <br>
Risk: Host LYRA/OpenClaw runtimes may have network or shell capabilities outside this public package. <br>
Mitigation: Treat this package as a map only and apply local runtime permissions, scans, and approval gates to the broader stack. <br>


## Reference(s): <br>
- [LYGO Protocol Stack](https://github.com/DeepSeekOracle/lygo-protocol-stack) <br>
- [ClawHub skill page](https://clawhub.ai/deepseekoracle/skills/lyra-open-claw) <br>
- [Security notes](references/SECURITY.md) <br>
- [SkillSpector audit](references/SKILLSPECTOR_AUDIT.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands, configuration] <br>
**Output Format:** [Markdown with install command examples and configuration guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [No secrets are included; external actions are consent-gated.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release, SKILL.md frontmatter, claw.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

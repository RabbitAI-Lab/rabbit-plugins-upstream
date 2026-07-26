## Description: <br>
Grants the agent real-time access to prediction markets (Polymarket, Kalshi, Limitless) for fact-checking, probability analysis, and order execution. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[realfishsam](https://clawhub.ai/user/realfishsam) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and developers use this skill to let an agent search prediction markets, retrieve implied probabilities, compare market pricing, and execute orders when explicitly requested. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can use private trading credentials to place real-money prediction-market orders. <br>
Mitigation: Configure credentials only when trading is intended; otherwise leave private keys and trading API keys unset. <br>
Risk: Order execution does not enforce a separate confirmation gate in code. <br>
Mitigation: Keep user confirmation outside the agent, require explicit amount and outcome before trading, and prefer low-balance or tightly scoped accounts. <br>
Risk: Configured exchange private keys and API keys are sensitive signing material. <br>
Mitigation: Store credentials in a managed secret store, restrict account permissions where exchanges allow it, and rotate keys after suspected exposure. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/realfishsam/skills/molt-pmxt) <br>
- [Publisher profile](https://clawhub.ai/user/realfishsam) <br>
- [Skill instructions](artifact/SKILL.md) <br>
- [README](artifact/README.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Structured tool results with Markdown guidance and code or shell snippets where setup is needed] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May use live prediction-market APIs and authenticated trading credentials when configured.] <br>

## Skill Version(s): <br>
1.1.0 (source: release metadata and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

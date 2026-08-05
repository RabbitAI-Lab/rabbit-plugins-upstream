## Description: <br>
LYRA 3-Brain Memory gives agents explicit local disk recall, logging, and graph-growth workflows under LYRA_CORE_ROOT with consent-gated writes and no network behavior. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[deepseekoracle](https://clawhub.ai/user/deepseekoracle) <br>

### License/Terms of Use: <br>
LYGO Sovereign License v2.0 <br>


## Use Case: <br>
Developers and agent operators use this skill when a LYRA-based agent needs persistent local memory operations: recalling prior stored context, writing small session snips, or growing compact facts into a local graph after explicit user consent. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Persistent memory writes can retain session-derived text on disk after the chat ends. <br>
Mitigation: Use write commands only after explicit user consent, set LYRA_CORE_ROOT or LYRA_CORE to a directory the operator controls, and delete or archive the memory files when they should no longer persist. <br>
Risk: Secrets or sensitive personal data could be stored if supplied to memory or graph-growth commands. <br>
Mitigation: Do not store credentials, tokens, private keys, or sensitive personal data; the skill evidence describes secret checks and no-secrets guidance for write inputs. <br>


## Reference(s): <br>
- [LYRA 3-Brain Memory on ClawHub](https://clawhub.ai/deepseekoracle/skills/lyra-brain) <br>
- [LYGO Protocol Stack](https://github.com/DeepSeekOracle/lygo-protocol-stack) <br>
- [Agent Contract](references/AGENT_CONTRACT.md) <br>
- [Memory Layout](references/MEMORY_LAYOUT.md) <br>
- [Security](references/SECURITY.md) <br>
- [SkillSpector Audit](references/SKILLSPECTOR_AUDIT.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration instructions] <br>
**Output Format:** [Markdown with inline shell commands and local file path guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May invoke local Python CLIs for recall or consent-gated persistent writes when the operator has configured LYRA_CORE_ROOT.] <br>

## Skill Version(s): <br>
2.1.0 (source: frontmatter, claw.json, server release) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

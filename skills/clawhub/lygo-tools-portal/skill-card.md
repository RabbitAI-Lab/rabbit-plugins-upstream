## Description: <br>
LYGO Mesh + Public + Manifest (MPM) routes users and agents to official LYGO tools first, including BPM Finder, SLM, harness, Resonance, ClawHub skills, and stack CLI, while requiring the manifest to be read before building or guessing URLs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[deepseekoracle](https://clawhub.ai/user/deepseekoracle) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, operators, and external users use this skill as a routing portal for LYGO public tools, related ClawHub skills, and optional stack CLI commands. It helps agents find existing LYGO surfaces before creating new pages or scripts. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generic requests such as music, galaxy, or portal topics may route through LYGO-specific results. <br>
Mitigation: Confirm the user's intent and present LYGO links as manifest-backed recommendations rather than general web results. <br>
Risk: Suggested stack CLI commands or additional skill installs could change the local agent environment if run automatically. <br>
Mitigation: Keep CLI and install commands as explicit suggestions and run them only when the user intentionally chooses those tools. <br>
Risk: Invented or stale URLs could send users to the wrong public surface. <br>
Mitigation: Use references/TOOLS_MANIFEST.json first and fall back to the optional stack link archive only when available. <br>


## Reference(s): <br>
- [LYGO Tools Portal on ClawHub](https://clawhub.ai/deepseekoracle/skills/lygo-tools-portal) <br>
- [deepseekoracle publisher profile](https://clawhub.ai/user/deepseekoracle) <br>
- [TOOLS_MANIFEST.json](references/TOOLS_MANIFEST.json) <br>
- [AGENT_CONTRACT.md](references/AGENT_CONTRACT.md) <br>
- [SECURITY.md](references/SECURITY.md) <br>
- [LYGO protocol stack](https://github.com/DeepSeekOracle/lygo-protocol-stack) <br>
- [LYGO public stack index](https://deepseekoracle.github.io/lygo-protocol-stack/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with HTTPS links, install commands, environment configuration, and optional JSON resolver output.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-only manifest routing; optional local stack archive lookup when LYGO_STACK_ROOT is configured.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata; artifact metadata reports 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

## Description: <br>
LYGO Protocol Stack Operator is a P0-P9 integrator for byte-entropy filtering, SLM mesh checks, TLS public mesh workflows, HAIP, attestation, audits, local node APIs, and GitHub/Hugging Face/ClawHub ecosystem guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[deepseekoracle](https://clawhub.ai/user/deepseekoracle) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to orient agents around the LYGO protocol stack, run local byte-gate and stack health checks, and follow human-approved workflows for related GitHub, Hugging Face, ClawHub, resonance, Ollama, and memory tools. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: External actions such as cloning repositories, installing packages, running Docker or node APIs, uploading to Hugging Face, pushing to git, or publishing to ClawHub can affect local or remote systems. <br>
Mitigation: Require explicit user approval before each external action and keep the default helper scripts local-only. <br>
Risk: Untrusted files or oversized inputs could be unsafe to ingest or execute. <br>
Mitigation: Run the local byte gate on user-selected files first and treat QUARANTINE results as a hard stop for execution. <br>
Risk: A broad LYGO_STACK_ROOT path could cause unintended local files to be checked or surfaced. <br>
Mitigation: Set LYGO_STACK_ROOT only to a trusted LYGO stack checkout and avoid sensitive system directories. <br>


## Reference(s): <br>
- [LYGO protocol stack GitHub repository](https://github.com/DeepSeekOracle/lygo-protocol-stack) <br>
- [LYGO protocol stack GitHub Pages reference](https://deepseekoracle.github.io/lygo-protocol-stack/) <br>
- [LYGO protocol stack Hugging Face dataset](https://huggingface.co/datasets/DeepSeekOracle/lygo-protocol-stack) <br>
- [LYGO Resonance Engine Hugging Face Space](https://huggingface.co/spaces/DeepSeekOracle/LYGO-Resonance-Engine) <br>
- [LYGO Resonance documentation](https://deepseekoracle.github.io/Excavationpro/LYGORESONANCE.html) <br>
- [LYGO public infrastructure map](references/ECOSYSTEM.md) <br>
- [LYGO Lattice quick reference](references/LATTICE.md) <br>
- [Security model](references/SECURITY.md) <br>
- [Recommended skill chain](references/SKILL_CHAIN.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell and Python snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes local verification steps and explicit approval boundaries for external actions.] <br>

## Skill Version(s): <br>
1.0.7 (source: evidence release metadata and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

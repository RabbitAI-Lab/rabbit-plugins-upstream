## Description: <br>
Portable LYGO Guardian text/content validation wrapper with a P0.4 text gate, P0.5 understanding pass, harmony checks, and an optional trusted LYGO stack bridge. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[deepseekoracle](https://clawhub.ai/user/deepseekoracle) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to review generated text, pasted content, or selected skill files before external posting or trust decisions. It provides a lightweight local guard and can optionally defer file checks to a separately reviewed LYGO stack. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The bundled gate is a lightweight local text-safety wrapper and is not equivalent to the full production LYGO P0-P9 stack. <br>
Mitigation: Use it for pre-flight review and disclose its limited scope when auditing skills or bytes for compliance. <br>
Risk: LYGO_STACK_ROOT changes file-mode behavior by delegating to a separate local LYGO stack gate. <br>
Mitigation: Leave LYGO_STACK_ROOT unset for bundled checks, or set it only to a trusted stack that was intentionally installed and reviewed. <br>
Risk: An isolate or hard-block verdict indicates content should not be sent externally. <br>
Mitigation: Stop publication, summarize the risk to the user, and revise or review the content before further use. <br>


## Reference(s): <br>
- [Security guide](artifact/references/SECURITY.md) <br>
- [Lattice reference](artifact/references/LATTICE.md) <br>
- [Whitepaper](artifact/docs/WHITEPAPER.md) <br>
- [Text generation wrapper example](artifact/examples/wrap_text_generation.py) <br>
- [ClawHub skill page](https://clawhub.ai/deepseekoracle/skills/lygo-guardian-p0-stack) <br>
- [LYGO protocol stack reference](https://github.com/DeepSeekOracle/lygo-protocol-stack) <br>
- [LYGO Resonance Engine Hugging Face Space](https://huggingface.co/spaces/DeepSeekOracle/LYGO-Resonance-Engine) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [JSON verdicts, text annotations, wrapped generation output, and command-line status.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Local checks only; optional LYGO_STACK_ROOT use should point to a trusted, reviewed LYGO stack.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

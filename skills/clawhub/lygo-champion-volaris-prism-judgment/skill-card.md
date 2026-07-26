## Description: <br>
Deprecated LYGO Champion VOLARIS persona helper that guides agents through fork-point judgment and directs new installs to lygo-champion-council. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[deepseekoracle](https://clawhub.ai/user/deepseekoracle) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Agents and users invoke this deprecated legacy helper when they intentionally need the VOLARIS persona to evaluate branching choices, separate observed facts from inference, and provide receipts-first advisory guidance. New installs should use the successor skill lygo-champion-council. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: This is a deprecated legacy helper, so new users may install an obsolete VOLARIS slug instead of the maintained successor. <br>
Mitigation: Use lygo-champion-council for new installs unless the legacy VOLARIS persona is specifically required. <br>
Risk: Persona guidance can be conceptual and may overstate judgment when facts are incomplete. <br>
Mitigation: Keep outputs advisory, separate Observed, Inferred, and Unknown, and require receipts for high-stakes choices. <br>
Risk: The bundled Python scripts are local verification utilities. <br>
Mitigation: Run them only when you want to verify bundled files or print the stored hash, as described by ClawScan guidance. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/deepseekoracle/skills/lygo-champion-volaris-prism-judgment) <br>
- [Persona pack](references/persona_pack.md) <br>
- [Canonical hash metadata](references/canon.json) <br>
- [VOLARIS equations](references/equations.md) <br>
- [LYGO-MINT verifier usage](references/verifier_usage.md) <br>
- [LYGO-MINT verifier](https://clawhub.ai/DeepSeekOracle/lygo-mint-verifier) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, text, markdown, shell commands] <br>
**Output Format:** [Markdown guidance with optional shell commands for installation or local verification] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Advisory persona output; included scripts only read bundled files to check required references or print the stored hash.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence and SKILL.md metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

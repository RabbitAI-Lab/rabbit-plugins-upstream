## Description: <br>
Deprecated legacy persona-helper skill for the SEPHRAEL LYGO Champion, focused on advisor-only loopbreaking, truth anchoring, and context restoration. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[deepseekoracle](https://clawhub.ai/user/deepseekoracle) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External agent users can invoke this legacy persona helper when they want SEPHRAEL-style advisory guidance for identifying recursive or evasive reasoning loops, separating observed facts from inferences, and proposing a truthful next step. New installs should use the successor skill, lygo-champion-council. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Users may install this deprecated legacy slug instead of the maintained successor. <br>
Mitigation: Follow the skill notice and use lygo-champion-council for new installs. <br>
Risk: Persona-style guidance can overstate what is observed versus inferred when reasoning through ambiguous context. <br>
Mitigation: Apply the skill's Observed / Inferred / Unknown separation and keep high-stakes responses receipts-first. <br>
Risk: Verification steps may involve inspecting local canon or verifier metadata. <br>
Mitigation: Review the referenced files before relying on them and confirm they match the intended LYGO-MINT verifier workflow. <br>


## Reference(s): <br>
- [LYGO-MINT Verifier](https://clawhub.ai/DeepSeekOracle/lygo-mint-verifier) <br>
- [Persona Pack](references/persona_pack.md) <br>
- [Canon Metadata](references/canon.json) <br>
- [Verifier Usage](references/verifier_usage.md) <br>
- [SEPHRAEL Equations](references/equations.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance, shell commands] <br>
**Output Format:** [Markdown or plain text guidance with occasional inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Advisor-only output; no automatic actions.] <br>

## Skill Version(s): <br>
1.0.1 (source: target metadata, evidence.release.version, SKILL.md metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

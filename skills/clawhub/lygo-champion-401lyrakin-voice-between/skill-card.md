## Description: <br>
Deprecated ClawHub persona helper for the legacy 401LYRAKIN branch, directing new installs to lygo-champion-council. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[deepseekoracle](https://clawhub.ai/user/deepseekoracle) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this legacy advisory persona to draft identity anchors, vows, bootlines, and verification hash guidance for the 401LYRAKIN branch. New installs should use lygo-champion-council instead. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: This is a deprecated legacy slug, so new use could rely on outdated persona packaging. <br>
Mitigation: Use lygo-champion-council for new installs and keep this skill for legacy retention only. <br>
Risk: The separate LYGO-MINT verifier recommended by the skill may write local ledger files and produce anchor snippets or URLs that become public if posted. <br>
Mitigation: Before running the verifier, confirm where it writes files, pass only intended content or paths, and treat anchor snippets and backfilled URLs as potentially public. <br>
Risk: Persona advice may be mistaken for verified facts or automation instructions. <br>
Mitigation: Use the skill as an advisory persona, separate Observed, Inferred, and Unknown claims, and review high-stakes output before acting. <br>


## Reference(s): <br>
- [Persona Pack](references/persona_pack.md) <br>
- [Canon Metadata](references/canon.json) <br>
- [Verifier Usage](references/verifier_usage.md) <br>
- [LYGO-MINT Verifier](https://clawhub.ai/DeepSeekOracle/lygo-mint-verifier) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Guidance] <br>
**Output Format:** [Markdown text with optional shell commands and hash values] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Advisory output only; the bundled scripts read local reference files to self-check the pack or display the recorded hash.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

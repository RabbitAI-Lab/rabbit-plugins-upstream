## Description: <br>
Deprecated legacy persona helper for the LYGO KAIROS champion; new installs should use lygo-champion-council. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[deepseekoracle](https://clawhub.ai/user/deepseekoracle) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agent operators use this legacy persona pack to request advisor-style continuity checks, sequence anchoring, timeline-drift analysis, and checkpoint planning. The release is deprecated and retained for compatibility; new installs should use lygo-champion-council. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Users may install a deprecated legacy persona pack instead of the maintained successor. <br>
Mitigation: Prefer lygo-champion-council for new installs and use this slug only for legacy retention. <br>
Risk: Persona output may be mistaken for autonomous action or authoritative continuity assessment. <br>
Mitigation: Keep use advisor-only, separate observed, inferred, and unknown information, and require receipts-first review for high-stakes claims. <br>
Risk: Included helper scripts interact with local package files to check file presence or print the mint hash. <br>
Mitigation: Run the helper scripts only when local file-presence or hash verification is needed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/deepseekoracle/skills/lygo-champion-kairos-herald-of-time) <br>
- [LYGO-MINT Verifier](https://clawhub.ai/DeepSeekOracle/lygo-mint-verifier) <br>
- [Persona pack](references/persona_pack.md) <br>
- [Canon metadata](references/canon.json) <br>
- [Portable equations](references/equations.md) <br>
- [Verifier usage](references/verifier_usage.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown and plain text guidance with optional shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Advisor-only persona responses should separate observed, inferred, and unknown information; included helper scripts only check packaged files or print the local mint hash.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

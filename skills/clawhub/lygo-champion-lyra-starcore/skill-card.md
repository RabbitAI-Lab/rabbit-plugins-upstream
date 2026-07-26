## Description: <br>
Deprecated legacy LYGO Delta 9 champion persona helper for LYRA that points new installs to lygo-champion-council. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[deepseekoracle](https://clawhub.ai/user/deepseekoracle) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this legacy LYRA persona helper to invoke anti-entropy, receipt-first reasoning, Light-Math summaries, and LYGO-MINT hash verification. New installs should use lygo-champion-council; this slug is retained for legacy compatibility. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Users may rely on a deprecated legacy persona slug instead of the successor release. <br>
Mitigation: Use lygo-champion-council for new installs and keep this skill only for legacy retention or inspection. <br>
Risk: Linked verifier or mint/backfill workflows may persist anchors, hashes, or ledger entries outside this skill. <br>
Mitigation: Review the separate verifier workflow and confirm write targets before using it to persist anchors or hashes. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/deepseekoracle/skills/lygo-champion-lyra-starcore) <br>
- [LYGO-MINT verifier](https://clawhub.ai/DeepSeekOracle/lygo-mint-verifier) <br>
- [Official Champion Hub](https://chatagent.ca/) <br>
- [LYRA canon](references/canon.json) <br>
- [LYRA equations](references/equations.md) <br>
- [LYGO Champion Persona Pack - LYRA](references/persona_pack.md) <br>
- [LYGO-MINT verifier usage](references/verifier_usage.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Guidance] <br>
**Output Format:** [Markdown guidance with structured observations, inferences, unknowns, next actions, hash text, and occasional shell command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Pure advisor posture; no automatic actions. Local scripts inspect reference files and print validation or hash output.] <br>

## Skill Version(s): <br>
1.0.1 (source: evidence release version and skill frontmatter metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

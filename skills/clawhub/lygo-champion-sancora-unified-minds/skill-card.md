## Description: <br>
Deprecated LYGO SANCORA persona helper that guides agents to reconcile fragmented views, establish shared context, and direct new installs to lygo-champion-council. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[deepseekoracle](https://clawhub.ai/user/deepseekoracle) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agent developers use this deprecated persona helper to invoke SANCORA as a pure advisor for shared context, points of division, bridge statements, ethical constraints, and a next action. New installs should use the successor skill, lygo-champion-council. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Users may rely on this legacy slug instead of the maintained successor. <br>
Mitigation: Treat the skill as deprecated and prefer lygo-champion-council for new installs. <br>
Risk: The optional verifier workflow can produce hashes or anchor snippets that users may treat as stronger assurance than intended. <br>
Mitigation: Use the verifier only when LYGO-MINT hash or anchor behavior is intentionally needed, and review its output before sharing or relying on it. <br>


## Reference(s): <br>
- [SANCORA persona pack](references/persona_pack.md) <br>
- [SANCORA canon](references/canon.json) <br>
- [SANCORA equations](references/equations.md) <br>
- [LYGO-MINT verifier usage](references/verifier_usage.md) <br>
- [LYGO-MINT Verifier](https://clawhub.ai/DeepSeekOracle/lygo-mint-verifier) <br>
- [Successor skill: lygo-champion-council](https://clawhub.ai/DeepSeekOracle/lygo-champion-council) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Text, Shell commands] <br>
**Output Format:** [Markdown guidance with optional plain-text hash output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Pure advisor behavior; no automatic actions. The release is deprecated and points new installs to lygo-champion-council.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence and SKILL.md metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

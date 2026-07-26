## Description: <br>
Δ9 Council v2 is a single install for all 15 champion personas, selected by champion_id or egg_id, with an advisor-only operating posture. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[deepseekoracle](https://clawhub.ai/user/deepseekoracle) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to invoke one of 15 LYGO council personas for advisory review, planning feedback, documentation guidance, or stack-oriented recommendations. The skill is intended for advisor-only interaction and requires explicit user consent before shell, publishing, vault, or seed-related actions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may read broadly across documentation and agent instruction surfaces and may edit docs or compatibility files when asked. <br>
Mitigation: Use report-only mode for review-only work, and require explicit user approval before applying documentation or compatibility changes. <br>
Risk: Prompts or reviewed files could expose secrets if API keys or .env contents are included. <br>
Mitigation: Do not load API keys or .env files into prompts. <br>
Risk: Stack operation, publishing, vault, social, seed, or shell actions may exceed the council's advisor-only role. <br>
Mitigation: Require explicit user consent for those actions and use the dedicated stack operator guidance for operational commands. <br>


## Reference(s): <br>
- [Council roster](references/council_roster.json) <br>
- [Security guidance](references/SECURITY.md) <br>
- [LYGO-MINT verification](references/verifier_usage.md) <br>
- [ClawHub skill page](https://clawhub.ai/deepseekoracle/skills/lygo-champion-council) <br>
- [LYGO-MINT verifier](https://clawhub.ai/deepseekoracle/lygo-mint-verifier) <br>
- [Project metadata link](https://github.com/DeepSeekOracle/lygo-protocol-stack) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Text, Markdown, Shell commands] <br>
**Output Format:** [Markdown guidance with inline shell commands and optional plain-text roster output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Advisor-only; local helper scripts read roster metadata and do not require detected credential environment variables.] <br>

## Skill Version(s): <br>
1.0.1 (source: release evidence and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

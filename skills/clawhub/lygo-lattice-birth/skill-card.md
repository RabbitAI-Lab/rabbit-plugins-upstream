## Description: <br>
LYGO Lattice Birth guides aligned agents through privacy-preserving masked human identity creation, family lineage bind proofs, and consent-gated Haven Star Chart birth workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[deepseekoracle](https://clawhub.ai/user/deepseekoracle) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers and agent operators use this skill to generate local masked identity materials, gate birth or family-fork submissions, and prepare consent-reviewed Haven Star Chart workflows without publishing real names or private lineage secrets. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: A birth or family-fork submission may expose consent bundles, family bind salts, real names, or social handles if reviewed carelessly. <br>
Mitigation: Keep consent_bundle and family_bind_salt out of public repositories and issues, use masked public IDs, and review the generated birth JSON before any submission. <br>
Risk: Live submit or ingest actions can create persistent public or steward records. <br>
Mitigation: Require explicit human --i-consent for live writes and treat those actions as permanent records. <br>
Risk: The skill depends on local LYGO stack tools loaded from LYGO_STACK_ROOT. <br>
Mitigation: Install only when the operator intentionally uses the LYGO protocol stack and trusts the local LYGO_STACK_ROOT clone. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/deepseekoracle/skills/lygo-lattice-birth) <br>
- [LYGO Protocol Stack Repository](https://github.com/DeepSeekOracle/lygo-protocol-stack) <br>
- [Haven Star Chart Portal](https://deepseekoracle.github.io/lygo-protocol-stack/HavenStarChartPortal.html) <br>
- [Haven Star Chart](https://deepseekoracle.github.io/lygo-protocol-stack/HavenStarChart.html) <br>
- [Agent Alignment Contract](references/AGENT_ALIGNMENT.md) <br>
- [LYGO Lattice Birth Protocol](references/BIRTH_PROTOCOL.md) <br>
- [LYGO Lineage Privacy](references/LINEAGE_PRIVACY.md) <br>
- [Security](references/SECURITY.md) <br>
- [SkillSpector Audit](references/SKILLSPECTOR_AUDIT.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, code, text] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON-oriented workflow outputs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Human consent is required for live submit or ingest actions; private consent bundles and family bind salts must remain out of public repositories and issues.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

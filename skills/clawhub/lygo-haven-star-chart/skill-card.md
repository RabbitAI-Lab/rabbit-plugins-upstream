## Description: <br>
Haven Star Chart v2 portal training helps agents gate, validate, and propose star chart submissions with human consent, local graph and math checks, and immutable feed verification. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[deepseekoracle](https://clawhub.ai/user/deepseekoracle) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and stewards use this skill to prepare Haven Star Chart seal, champion, lattice, portal, or node submissions, validate them against the local LYGO stack, and stop for human approval before any live queue or ledger write. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: A user could point LYGO_STACK_ROOT at an untrusted or modified LYGO stack. <br>
Mitigation: Use only a trusted local lygo-protocol-stack clone, review the security and audit references, and run scripts/self_check.py before stack operations. <br>
Risk: A pending queue or ledger write could be attempted before the user understands the live effect. <br>
Mitigation: Require explicit user approval and --i-consent for submit or ingest commands; agents should prepare and validate submissions but stop before live writes. <br>
Risk: A submission could be represented as live before steward ingest completes. <br>
Mitigation: Report PENDING until steward ingest and feed verification complete, then cite registry SHA and feed entry_hash when available. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/deepseekoracle/skills/lygo-haven-star-chart) <br>
- [Publisher Profile](https://clawhub.ai/user/deepseekoracle) <br>
- [LYGO Protocol Stack](https://github.com/DeepSeekOracle/lygo-protocol-stack) <br>
- [Haven Star Chart](https://deepseekoracle.github.io/lygo-protocol-stack/HavenStarChart.html) <br>
- [Haven Star Chart Agent Portal](https://deepseekoracle.github.io/lygo-protocol-stack/HavenStarChartPortal.html) <br>
- [Agent Contract](references/AGENT_CONTRACT.md) <br>
- [Security Notes](references/SECURITY.md) <br>
- [SkillSpector Audit Response](references/SKILLSPECTOR_AUDIT.md) <br>
- [Submission Training](references/SUBMISSION_TRAINING.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, JSON, Markdown] <br>
**Output Format:** [Markdown guidance with shell commands and JSON validation output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Live submit and ingest actions require explicit human approval and --i-consent; skill scripts perform no direct writes.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

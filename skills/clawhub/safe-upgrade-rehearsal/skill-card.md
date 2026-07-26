## Description: <br>
Dry-run OpenClaw version updates, compare package and runtime evidence, and prepare rollback-aware operator review artifacts without changing a live runtime. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[pdurlej](https://clawhub.ai/user/pdurlej) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to rehearse OpenClaw upgrades, collect package and installation evidence, identify blocked readiness conditions, and draft an operator plan before any live change. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Incorrect package versions or output paths could make the rehearsal evidence misleading. <br>
Mitigation: Review the exact package versions and output directories before running the rehearsal. <br>
Risk: Untrusted local binaries, advisory adapters, or environment variables could affect local execution. <br>
Mitigation: Run only with trusted local python, node, and npm binaries, and configure advisory adapters or environment variables only when those executables are trusted. <br>
Risk: Secrets, private conversations, production logs, or live configuration values could be exposed in review inputs or artifacts. <br>
Mitigation: Use only public-safe, sanitized installation evidence and omit secrets, private conversations, production logs, and raw live configuration values. <br>


## Reference(s): <br>
- [OpenClaw Safe Update homepage](https://github.com/pdurlej/openclaw-skill-safe-update) <br>
- [Evidence Contract](references/evidence-contract.md) <br>
- [Installation Contract](references/installation-contract.md) <br>
- [Safe-update phase handoffs](references/phase-handoffs.md) <br>
- [Benchmark Runner and Reporting](references/benchmark-runner.md) <br>
- [Benchmark Scoring Protocol](references/benchmark-scoring-protocol.md) <br>
- [v1.3 exit decision](references/v1.3-decision.md) <br>
- [Shadow Runs Index](references/shadow-runs-index.json) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, code, markdown, text] <br>
**Output Format:** [Markdown guidance with bash commands, JSON and YAML configuration examples, and review artifact descriptions.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces local dry-run evidence and operator review artifacts; it does not apply updates.] <br>

## Skill Version(s): <br>
1.3.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

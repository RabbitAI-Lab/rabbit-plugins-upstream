## Description: <br>
Database Credential Security (Zero‑Exposure Edition) teaches agents how to manage database credentials with MGC Blackbox while using local scripts for database operations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zkeviny](https://clawhub.ai/user/zkeviny) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this documentation skill to plan database automation that keeps passwords out of agent prompts by storing credentials in MGC and running database work through trusted local scripts. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security review found misleading zero-exposure claims and workflows that can expose credentials or execute database scripts. <br>
Mitigation: Review carefully before installing, use only trusted local MGC tooling, and do not let an AI agent call mgc_get for secrets unless those secrets may enter model context. <br>
Risk: Production database or sealed-script execution can affect sensitive systems. <br>
Mitigation: Require human approval, least-privilege credentials, backups, and script provenance checks before production database or sealed-script execution. <br>
Risk: Credential-handling examples may expose secrets if implemented with direct agent retrieval or unsafe logging. <br>
Mitigation: Keep credential retrieval inside local scripts, avoid printing or logging credential values, and return only non-sensitive results to the agent. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zkeviny/skills/mgc-database-security) <br>
- [Skill documentation](artifact/SKILL.md) <br>
- [Release README](artifact/README.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, code, shell commands, configuration] <br>
**Output Format:** [Markdown documentation with conceptual code and command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [No executable files are included; examples require trusted local MGC tooling and database drivers.] <br>

## Skill Version(s): <br>
1.2.0 (source: server release metadata, artifact frontmatter, manifest) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

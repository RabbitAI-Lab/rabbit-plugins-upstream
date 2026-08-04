## Description: <br>
Audits dependency supply chains for bad versions, lockfile drift, and artifact integrity. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and security engineers use this skill to audit Python dependency supply chains, investigate suspected package compromises, and plan incident response steps for affected environments. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad local scan or forensic commands may inspect more files than intended during incident response. <br>
Mitigation: Prefer project-scoped paths where possible and review commands before execution. <br>
Risk: Environment snapshots collected during triage may contain secrets. <br>
Mitigation: Treat captured environment data as secret material and store or share it only through approved channels. <br>
Risk: Referenced hook or plugin behavior may add persistent per-session dependency checks. <br>
Mitigation: Enable hooks or external plugin behavior only when persistent checks are desired and understood. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-leyline-supply-chain-advisory) <br>
- [OpenClaw homepage metadata](https://github.com/athola/claude-night-market/tree/master/plugins/leyline) <br>
- [Incident Response](modules/incident-response.md) <br>
- [Scanning Patterns](modules/scanning-patterns.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, code, configuration] <br>
**Output Format:** [Markdown guidance with inline shell and Python code examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May recommend project-scoped local scans, dependency exclusions, lockfile regeneration, credential rotation, and optional hook or plugin configuration.] <br>

## Skill Version(s): <br>
1.9.17 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

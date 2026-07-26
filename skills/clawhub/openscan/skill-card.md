## Description: <br>
Scan binaries and scripts for malicious patterns before trusting them. Use when installing skills, evaluating unknown binaries, or auditing tool dependencies. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dev-null321](https://clawhub.ai/user/dev-null321) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agents use OpenScan to inspect local macOS and Linux binaries, scripts, and skill folders before trusting or executing them. It supports pre-install checks, dependency audits, and automated review workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Scan targets may include sensitive local files or broad directory contents. <br>
Mitigation: Review scan paths before execution and avoid broad directory scans unless the scope is intentional. <br>
Risk: Static malware scanning can miss runtime-only behavior, sophisticated obfuscation, or unknown malware. <br>
Mitigation: Use OpenScan as an early screening tool and pair findings with manual review or dedicated security tooling for high-risk files. <br>
Risk: Legitimate security tools, debuggers, or system utilities may trigger suspicious-pattern findings. <br>
Mitigation: Treat non-clean results as review prompts and confirm whether the reported APIs, strings, or entropy are expected for the file. <br>


## Reference(s): <br>
- [OpenScan ClawHub Skill Page](https://clawhub.ai/dev-null321/skills/openscan) <br>
- [Harkonnen Antimalware Engine](https://github.com/dev-null321/Harkonnen) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, JSON, Shell commands, Guidance] <br>
**Output Format:** [Human-readable terminal report or JSON array] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes file hashes, threat score, threat level, findings, and exit code; scans local files up to 50 MB by default.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter, package.json, ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

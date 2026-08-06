## Description: <br>
Skill Security Checker helps agents audit skill directories for static security risks, dependency vulnerabilities, permission overreach, quality issues, optional sandbox behavior, supply-chain findings, and CI/CD report generation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[fyniujin](https://clawhub.ai/user/fyniujin) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, reviewers, and CI maintainers use this skill to scan ClawHub, SkillHub, or WorkBuddy skill directories before release or during pull-request checks. It supports local audits, third-party skill assessment, and automated quality gates with remediation guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can check GitHub for release updates during normal operation. <br>
Mitigation: Use --skip-update in offline or sensitive environments. <br>
Risk: Supply-chain checks may perform external vulnerability or package metadata lookups that reveal dependency names. <br>
Mitigation: Avoid --supply-chain for private dependency names unless those lookups are acceptable. <br>
Risk: Dynamic scanning executes target skill scripts to observe behavior. <br>
Mitigation: Enable --dynamic only when Docker or Windows Sandbox isolation is available; otherwise rely on static and supply-chain scans. <br>
Risk: The tool may create local cache files for update or supply-chain metadata. <br>
Mitigation: Review or clear the local cache when operating in sensitive environments. <br>


## Reference(s): <br>
- [Scan Patterns Reference](references/scan-patterns.md) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Text, JSON, HTML, SARIF, Shell commands, Configuration instructions, Guidance] <br>
**Output Format:** [Text, JSON, HTML, and SARIF reports with scores, findings, exit codes, CI configuration, and remediation guidance.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can write report files via an output path; optional dynamic and supply-chain checks may add runtime behavior and dependency-risk findings.] <br>

## Skill Version(s): <br>
3.0.0 (source: frontmatter, release evidence, artifact metadata, and changelog) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

## Description: <br>
Go安全漏洞扫描免费版 helps individual Go developers use govulncheck to scan known dependency vulnerabilities, assess impact, and identify safer update paths. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to run Go project vulnerability checks before release, before dependency updates, or as part of basic CI security scanning. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Dependency update commands can change go.mod and go.sum. <br>
Mitigation: Run update steps only when intentionally repairing dependencies, keep the project under version control, and review the resulting module changes before committing. <br>
Risk: The skill runs local Go tooling and is scoped to Go vulnerability checks. <br>
Mitigation: Use it only inside Go projects where govulncheck and related Go commands are appropriate; do not invoke it for non-Go security, encryption, or unrelated assessment requests. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/go-security-vuln-tool-free) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, Markdown, JSON] <br>
**Output Format:** [Markdown guidance with bash, YAML, and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces govulncheck-oriented scan guidance, impact summaries, dependency update commands, and CI configuration examples.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

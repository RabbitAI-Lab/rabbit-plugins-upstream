## Description:

Scans C and Python code for security vulnerabilities, dependency risk, and CWE/CVE context, then returns structured findings and remediation guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[a9320](https://clawhub.ai/user/a9320)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and security engineers use this skill to audit local C and Python source trees, inspect dependency exposure, look up related CVEs, and prepare concise vulnerability reports with remediation steps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill needs broad read access to local source trees to scan code.

Mitigation: Install and run it only in workspaces where code scanning is intended, and review requested target paths before execution.

Risk: When AI analysis is enabled, source code may be sent to the configured LLM provider.

Mitigation: Keep AI analysis disabled for private code or configure local inference with CODERISK_LLM_BACKEND=local.

Risk: The supplied security guidance flags SSE mode until the advertised auth middleware is fixed.

Mitigation: Use the default stdio mode and avoid SSE mode unless the deployment has independently validated its authentication behavior.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/a9320/skills/code-risk-agent)
- [Publisher profile](https://clawhub.ai/user/a9320)
- [Server-resolved GitHub import](https://github.com/a9320/code-risk-agent/tree/master/skill)
- [CWE reference](https://cwe.mitre.org/data/definitions/{num}.html)
- [NVD CVE detail](https://nvd.nist.gov/vuln/detail/{cve_id})

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [JSON scan results with Markdown summaries and remediation guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes severity breakdowns, CWE/CVE references, evidence sources, and optional saved report files.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

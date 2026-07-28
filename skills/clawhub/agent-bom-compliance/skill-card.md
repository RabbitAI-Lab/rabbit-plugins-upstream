## Description: <br>
AI compliance and policy engine that evaluates scan results against OWASP, NIST, SOC 2, ISO 27001, CMMC, EU AI Act, AISVS v1.0, and related frameworks, and helps generate SBOMs and compliance reports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[msaad00](https://clawhub.ai/user/msaad00) <br>

### License/Terms of Use: <br>
Apache-2.0 <br>


## Use Case: <br>
Developers, security engineers, and compliance teams use this skill to evaluate AI infrastructure scan results, enforce policy-as-code rules, generate SBOMs, and produce compliance reports. Optional CIS benchmark checks can be run when the operator intentionally uses locally configured cloud credentials for read-only provider API calls. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad activation phrases such as NIST, SOC 2, OWASP, or compliance report may activate the skill when the user did not intend to run compliance tooling. <br>
Mitigation: Confirm the intended compliance, SBOM, policy-as-code, or CIS benchmark task before invoking tools or producing execution steps. <br>
Risk: Optional CIS benchmark checks use locally configured AWS, Azure, GCP, or Snowflake credentials for read-only provider API calls. <br>
Mitigation: Run CIS checks only after explicit user request, rely on operator-configured SDK credentials, and avoid requesting or printing cloud tokens, private keys, passwords, or connection strings. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/msaad00/skills/agent-bom-compliance) <br>
- [agent-bom source repository](https://github.com/msaad00/agent-bom) <br>
- [agent-bom PyPI package](https://pypi.org/project/agent-bom/) <br>
- [OpenSSF Scorecard](https://securityscorecards.dev/viewer/?uri=github.com/msaad00/agent-bom) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline commands and structured compliance guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May reference user-provided SBOM or policy files and may propose optional cloud-provider CIS checks when explicitly requested.] <br>

## Skill Version(s): <br>
0.98.2 (source: frontmatter and release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

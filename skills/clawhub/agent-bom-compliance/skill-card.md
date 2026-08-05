## Description: <br>
AI compliance and policy engine for evaluating scan results against OWASP, NIST, SOC 2, ISO 27001, CMMC, EU AI Act, AISVS v1.0, and related frameworks, while generating SBOMs and compliance reports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[msaad00](https://clawhub.ai/user/msaad00) <br>

### License/Terms of Use: <br>
Apache-2.0 <br>


## Use Case: <br>
Developers, security engineers, and compliance teams use this skill to run AI security and compliance checks, enforce policy-as-code rules, generate CycloneDX or SPDX SBOMs, and prepare compliance reports for supported frameworks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can optionally use local cloud credentials for CIS benchmark checks against AWS, Azure, GCP, or Snowflake. <br>
Mitigation: Use only minimum-scope read-only credentials and invoke CIS benchmark checks only when the cloud account review is intended. <br>
Risk: The release is published by a third party and may be installed from package or source locations outside NVIDIA control. <br>
Mitigation: Verify the agent-bom package or source repository before installation, especially before running checks that can access cloud APIs. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/msaad00/skills/agent-bom-compliance) <br>
- [agent-bom Source Repository](https://github.com/msaad00/agent-bom) <br>
- [agent-bom PyPI Package](https://pypi.org/project/agent-bom/) <br>
- [OpenSSF Scorecard](https://securityscorecards.dev/viewer/?uri=github.com/msaad00/agent-bom) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON outputs for SBOMs, policy checks, and compliance reports] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [OWASP, NIST, EU AI Act, MITRE, AISVS, SBOM, and policy evaluation run locally; optional CIS benchmark checks make read-only cloud provider API calls when explicitly invoked.] <br>

## Skill Version(s): <br>
0.98.3 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

## Description: <br>
AI compliance and policy engine that evaluates scan results against OWASP, NIST, SOC 2, ISO 27001, CMMC, EU AI Act, AISVS v1.0, and related frameworks, and generates SBOMs and compliance reports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[msaad00](https://clawhub.ai/user/msaad00) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, security engineers, and compliance teams use this skill to check AI infrastructure scan results against security and regulatory frameworks, enforce policy-as-code rules, and produce SBOM or compliance-reporting outputs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Optional CIS benchmark checks can query cloud accounts using local cloud credentials. <br>
Mitigation: Run CIS checks only when intended, use least-privilege read-only credentials, and rely on locally configured cloud SDK credentials rather than pasted secrets. <br>
Risk: The installed agent-bom package is an external package source. <br>
Mitigation: Verify that the package source and publisher are trusted before installation. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/msaad00/skills/agent-bom-compliance) <br>
- [Project homepage](https://github.com/msaad00/agent-bom) <br>
- [PyPI package](https://pypi.org/project/agent-bom/) <br>
- [OpenSSF Scorecard](https://securityscorecards.dev/viewer/?uri=github.com/msaad00/agent-bom) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown, text guidance, shell commands, policy configuration examples, and SBOM or compliance report files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can generate CycloneDX or SPDX SBOMs and framework-oriented compliance reports; optional CIS checks may query cloud provider APIs when explicitly invoked.] <br>

## Skill Version(s): <br>
0.98.0 (source: server release and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

## Description: <br>
Discover GCP-hosted AI agent and MCP-relevant assets from the operator's environment, emit canonical agent-bom inventory JSON, and scan it without giving agent-bom long-lived GCP credentials. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[msaad00](https://clawhub.ai/user/msaad00) <br>

### License/Terms of Use: <br>
Apache-2.0 <br>


## Use Case: <br>
Developers and cloud security operators use this skill to inventory approved GCP projects for Vertex AI, Cloud Run, Cloud Functions, GKE, and agentic infrastructure. It helps produce schema-valid agent-bom inventory JSON and optional scan findings while keeping credential use local. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow uses existing GCP credentials and could expose more project inventory than intended if credentials or project scope are too broad. <br>
Mitigation: Use operator-approved projects with scoped, read-only, or short-lived credentials. <br>
Risk: Generated inventory may describe sensitive cloud resources even when credential values are redacted. <br>
Mitigation: Choose the output path yourself and review generated inventory before sharing it. <br>
Risk: Service account keys, OAuth refresh tokens, or bearer tokens could be mishandled if copied into chat or printed. <br>
Mitigation: Keep credential material in the operator environment and do not request, display, or persist secret values. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/msaad00/skills/agent-bom-discover-gcp) <br>
- [agent-bom Repository](https://github.com/msaad00/agent-bom) <br>
- [agent-bom PyPI Project](https://pypi.org/project/agent-bom/) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, JSON, Guidance] <br>
**Output Format:** [Markdown with bash commands and JSON inventory or findings output paths] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Default behavior is discover-only; scan findings are produced only when the operator asks.] <br>

## Skill Version(s): <br>
0.98.2 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

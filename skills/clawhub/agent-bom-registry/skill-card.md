## Description: <br>
MCP server security registry and trust assessment that looks up servers in a 1034-entry metadata registry, runs pre-install marketplace checks, batch fleet risk scoring, skill-file trust assessment, and SAST code scans. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[msaad00](https://clawhub.ai/user/msaad00) <br>

### License/Terms of Use: <br>
Apache-2.0 <br>


## Use Case: <br>
Developers and security engineers use this skill to check MCP server trust, review marketplace packages before installation, score server inventories, assess skill instructions, and run static security scans. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The installed package may not be the intended PyPI or GitHub package. <br>
Mitigation: Verify the package identity and source before installing or trusting scan results. <br>
Risk: Optional vulnerability enrichment requires SNYK_TOKEN and may involve third-party processing. <br>
Mitigation: Provide SNYK_TOKEN only when Snyk enrichment is intended, and keep the token in the operator environment. <br>
Risk: Skill or code contents submitted for optional enrichment may contain sensitive information. <br>
Mitigation: Treat scanned content as sensitive and avoid optional third-party enrichment for material that should remain local. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/msaad00/skills/agent-bom-registry) <br>
- [agent-bom GitHub repository](https://github.com/msaad00/agent-bom) <br>
- [agent-bom PyPI package](https://pypi.org/project/agent-bom/) <br>
- [OpenSSF Scorecard](https://securityscorecards.dev/viewer/?uri=github.com/msaad00/agent-bom) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Guidance] <br>
**Output Format:** [Markdown and structured text with command examples and security findings] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include registry matches, trust assessments, risk scores, SAST findings, and recommended next actions.] <br>

## Skill Version(s): <br>
0.98.3 (source: frontmatter and release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

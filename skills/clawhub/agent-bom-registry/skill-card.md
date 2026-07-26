## Description: <br>
MCP server security registry and trust assessment - look up servers in the 1013-entry server security metadata registry, run pre-install marketplace checks, batch fleet risk scoring, assess skill file trust, and run SAST code scans. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[msaad00](https://clawhub.ai/user/msaad00) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and security reviewers use this skill to evaluate MCP server trust, run pre-install marketplace checks, assess skill files, and perform SAST-oriented code scans before adopting agent tooling. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can run security lookups and scans over MCP servers, skill files, or code, so results may depend on the exact targets selected for analysis. <br>
Mitigation: Keep scans pointed at directories, skill files, and server inventories that the operator intends to analyze, and review findings before using them for deployment decisions. <br>
Risk: Optional Snyk enrichment may contact a third-party vulnerability service when SNYK_TOKEN is provided. <br>
Mitigation: Provide SNYK_TOKEN only when third-party enrichment is desired, and keep the token in the operator environment rather than embedding it in skill output. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/msaad00/skills/agent-bom-registry) <br>
- [Project homepage](https://github.com/msaad00/agent-bom) <br>
- [PyPI project](https://pypi.org/project/agent-bom/) <br>
- [OpenSSF Scorecard](https://securityscorecards.dev/viewer/?uri=github.com/msaad00/agent-bom) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown and plain text with inline shell commands and structured security findings] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May report local registry lookup results, skill trust findings, fleet risk scores, and optional Semgrep or Snyk-enriched scan guidance.] <br>

## Skill Version(s): <br>
0.98.0 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

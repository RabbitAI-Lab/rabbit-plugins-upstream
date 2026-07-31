## Description: <br>
MCP server security registry and trust assessment for looking up servers in a 1013-entry metadata registry, running pre-install marketplace checks, scoring fleet risk, assessing skill file trust, and running SAST code scans. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[msaad00](https://clawhub.ai/user/msaad00) <br>

### License/Terms of Use: <br>
Apache-2.0 <br>


## Use Case: <br>
Developers and security reviewers use this skill to assess MCP server packages, inspect skill files, and run registry-backed trust checks before installation or fleet use. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Optional vulnerability enrichment can contact Snyk and requires a token when enabled. <br>
Mitigation: Use optional Snyk enrichment only when needed, keep SNYK_TOKEN in the operator environment, and do not include secrets in prompts or outputs. <br>
Risk: Registry lookups, SAST findings, and trust assessments can be incomplete or produce false positives. <br>
Mitigation: Review findings before acting on them, verify the PyPI or GitHub package source, and combine the results with normal security review before installation or deployment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/msaad00/skills/agent-bom-registry) <br>
- [agent-bom source](https://github.com/msaad00/agent-bom) <br>
- [agent-bom PyPI package](https://pypi.org/project/agent-bom/) <br>
- [OpenSSF Scorecard](https://securityscorecards.dev/viewer/?uri=github.com/msaad00/agent-bom) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Guidance] <br>
**Output Format:** [Markdown and text guidance with tool-call examples and shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include local registry results and optional Snyk enrichment when configured.] <br>

## Skill Version(s): <br>
0.98.2 (source: SKILL.md frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

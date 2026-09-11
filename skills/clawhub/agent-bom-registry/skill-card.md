## Description:

MCP server security registry and trust assessment for looking up server metadata, running pre-install marketplace checks, batch fleet risk scoring, skill trust assessment, and SAST code scans.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers and engineers use this skill to assess MCP server and skill trust before installation or deployment, run registry lookups, score MCP server inventories, and request SAST scans.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing without a version pin could pull a package version other than the reviewed 0.104.0 release.

Mitigation: Pin agent-bom to version 0.104.0 when installing or approving the skill for a controlled environment.

Risk: Optional Snyk enrichment uses SNYK_TOKEN and contacts the Snyk API when intentionally enabled.

Mitigation: Provide SNYK_TOKEN only when Snyk enrichment is needed, keep it in the operator environment, and avoid exposing it in prompts or outputs.

Risk: Scan outputs are meaningful only for files, repositories, or MCP server inventories the operator intended to analyze.

Mitigation: Run scans only on intended inputs and review findings before acting on deployment or installation decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/msaad00/skills/agent-bom-registry)
- [Project homepage](https://github.com/msaad00/agent-bom)
- [Source repository](https://github.com/msaad00/agent-bom)
- [PyPI package](https://pypi.org/project/agent-bom/)
- [OpenSSF Scorecard](https://securityscorecards.dev/viewer/?uri=github.com/msaad00/agent-bom)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown and text with inline shell commands, code snippets, and structured scan guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces registry lookups, trust assessments, fleet risk scoring, and SAST-oriented findings for agent workflows.]

## Skill Version(s):

0.104.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

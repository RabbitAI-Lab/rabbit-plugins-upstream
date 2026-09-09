## Description:

MCP server security registry and trust assessment - look up servers in the 1123-entry server security metadata registry, run pre-install marketplace checks, batch fleet risk scoring, assess skill file trust, and run SAST code scans.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers and engineers use this skill to assess MCP server trust, check marketplace packages before installation, score MCP server inventories, evaluate skill files, and run optional SAST scans.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Code and skill scanning requires the operator to point the tool at files or directories.

Mitigation: Scan only intended paths and review findings before using the results to make installation or deployment decisions.

Risk: Optional Snyk enrichment sends requests to a third-party service and requires SNYK_TOKEN.

Mitigation: Use Snyk enrichment only when approved for the environment, keep the token in the operator environment, and avoid including it in prompts, files, or output.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/msaad00/skills/agent-bom-registry)
- [Source repository](https://github.com/msaad00/agent-bom)
- [PyPI package](https://pypi.org/project/agent-bom/)
- [OpenSSF Scorecard](https://securityscorecards.dev/viewer/?uri=github.com/msaad00/agent-bom)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and text with inline shell commands and structured scan findings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Registry lookup data is bundled locally; optional code scanning may use Semgrep, and optional Snyk enrichment requires SNYK_TOKEN.]

## Skill Version(s):

0.103.2 (source: artifact/SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

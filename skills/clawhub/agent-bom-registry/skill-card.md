## Description:

MCP server security registry and trust assessment - look up servers in the 1099-entry server security metadata registry, run pre-install marketplace checks, batch fleet risk scoring, assess skill file trust, and run SAST code scans.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers and engineers use this skill to evaluate MCP server trust, check marketplace packages before installation, score server inventories, assess skill files, and run optional SAST scans.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Scanner workflows can read files from paths provided by the operator.

Mitigation: Run scans only on intended directories and review selected paths before invoking file or skill analysis.

Risk: Optional Snyk enrichment can use a token and make network calls.

Mitigation: Keep SNYK_TOKEN in the operator environment, do not paste tokens into prompts, and enable enrichment only when network use is intended.

## Reference(s):

- [agent-bom source](https://github.com/msaad00/agent-bom)
- [agent-bom on PyPI](https://pypi.org/project/agent-bom/)
- [OpenSSF Scorecard](https://securityscorecards.dev/viewer/?uri=github.com/msaad00/agent-bom)
- [ClawHub skill page](https://clawhub.ai/msaad00/skills/agent-bom-registry)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown with inline shell commands and structured security findings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include local registry lookup results, trust assessments, fleet risk scores, skill scan findings, and optional SAST findings.]

## Skill Version(s):

0.102.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

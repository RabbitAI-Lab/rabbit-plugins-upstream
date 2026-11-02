## Description:

MCP server security registry and trust assessment — look up servers in the 1256-entry server security metadata registry, run pre-install marketplace checks, batch fleet risk scoring, assess skill file trust, and run SAST code scans. Use when the user mentions MCP server trust, registry lookup, marketplace check, or skill trust assessment.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and security teams can use the skill to look up MCP server trust data, check packages before installation, score server inventories, assess skill file trust, and review code with SAST scans.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The supplied instruction review does not certify the downloaded package or guarantee that every command runs offline.

Mitigation: Install with pipx and review or pin the package version before use.

Risk: Code scans can involve optional third-party vulnerability enrichment.

Mitigation: Limit scans to intended files and enable Snyk enrichment only when wanted; keep its token in the operator environment.

## Reference(s):

- [Agent-BOM project](https://github.com/koda-ai-studio/agent-bom)
- [PyPI package](https://pypi.org/project/agent-bom/)
- [OpenSSF Scorecard](https://securityscorecards.dev/viewer/?uri=github.com/koda-ai-studio/agent-bom)
- [ClawHub release page](https://clawhub.ai/msaad00/skills/agent-bom-registry)

## Skill Output:

**Output Type(s):** [Analysis, Text, Guidance]

**Output Format:** [Text summaries and security findings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on the requested lookup or scan; optional Snyk enrichment requires an operator-provided token.]

## Skill Version(s):

0.112.1 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

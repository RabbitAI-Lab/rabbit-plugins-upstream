## Description:

MCP server security registry and trust assessment — look up servers in the 1256-entry server security metadata registry, run pre-install marketplace checks, batch fleet risk scoring, assess skill file trust, and run SAST code scans.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and security engineers use this skill to look up MCP servers, assess packages before installation, score server inventories, review skill files, and scan code for security issues.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional Snyk enrichment for code scans contacts an external service and requires SNYK_TOKEN.

Mitigation: Enable enrichment only when needed, keep the token in the operator environment, and review external data handling first.

Risk: Scans and trust assessments process the selected folders or supplied skill content.

Mitigation: Choose a trusted package version, limit scans to intended folders, and review results before acting on them.

## Reference(s):

- [Project homepage](https://github.com/koda-ai-studio/agent-bom)
- [PyPI package](https://pypi.org/project/agent-bom/)
- [OpenSSF Scorecard](https://securityscorecards.dev/viewer/?uri=github.com/koda-ai-studio/agent-bom)
- [ClawHub skill page](https://clawhub.ai/msaad00/skills/agent-bom-registry)

## Skill Output:

**Output Type(s):** [Analysis, Text, Guidance]

**Output Format:** [Registry lookup results and security assessment summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include registry matches, risk scores, trust findings, or SAST findings, depending on the selected servers, files, or code.]

## Skill Version(s):

0.111.0 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

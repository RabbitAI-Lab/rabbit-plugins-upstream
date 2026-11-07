## Description:

MCP server security registry and trust assessment — look up servers in the 1295-entry server security metadata registry, run pre-install marketplace checks, batch fleet risk scoring, assess skill file trust, and run SAST code scans.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

Apache 2.0

## Use Case:

Developers and security teams use the registry to review MCP servers before installation, assess skill-file trust, score server inventories, and run code security scans.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional Snyk enrichment sends vulnerability scan requests to an external service and uses SNYK_TOKEN.

Mitigation: Enable enrichment only when intended and keep the token in the operator environment.

Risk: The separately downloaded runtime package was not audited with the supplied skill instructions.

Mitigation: Use pipx with a verified, pinned package version and select the intended scan directory.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/msaad00/skills/agent-bom-registry)
- [Agent-BOM project homepage](https://github.com/koda-ai-studio/agent-bom)
- [Agent-BOM on PyPI](https://pypi.org/project/agent-bom/)
- [OpenSSF Scorecard](https://securityscorecards.dev/viewer/?uri=github.com/koda-ai-studio/agent-bom)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Text, Markdown]

**Output Format:** [Text or Markdown summaries of registry matches, trust assessments, risk scores, and scan findings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on the selected registry or assessment tool.]

## Skill Version(s):

0.113.2 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

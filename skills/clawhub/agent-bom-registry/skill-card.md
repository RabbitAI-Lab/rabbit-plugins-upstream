## Description:

MCP server security registry and trust assessment — look up servers in the 1356-entry server security metadata registry, run pre-install marketplace checks, batch fleet risk scoring, assess skill file trust, and run SAST code scans. Use when the user mentions MCP server trust, registry lookup, marketplace check, or skill trust assessment.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers and security teams use this skill to look up MCP server security metadata, assess marketplace candidates and instruction files, score server inventories, and review code scan findings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional Snyk enrichment for code scans uses the SNYK_TOKEN to contact the Snyk API.

Mitigation: Keep the optional token in the operator environment and out of prompts and skill output.

Risk: A benign scan result does not guarantee that the skill is risk-free.

Mitigation: Review the skill and its scan coverage before relying on the results.

## Reference(s):

- [agent-bom source repository](https://github.com/koda-ai-studio/agent-bom)
- [agent-bom on PyPI](https://pypi.org/project/agent-bom/)
- [OpenSSF Scorecard](https://securityscorecards.dev/viewer/?uri=github.com/koda-ai-studio/agent-bom)

## Skill Output:

**Output Type(s):** [Text, Analysis, Guidance]

**Output Format:** [Text reports with registry matches, trust assessments, and scan findings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on the queried server, supplied skill content, and available scan tools.]

## Skill Version(s):

0.115.4 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

MCP server security registry and trust assessment — look up servers in the 1256-entry server security metadata registry, run pre-install marketplace checks, batch fleet risk scoring, assess skill file trust, and run SAST code scans. Use when the user mentions MCP server trust, registry lookup, marketplace check, or skill trust assessment.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and security engineers use this skill to check MCP server metadata before installation, assess skill-file trust, score server inventories, and run code scans.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad scans may inspect files outside the intended scope.

Mitigation: Limit scans to the files and directories intended for review.

Risk: Optional Snyk enrichment makes an external request and requires SNYK_TOKEN.

Mitigation: Review the optional Snyk request before enabling enrichment and keep the token in the operator environment.

Risk: Package changes may alter the behavior of security checks.

Mitigation: Pin the agent-bom package version used for checks.

## Reference(s):

- [Project homepage](https://github.com/msaad00/agent-bom)
- [PyPI package](https://pypi.org/project/agent-bom/)
- [OpenSSF Scorecard](https://securityscorecards.dev/viewer/?uri=github.com/msaad00/agent-bom)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Shell commands, Configuration instructions]

**Output Format:** [Text and Markdown, with shell command examples where useful]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on the requested lookup or scan; optional Snyk enrichment may contact api.snyk.io.]

## Skill Version(s):

0.110.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

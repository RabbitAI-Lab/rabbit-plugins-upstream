## Description:

MCP server security registry and trust assessment: look up servers in the 1142-entry server security metadata registry, run pre-install marketplace checks, batch fleet risk scoring, assess skill file trust, and run SAST code scans.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and security reviewers use this skill to check MCP server trust signals, evaluate marketplace packages before installation, scan fleets of MCP servers, assess skill files, and run optional static code analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional code scanning or Snyk enrichment may share scan metadata with Snyk when enabled.

Mitigation: Confirm the operator is comfortable with that sharing before enrichment, and keep SNYK_TOKEN in the environment rather than prompts or outputs.

Risk: Skill trust analysis depends on user-provided SKILL.md content and registry metadata.

Mitigation: Review analysis results before deployment and use the bundled security guidance as decision support rather than automatic approval.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/msaad00/skills/agent-bom-registry)
- [Project homepage](https://github.com/msaad00/agent-bom)
- [PyPI package](https://pypi.org/project/agent-bom/)
- [OpenSSF Scorecard](https://securityscorecards.dev/viewer/?uri=github.com/msaad00/agent-bom)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and structured analysis]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include registry lookup results, trust assessments, risk scoring, SAST findings, and installation or configuration guidance.]

## Skill Version(s):

0.105.0 (source: server release metadata and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

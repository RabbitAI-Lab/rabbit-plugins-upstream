## Description:

Discover AWS-hosted AI agent and MCP-relevant assets, emit canonical inventory JSON, and optionally scan that inventory locally.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers and cloud operators use this skill to inventory AWS-hosted AI agents and workloads as canonical JSON. They can then choose to scan that inventory locally with agent-bom.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review reported medium confidence because reference resolution was partial and noted an excessive-agency alert.

Mitigation: Review referenced material and confirm the workflow scope before use; follow the skill's guidance to use read-only, short-lived AWS credentials.

## Reference(s):

- [Project homepage](https://github.com/koda-ai-studio/agent-bom)
- [agent-bom on PyPI](https://pypi.org/project/agent-bom/)

## Skill Output:

**Output Type(s):** [JSON, Files]

**Output Format:** [Canonical agent-bom inventory JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes to an operator-selected path; discovery-only by default, with scanning or export only when explicitly requested.]

## Skill Version(s):

0.115.5 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

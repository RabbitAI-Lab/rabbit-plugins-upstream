## Description:

Discover GCP-hosted AI agent and MCP-relevant assets from the operator's environment, emit canonical agent-bom inventory JSON, and scan it without giving agent-bom long-lived GCP credentials.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers and cloud security engineers use this skill to inventory approved GCP projects for Vertex AI, Cloud Run, Cloud Functions, GKE, and related agentic infrastructure. It produces canonical agent-bom inventory for local review and optional scanning.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can use existing local GCP credentials to enumerate approved projects.

Mitigation: Run it only with scoped read-only credentials for operator-approved projects.

Risk: Generated inventory may contain sensitive details about cloud resources.

Mitigation: Write inventory only to an operator-selected local path and review it before sharing or scanning.

Risk: The workflow depends on the agent-bom package and adapter script used in the operator environment.

Mitigation: Verify the installed package and adapter source before execution.

## Reference(s):

- [agent-bom source repository](https://github.com/msaad00/agent-bom)
- [agent-bom PyPI package](https://pypi.org/project/agent-bom/)
- [ClawHub skill page](https://clawhub.ai/msaad00/skills/agent-bom-discover-gcp)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash commands and JSON inventory outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes canonical inventory JSON to an operator-selected path and can optionally produce JSON scan findings.]

## Skill Version(s):

0.105.0 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

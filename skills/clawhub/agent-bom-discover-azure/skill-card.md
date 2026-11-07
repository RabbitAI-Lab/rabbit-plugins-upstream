## Description:

Discover Azure-hosted AI agent and MCP-relevant assets from the operator's environment, emit canonical agent-bom inventory JSON, and scan it without giving agent-bom long-lived Azure credentials.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers and cloud security engineers use this skill to inventory Azure AI and workload resources into canonical agent-bom JSON. They can request an optional local scan of that inventory for findings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow references an Azure inventory adapter that is absent from this package, so its API calls and credential redaction have not been verified.

Mitigation: Obtain and review the adapter from a trusted source before running it. Use a read-only identity limited to approved subscriptions and protect the generated inventory.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/msaad00/skills/agent-bom-discover-azure)
- [agent-bom on PyPI](https://pypi.org/project/agent-bom/)

## Skill Output:

**Output Type(s):** [JSON, Files, Shell commands]

**Output Format:** [Canonical agent-bom inventory JSON file; optional JSON scan findings file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes to an operator-selected path; scanning is optional and requires an explicit request.]

## Skill Version(s):

0.113.2 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

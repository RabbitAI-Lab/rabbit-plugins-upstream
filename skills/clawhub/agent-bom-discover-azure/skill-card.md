## Description:

Discovers Azure-hosted AI and MCP-relevant assets, writes canonical agent-bom inventory JSON, and scans it without giving agent-bom long-lived Azure credentials.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers and cloud security engineers use this skill to inventory Azure OpenAI and agentic workloads in approved subscriptions, save canonical JSON locally, and optionally scan it when requested.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The referenced Azure discovery adapter is absent from this package, so its credential handling and redaction could not be checked.

Mitigation: Obtain and review the adapter from a trusted source before running it, and use a read-only identity scoped to the intended subscription.

Risk: Azure inventory may contain sensitive environment details.

Mitigation: Choose the output location and inspect the inventory before sharing it.

## Reference(s):

- [agent-bom project](https://github.com/koda-ai-studio/agent-bom)
- [agent-bom on PyPI](https://pypi.org/project/agent-bom/)

## Skill Output:

**Output Type(s):** [JSON, Files]

**Output Format:** [Canonical JSON inventory; optional JSON scan findings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses an operator-selected subscription and output path; discovery is read-only, and scanning runs only when requested.]

## Skill Version(s):

0.112.1 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

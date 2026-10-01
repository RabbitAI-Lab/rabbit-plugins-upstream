## Description:

Discovers Azure-hosted AI and agent-related assets using an operator-approved read-only identity and produces canonical agent-bom inventory JSON, with optional inventory scanning on request.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operators use this skill to inventory AI-related resources in approved Azure subscriptions. They can optionally scan the resulting inventory for findings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Azure inventory access through the operator's local identity may expose resources beyond the intended scope.

Mitigation: Use a narrowly scoped read-only identity and approve only the subscriptions to inventory.

Risk: Inventory files can reveal details of the operator's Azure environment.

Mitigation: Choose the output path deliberately and review inventory before sharing or scanning it.

Risk: The external agent-bom runtime adapter executes in the operator's environment.

Mitigation: Review the external package or repository code before relying on the adapter.

## Reference(s):

- [Agent-bom project homepage (listed in skill metadata)](https://github.com/msaad00/agent-bom)
- [Agent-bom package on PyPI](https://pypi.org/project/agent-bom/)

## Skill Output:

**Output Type(s):** [JSON inventory file, JSON scan findings, Shell commands, Guidance]

**Output Format:** [Canonical inventory JSON; optional findings JSON and Markdown instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Discovery writes to an operator-selected path; scanning is optional and requires an explicit request.]

## Skill Version(s):

0.107.0 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

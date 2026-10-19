## Description:

Discovers GCP-hosted AI and workload assets in approved projects and produces canonical agent-bom inventory JSON for optional scanning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operators inventory AI and workload assets in approved GCP projects using read-only credentials, then optionally request a scan of the resulting inventory.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: GCP discovery uses local credentials and may collect information about unapproved projects.

Mitigation: Use narrowly scoped, read-only credentials and inventory only operator-approved projects; never share credential values.

Risk: Generated inventory may contain sensitive asset details.

Mitigation: Review inventory JSON before sharing it and write it only to an operator-selected path.

Risk: The executable discovery adapter is not bundled with this skill artifact.

Mitigation: Verify the external agent-bom package or repository source before running the adapter.

## Reference(s):

- [Project page (declared in skill metadata)](https://github.com/msaad00/agent-bom)
- [agent-bom package (declared in skill metadata)](https://pypi.org/project/agent-bom/)

## Skill Output:

**Output Type(s):** [Shell commands, Files, Guidance]

**Output Format:** [JSON inventory file; optional JSON scan findings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Inventory is written to an operator-selected path; scanning requires an explicit request.]

## Skill Version(s):

0.109.0 (source: frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

A local MCP and CLI bus that shares project state and CAD contracts between cad-file-reader and five quantity-surveying skills, allowing them to reuse one drawing parse.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lisong2003-lgtm](https://clawhub.ai/user/lisong2003-lgtm)

### License/Terms of Use:

MIT

## Use Case:

Developers and quantity-surveying teams use it to install a local bridge between cad-file-reader and the supported estimating skills. The bridge shares project state and CAD contracts so downstream skills can reuse the existing parse.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Contract lookup can fall back to a filename match even when a supplied source hash conflicts, so results from another drawing may reach construction estimates.

Mitigation: Reject conflicting hashes before relying on cached estimates, verify each reused contract belongs to the intended drawing, and evaluate with a separate local state directory.

Risk: Uninstallation leaves local bus data behind, and validation by separately installed companion skills has not been verified.

Mitigation: Review MCP registration changes and retain backups; check that each receiving skill validates the contract and drawing identity before using it for estimates.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/lisong2003-lgtm/skills/lis-skill-bus)

## Skill Output:

**Output Type(s):** [JSON, Configuration instructions, Shell commands]

**Output Format:** [JSON project state and CAD contract responses, with CLI/MCP setup guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Project, building, floor, contract type, and source identifiers vary by integration.]

## Skill Version(s):

0.1.9 (source: frontmatter, server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

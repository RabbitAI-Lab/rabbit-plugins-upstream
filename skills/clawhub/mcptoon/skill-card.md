## Description:

Guides agents in using mcptoon to reduce MCP tool-catalog and result overhead while managing tool and skill access.

This skill is ready for commercial/non-commercial use.

## Publisher:

[activeing123](https://clawhub.ai/user/activeing123)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other agent users use this skill to find and call MCP tools with smaller catalogs, manage skills across agents, and recover original tool results when compression obscures details.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Gateway setup can change agent MCP configuration and route existing tool calls through mcptoon.

Mitigation: Review changes before takeover with a dry run and use mcptoon restore to undo configuration changes.

Risk: Compressed tool results can omit details needed to assess an answer; originals are stored for later retrieval.

Mitigation: Retrieve the original result by handle, or turn compression off for a tool or the whole session when exact output matters.

Risk: Installing or upgrading the CLI can introduce an unreviewed package version or publisher.

Mitigation: Verify the package publisher and installation source, and pin a reviewed version when reproducibility matters.

## Reference(s):


## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes commands for inspecting tools, adjusting compression and exposure, and restoring configuration.]

## Skill Version(s):

1.0.10 (source: ClawHub release metadata; skill frontmatter lists 1.2.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

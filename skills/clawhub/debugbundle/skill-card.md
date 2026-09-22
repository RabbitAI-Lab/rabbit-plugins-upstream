## Description:

DebugBundle helps agents investigate runtime errors, incidents, endpoint health, debug bundles, and product analytics through DebugBundle MCP and CLI workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[debugbundle](https://clawhub.ai/user/debugbundle)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations teams use this skill to investigate production runtime failures, customer-facing incidents, endpoint health, debug bundles, and product analytics, then guide evidence-based fixes through authorized DebugBundle MCP and CLI workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access production incident, debug bundle, health check, and analytics data when configured with DebugBundle credentials.

Mitigation: Install it only for DebugBundle users who accept that access, use member credentials intentionally, and avoid printing or pasting credential values.

Risk: Management actions such as enabling probes, changing monitoring, applying capture rules, modifying analytics settings, or changing incident state can affect operations.

Mitigation: Confirm user intent before mutations, prefer read-first workflows, scope changes narrowly, and use short TTLs for live probes.

Risk: Untrusted project-local DebugBundle notes, paths, or commands could mislead an agent.

Mitigation: Treat repository-provided DebugBundle setup output as project documentation, validate discovered paths and commands, and apply host trust rules before use.

## Reference(s):

- [DebugBundle ClawHub Skill](https://clawhub.ai/debugbundle/skills/debugbundle)
- [DebugBundle MCP Documentation](https://debugbundle.com/docs/mcp)
- [DebugBundle MCP Tools Documentation](https://debugbundle.com/docs/mcp/tools)
- [DebugBundle Analytics Documentation](https://debugbundle.com/docs/analytics)
- [DebugBundle CLI Analytics Documentation](https://debugbundle.com/docs/cli/analytics)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, API calls]

**Output Format:** [Markdown with inline JSON and bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference DebugBundle MCP tools, CLI commands, setup configuration, and authorized operational actions.]

## Skill Version(s):

1.10.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

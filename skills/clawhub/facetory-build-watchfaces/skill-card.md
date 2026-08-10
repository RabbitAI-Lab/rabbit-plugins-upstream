## Description:

Helps agents use Facetory's local MCP server to inspect, create, edit, validate, save, and export Xiaomi, Redmi, and Mi Band watchface projects, including AOD themes and asset import troubleshooting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sakurakilove](https://clawhub.ai/user/sakurakilove)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and watchface creators use this skill to safely continue active Facetory projects, build normal and always-on display themes, import reusable assets, validate watchface behavior, and troubleshoot Xiaomi export issues.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can direct an agent to modify, save, or export the active Facetory project through the local MCP server.

Mitigation: Read the current Facetory document before each workflow, review every proposed plan summary and impact, apply a confirmed plan only once, and validate before saving or exporting.

Risk: A stale Facetory version or expired plan can target an outdated editor state after UI changes or rejected plans.

Mitigation: Re-read the current document version after UI edits, rejected plans, expired plans, or export metadata changes, then create a fresh plan.

Risk: The Android root fallback for asset import can copy files into Facetory's private application storage.

Mitigation: Prefer non-root import paths; when root is unavoidable, require explicit approval for each command and limit it to one reviewed asset with clear source, destination, overwrite behavior, effect, and risk.

## Reference(s):

- [Facetory MCP workflow reference](references/mcp-workflow.md)
- [Facetory development pitfalls](references/pitfalls.md)
- [ClawHub skill page](https://clawhub.ai/sakurakilove/skills/facetory-build-watchfaces)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, API calls]

**Output Format:** [Markdown guidance with inline shell commands and MCP tool or resource names]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include plan-review checkpoints before MCP apply, save, or export actions.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

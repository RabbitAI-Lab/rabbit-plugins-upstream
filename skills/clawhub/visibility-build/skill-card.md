## Description:

Build the one missing asset that unlocks the most listings for a project - a remote MCP server, server.json, a one-job browser extension, an API-wrapper CLI, an OpenAPI file, llms.txt docs - or a platform's own integration (n8n node, Make app, Notion connection), from a short recipe sourced from the platform's docs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[orensegal](https://clawhub.ai/user/orensegal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to choose and build a useful project asset or platform integration from a recipe, helping their product meet platform listing requirements.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Recipes using unpinned `npx` commands may run changing package versions.

Mitigation: Review and fix package versions before running them, and use an isolated environment without production credentials.

Risk: Zapier test actions may modify live records.

Mitigation: Use synthetic data with isolated integrations for testing.

Risk: The security scan is partial because a local path-like reference could not be resolved.

Mitigation: Review the unresolved reference and treat the security assessment as incomplete until the source has been checked.

## Reference(s):

- [Visibility project homepage](https://github.com/OrenSegal/visibility)
- [ClawHub skill release](https://clawhub.ai/orensegal/skills/visibility-build)

## Skill Output:

**Output Type(s):** [Code, Configuration, Markdown, Shell commands, Guidance]

**Output Format:** [Recipe-specific project files and concise setup or verification guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Varies with the selected asset or platform integration.]

## Skill Version(s):

1.0.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

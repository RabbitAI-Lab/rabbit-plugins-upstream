## Description:

Helps agents define, inspect, and manage saved audience segments and filters in a Cargo workspace.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and workspace operators use this skill to preview audiences, save filters as segments, inspect membership and changes, and prepare segments for downstream workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Cargo CLI actions can read, create, update, delete, or export workspace audience data.

Mitigation: Use the CLI only when the package is trusted, confirm the active workspace, and review changes before update or removal.

Risk: Download links can expose sensitive customer or business data.

Mitigation: Treat signed download URLs and exported audience data as sensitive and share them only with authorized recipients.

## Reference(s):

- [Cargo Segmentation on ClawHub](https://clawhub.ai/cargo-ai/skills/cargo-segmentation)
- [Cargo Skills homepage](https://github.com/getcargohq/cargo-skills)
- [Segmentation response shapes](references/response-shapes.md)
- [Segmentation troubleshooting](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, JSON filter configuration]

**Output Format:** [Markdown with CLI commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Cargo CLI responses are JSON; downloads may return signed URLs.]

## Skill Version(s):

1.1.0 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

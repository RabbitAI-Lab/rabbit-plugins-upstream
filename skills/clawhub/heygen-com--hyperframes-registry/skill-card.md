## Description:

Install, discover, and wire HyperFrames registry blocks and components, and guide authors through contributing new registry items.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and video composition authors use this skill to search the HyperFrames catalog, install blocks or components into a project, wire them into host compositions, and author validated registry contributions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The HyperFrames add workflow writes files into the user's project and fetches registry content over the network.

Mitigation: Review generated HTML and changed project files before shipping, then run the documented lint, check, preview, or snapshot steps as appropriate.

Risk: Runtime CDN dependencies and network registry fetches can affect production reliability or offline installs.

Mitigation: Consider vendoring or lockfile-managed dependencies for production, verify network access before installs, and use cached catalog results only for discovery when offline.

Risk: The feedback command can send search-miss and wanted-effect details outside the local project.

Mitigation: Avoid confidential brief details in feedback reports unless the user is comfortable sending them.

## Reference(s):

- [HyperFrames Registry Skill](SKILL.md)
- [Install Locations](references/install-locations.md)
- [Registry Discovery](references/discovery.md)
- [Wiring Blocks](references/wiring-blocks.md)
- [Wiring Components](references/wiring-components.md)
- [Contributing a Block or Component](references/contributing.md)
- [Component Quality Bar](references/component-quality-bar.md)
- [Contribute Templates](references/templates.md)
- [HyperFrames Registry Manifest](https://raw.githubusercontent.com/heygen-com/hyperframes/main/registry/registry.json)
- [hyperframes.json Schema](https://hyperframes.heygen.com/schema/hyperframes.json)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown guidance with inline shell commands, JSON, HTML, CSS, and JavaScript snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose project file writes through HyperFrames CLI workflows; generated files should be reviewed before shipping.]

## Skill Version(s):

1.0.6 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

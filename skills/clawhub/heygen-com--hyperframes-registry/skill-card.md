## Description: <br>
Install, discover, and wire HyperFrames registry blocks and components into compositions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[heygen-com](https://clawhub.ai/user/heygen-com) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and video engineers use this skill to discover HyperFrames registry items, install blocks or components, wire them into host compositions, and author new registry contributions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Preview, publish, or upload commands can send project material to an unintended destination. <br>
Mitigation: Review the project for secrets or private assets and confirm the destination before running publish or upload commands. <br>
Risk: CDN dependencies in HTML templates can change or load third-party code in production. <br>
Mitigation: Vendor or integrity-pin CDN dependencies before using generated templates in production. <br>
Risk: Manual wiring of blocks and components can introduce incorrect composition IDs, timing, paths, or layering. <br>
Mitigation: Review installed files and run the documented HyperFrames lint, check, and preview commands before deployment. <br>


## Reference(s): <br>
- [Install Locations](references/install-locations.md) <br>
- [Registry Discovery](references/discovery.md) <br>
- [Wiring Blocks](references/wiring-blocks.md) <br>
- [Wiring Components](references/wiring-components.md) <br>
- [Contributing a Block or Component to the Registry](references/contributing.md) <br>
- [Contribute Templates](references/templates.md) <br>
- [HyperFrames Registry Manifest](https://raw.githubusercontent.com/heygen-com/hyperframes/main/registry/registry.json) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Code, Configuration] <br>
**Output Format:** [Markdown with shell, HTML, CSS, JavaScript, and JSON snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose HyperFrames CLI commands and project file edits for registry installation, wiring, validation, preview, and publishing workflows.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

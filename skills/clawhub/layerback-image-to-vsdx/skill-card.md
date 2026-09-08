## Description:

Convert diagram images into fully editable Visio VSDX files with the official LayerBack web app and API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[toplocalai](https://clawhub.ai/user/toplocalai)

### License/Terms of Use:

MIT

## Use Case:

Developers, engineers, analysts, and operations teams use this skill to convert diagram screenshots, exports, flowcharts, architecture diagrams, UML, ER diagrams, organization charts, network diagrams, and whiteboard photos into editable Visio files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Converting a diagram uploads the selected image to LayerBack.

Mitigation: Confirm the file is not confidential or sensitive and get explicit user authorization before upload.

Risk: The direct API workflow requires a LayerBack API key.

Mitigation: Keep the key in the local environment and do not paste it into chat, prompts, committed files, logs, or packaged skill files.

Risk: The release includes an installer command that fetches a package at install time.

Mitigation: Consider pinning or verifying the installer command before global installation.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/toplocalai/skills/layerback-image-to-vsdx)
- [LayerBack Image to Visio](https://layerback.com/image-to-visio)
- [LayerBack Online Converter](https://layerback.com/convert)
- [LayerBack API Documentation](https://layerback.com/docs/api)
- [LayerBack OpenAPI Specification](https://layerback.com/openapi.yaml)
- [LayerBack MCP Repository](https://github.com/TopLocalAI/layerback-mcp)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, files]

**Output Format:** [Markdown with inline shell commands and file paths]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Primary conversion output is VSDX; the LayerBack API can also return PPTX, draw.io, SVG, IR, and preview files.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

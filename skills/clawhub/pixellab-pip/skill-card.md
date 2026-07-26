## Description: <br>
PixelLab Pip helps agents set up PixelLab access, choose MCP or REST workflows, generate and edit pixel-art assets, animations, tilesets, UI, icons, and record reproducible blueprints while respecting credential, cost, and destructive-action safeguards. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[shilo](https://clawhub.ai/user/shilo) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, game creators, and agent users use this skill to configure PixelLab integrations and drive PixelLab asset workflows from setup through generation, editing, animation, packaging, and troubleshooting. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Live PixelLab generation sends prompts and images to PixelLab and may spend credits. <br>
Mitigation: Review the request before starting paid work, use the skill's cost-routing guidance for budget-sensitive tasks, and ask before extra paid attempts unless the user approved a concrete budget or attempt count. <br>
Risk: PIXELLAB_SECRET is a bearer token used for live PixelLab API or MCP calls. <br>
Mitigation: Store the token in a local secret store or environment variable, never paste it into chat, and use it only as an authorization header. <br>
Risk: Generated outputs, blueprints, and manifests may contain user prompt text or workflow details in the project output folder. <br>
Mitigation: Review generated files before sharing them and keep private audit or resume data out of shareable blueprints. <br>
Risk: Remote PixelLab deletions, clears, or overwrites can discard existing assets. <br>
Mitigation: Require explicit user permission for destructive remote actions and list the affected assets before carrying them out. <br>


## Reference(s): <br>
- [PixelLab Skill Page](https://clawhub.ai/shilo/skills/pixellab-pip) <br>
- [Official PixelLab Documentation](references/official-pixellab-documentation.md) <br>
- [PixelLab REST v2 API Docs](https://api.pixellab.ai/v2/docs) <br>
- [PixelLab REST v2 OpenAPI Schema](https://api.pixellab.ai/v2/openapi.json) <br>
- [PixelLab MCP Documentation](https://api.pixellab.ai/mcp/docs) <br>
- [PixelLab MCP Setup](https://www.pixellab.ai/mcp) <br>
- [Setup](references/setup.md) <br>
- [Credentials](references/credentials.md) <br>
- [Cost Routing](references/cost-routing.md) <br>
- [Blueprint](references/blueprint.md) <br>
- [Job Lifecycle](references/job-lifecycle.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline code, shell commands, configuration snippets, file paths, and generated asset manifests or blueprints when a PixelLab workflow runs.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce project-local files such as generated assets, spritesheets, manifests, and blueprint JSON only when the user requests a workflow that creates or packages assets.] <br>

## Skill Version(s): <br>
1.2.0 (source: server release metadata and target metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

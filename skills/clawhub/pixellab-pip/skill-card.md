## Description:

PixelLab Pip helps agents route PixelLab setup, authentication, asset generation, editing, animation, talking portraits, lip sync, blueprints, cost checks, and troubleshooting across supported PixelLab MCP, REST, website/editor, Pixelorama, Aseprite, and legacy v1 surfaces.

This skill is ready for commercial/non-commercial use.

## Publisher:

[shilo](https://clawhub.ai/user/shilo)

### License/Terms of Use:

MIT

## Use Case:

Developers, artists, and agent operators use this skill to create, transform, animate, package, and troubleshoot PixelLab game-art assets while preserving credential, cost, provenance, and destructive-action safeguards.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: PixelLab live generation can spend credits, and approved auto mode may allow jobs to run without a fresh cost prompt.

Mitigation: Keep auto off unless that behavior is intended; review the planned paid calls, material inputs, and rough total before credit-spending work.

Risk: A PixelLab bearer token could be exposed if copied into chat or stored in an unsafe place.

Mitigation: Store PIXELLAB_SECRET only in a local secret or environment setting and never paste the token into chat or generated reports.

Risk: Deleting, clearing, or overwriting existing remote PixelLab assets can irreversibly discard stored content.

Mitigation: Require explicit user approval for destructive remote actions and list the affected names, IDs, and count before execution.

Risk: Local post-processing can misrepresent generated art if altered pixels are reported as final PixelLab output.

Mitigation: Preserve original PixelLab outputs, label any approved local fallback or post-processing, and avoid claiming repaired or composited files are final without approval.

## Reference(s):

- [PixelLab REST v2 endpoint index](https://api.pixellab.ai/v2/llms.txt)
- [PixelLab REST v2 docs](https://api.pixellab.ai/v2/docs)
- [PixelLab MCP docs](https://api.pixellab.ai/mcp/docs)
- [PixelLab MCP setup](https://www.pixellab.ai/mcp)
- [PixelLab SDK and MCP repositories](https://github.com/pixellab-code)
- [Setup reference](references/setup.md)
- [Blueprint reference](references/blueprint.md)
- [Usage reporting reference](references/usage-reporting.md)
- [Job lifecycle reference](references/job-lifecycle.md)
- [Cost routing reference](references/cost-routing.md)
- [Official PixelLab documentation reference](references/official-pixellab-documentation.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, API calls, files]

**Output Format:** [Markdown guidance with inline commands, JSON blueprints, manifests, generated asset files, and PixelLab API or MCP call plans]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce saved PixelLab generations, derived previews, per-generation manifests, and portable blueprint JSON files when live generation succeeds.]

## Skill Version(s):

1.6.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

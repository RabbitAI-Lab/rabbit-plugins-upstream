## Description: <br>
Meitu Skills is an agent skill library that routes image, video, audio, poster, product, and editing requests through Meitu CLI and Meitu OpenAPI workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[meituskills](https://clawhub.ai/user/meituskills) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill pack to generate and edit media assets, including posters, stickers, product views, videos, GIFs, portraits, and enhanced images, from agent workflows backed by Meitu OpenAPI. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires Meitu OpenAPI credentials and can read them from environment variables or a local credentials file. <br>
Mitigation: Prefer environment-variable credentials in shared or CI environments, restrict local credential file permissions, and verify credentials are not committed before packaging or publishing. <br>
Risk: User media, prompts, and selected local context may be sent to Meitu OpenAPI for third-party processing. <br>
Mitigation: Use the skill only with media and context that are acceptable for third-party processing, and avoid sensitive personal or proprietary inputs unless that processing is approved. <br>
Risk: Some scene workflows read project context and shared visual memory and may persist outputs, preferences, or project memory locally. <br>
Mitigation: Review workspace and visual-memory paths before use, disable or clear shared profile and memory files in shared workspaces, and inspect generated files before reuse. <br>
Risk: The security verdict requires review because the package combines credentialed execution, remote media processing, broad local reads, and persistent writes. <br>
Mitigation: Perform a deployment review against SECURITY.md, confirm declared permissions match the enabled workflows, and keep runtime repair or CLI upgrades as explicit operator actions. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/meituskills/skills/meitu-skills) <br>
- [README](README.md) <br>
- [Security Model](SECURITY.md) <br>
- [Package Manifest](PACKAGE_MANIFEST.json) <br>
- [Routing Guide](references/routing-guide.md) <br>
- [Meitu Tools Command Catalog](meitu-tools/references/tools.yaml) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files] <br>
**Output Format:** [Markdown guidance, shell commands, JSON CLI results, and generated media files or URLs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Generated outputs may be written to project-local output directories or the OpenClaw visual workspace depending on the selected workflow.] <br>

## Skill Version(s): <br>
2.0.13 (source: server release metadata and PACKAGE_MANIFEST.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

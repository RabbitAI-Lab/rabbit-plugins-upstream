## Description: <br>
Compile AI-generated pixel sprite references and action sheets into deterministic, validated game asset packages and Godot 4 exports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xwchris](https://clawhub.ai/user/xwchris) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and game teams use this skill to turn AI-generated character references and per-action sprite sheets into validated asset manifests, generic output packages, and Godot-ready AnimatedSprite2D exports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow can create or overwrite generated asset files in selected output paths. <br>
Mitigation: Run it only against intended sprite input directories and dedicated output directories, and review paths before compiling or exporting. <br>
Risk: Missing or guessed action semantics can produce incorrect animation manifests or misleading exports. <br>
Mitigation: Require explicit action names, FPS, loop behavior, direction when relevant, and expected frame counts before compile or validation. <br>
Risk: Installing the required CLI globally may affect the user's local npm environment. <br>
Mitigation: Prefer an existing `pixel-asset` executable or local development build; use global install only after confirming it is acceptable. <br>


## Reference(s): <br>
- [Manifest v1](artifact/references/manifest-v1.md) <br>
- [Quality Gates](artifact/references/quality-gates.md) <br>
- [Pixel Asset Compiler on ClawHub](https://clawhub.ai/xwchris/skills/pixel-asset-compiler) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files] <br>
**Output Format:** [Markdown guidance with shell commands, JSON manifest configuration, workflow reports, and generated asset files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce or overwrite generated asset files in caller-selected output directories.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

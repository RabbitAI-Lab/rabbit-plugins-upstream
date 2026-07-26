## Description: <br>
AI 3D model generation powered by CellCog for text-to-3D and image-to-3D workflows that produce production-ready GLB files for games, AR/VR, e-commerce, 3D printing, and batch asset generation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[nitishgargiitd](https://clawhub.ai/user/nitishgargiitd) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, designers, and creative production teams use this skill to ask CellCog to create GLB 3D models from text prompts, reference images, sketches, product photos, or batch item lists. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts and reference files selected by the user may be sent to CellCog for processing. <br>
Mitigation: Use only content approved for external processing, and avoid confidential, regulated, or proprietary designs unless organizational policy permits it. <br>
Risk: CELLCOG_API_KEY could be exposed if copied into source files, logs, or chat messages. <br>
Mitigation: Store CELLCOG_API_KEY in an environment variable or secrets manager and avoid embedding it in prompts, code snippets, or committed files. <br>
Risk: Generated GLB assets may not meet production, safety, performance, or brand requirements without review. <br>
Mitigation: Inspect generated models, textures, polygon counts, and licensing or usage constraints before deployment in games, AR/VR, e-commerce, or 3D printing workflows. <br>


## Reference(s): <br>
- [CellCog Homepage](https://cellcog.ai) <br>
- [ClawHub Skill Page](https://clawhub.ai/nitishgargiitd/skills/3d-model-generation-cellcog) <br>
- [ClawHub Publisher Profile](https://clawhub.ai/user/nitishgargiitd) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Code, API Calls, Configuration, Files] <br>
**Output Format:** [Markdown guidance with Python code examples and CellCog-generated GLB files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires python3, the cellcog dependency, and CELLCOG_API_KEY for CellCog API access.] <br>

## Skill Version(s): <br>
1.0.11 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

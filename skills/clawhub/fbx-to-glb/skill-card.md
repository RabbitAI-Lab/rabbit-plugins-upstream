## Description: <br>
Fbx To Glb Skill Repo helps agents convert FBX 3D models to GLB/glTF using a Node.js assimpjs CLI or prepare a browser-based converter with 3D preview. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zzh448](https://clawhub.ai/user/zzh448) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and technical users use this skill to convert FBX assets to GLB files, preserve common 3D model data, and deploy a simple browser converter when they need a shareable workflow. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The browser template loads Three.js modules from unpkg, adding a third-party runtime dependency for web deployments. <br>
Mitigation: Self-host or pin and review browser dependencies before deploying the web converter for private or business-sensitive models. <br>
Risk: The documentation references an assimpjs.wasm asset, but the artifact evidence does not include that file. <br>
Mitigation: Verify that assimpjs.wasm is bundled alongside assimpjs.js before production web deployment; prefer the CLI when the web bundle is incomplete. <br>
Risk: The CLI writes output files to user-selected paths and supports overwrite with --force. <br>
Mitigation: Review input and output paths before execution and use --force only when replacing an existing GLB file is intended. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zzh448/skills/fbx-to-glb) <br>
- [assimpjs project](https://github.com/kovacsv/assimpjs) <br>
- [Published web converter URL](https://zzh448.github.io/fbx-to-glb/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files] <br>
**Output Format:** [Markdown guidance with inline shell commands; GLB files may be produced when the conversion script is executed.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [CLI conversion reads a user-provided FBX file path and writes GLB output; the web template converts files in the browser.] <br>

## Skill Version(s): <br>
1.0.1 (source: ClawHub release metadata; skill frontmatter lists 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

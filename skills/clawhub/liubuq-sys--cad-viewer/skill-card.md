## Description: <br>
Starts or reuses CAD Viewer and returns live review links for CAD, implicit CAD, robot-description, DXF, and G-code files. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[liubuq-sys](https://clawhub.ai/user/liubuq-sys) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and engineers use this skill to open generated or existing CAD, robot-description, and toolpath artifacts in a local viewer and return review URLs for visual inspection. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security review flags under-disclosed code-execution and file-writing behavior. <br>
Mitigation: Review the skill before installation and use it only with CAD files and generators from trusted sources. <br>
Risk: Executable model sources and CAD sidecars can run code or create derived artifacts. <br>
Mitigation: Treat .implicit.js, .implicit.mjs, STEP sidecar modules, and Python CAD generator files as executable code, and use a narrow dedicated model directory as --dir. <br>
Risk: The viewer keeps a local server running and review URLs can include custom query parameters. <br>
Mitigation: Open only trusted review links, avoid untrusted custom query parameters, and stop the local viewer when it is no longer needed. <br>


## Reference(s): <br>
- [ClawHub Cad Viewer skill page](https://clawhub.ai/liubuq-sys/skills/cad-viewer) <br>
- [CAD Viewer Features](references/viewer-features.md) <br>
- [CAD Viewer Development](references/development.md) <br>
- [MoveIt2 Server](references/moveit2-server.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown or plain text with local review URLs and optional JSON startup details] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Starts or reuses a local viewer for an explicit model directory and returns URLs scoped to requested files.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

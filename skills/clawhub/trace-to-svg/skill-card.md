## Description: <br>
Trace bitmap images (PNG/JPG/WebP) into clean SVG paths using potrace/mkbitmap for logos, silhouettes, manufacturable outlines, and downstream CAD workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ajmwagar](https://clawhub.ai/user/ajmwagar) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and engineers use this skill to convert high-contrast bitmap images, logos, and silhouettes into SVG path output for CAD and manufacturing-oriented workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Installing required tracing binaries from untrusted sources could introduce unsafe local tooling. <br>
Mitigation: Install potrace and mkbitmap through a trusted package manager as recommended by the server security guidance. <br>
Risk: The conversion script creates parent directories and writes the SVG to the user-specified output path. <br>
Mitigation: Verify the input image and output path before execution, especially when using paths supplied by another user or workflow. <br>
Risk: Low-contrast photos or noisy source images can produce inaccurate or overly complex SVG paths for downstream CAD use. <br>
Mitigation: Inspect the generated SVG and tune threshold, turdsize, alphamax, or opttolerance before using paths in manufacturing-oriented workflows. <br>


## Reference(s): <br>
- [Examples](artifact/references/examples.md) <br>
- [Trace To Svg ClawHub page](https://clawhub.ai/ajmwagar/skills/trace-to-svg) <br>


## Skill Output: <br>
**Output Type(s):** [Files, Shell commands, Guidance] <br>
**Output Format:** [SVG file output with Markdown and bash usage guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires local potrace and mkbitmap binaries; the script writes an SVG to the requested output path and echoes that path.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

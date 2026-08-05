## Description: <br>
Build lightweight SDF and canvas displacement glass surfaces with Vaso for React interfaces. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[woodfishhhh](https://clawhub.ai/user/woodfishhhh) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to add compact React SDF liquid-glass surfaces using Vaso, with guidance for readable overlays, responsive sizing, browser fallbacks, and tuning. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill asks agents to add the vaso frontend package. <br>
Mitigation: Review the dependency before installation and use it only in React projects where a canvas/SDF glass effect is desired. <br>
Risk: Readable content can become distorted, doubled, or color-fringed if it is placed inside the displacement layer. <br>
Mitigation: Keep Vaso in an absolute background layer and render text, controls, icons, and focus rings in an unfiltered sibling overlay. <br>
Risk: Mismatched dimensions, radius values, or unsupported browser behavior can produce clipped corners, stale canvas sizing, or weak fallbacks. <br>
Mitigation: Use ResizeObserver, pass explicit width and height to Vaso, match the host radius, keep a CSS tint/backdrop fallback, and verify desktop and mobile viewports. <br>


## Reference(s): <br>
- [SDF Tuning](artifact/references/tuning.md) <br>
- [huozhi/vaso](https://github.com/huozhi/vaso) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline TypeScript, CSS, and shell command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May adapt bundled React and CSS assets and add the vaso dependency; no credentials or external services are required by the skill evidence.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

## Description: <br>
Aios Make Chart Image renders JSON data, Markdown tables, or ECharts options into PNG, SVG, JPEG, or WebP chart images using its bundled JavaScript renderer. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kadbbz](https://clawhub.ai/user/kadbbz) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to turn sender-provided chart data into shareable chart image files while preserving workspace file isolation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Untrusted chart input may be rendered into files that are later shared with users. <br>
Mitigation: Prefer PNG, JPEG, or WebP for untrusted inputs and review generated chart files before distribution. <br>
Risk: Incorrect workspace or senderId values could break sender-scoped file isolation. <br>
Mitigation: Verify the senderId and workspace arguments before generation and stop if senderId is unavailable. <br>
Risk: Image rendering depends on npm packages including ECharts and Sharp. <br>
Mitigation: Keep npm dependencies current and install them only from trusted package sources. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/kadbbz/skills/aios-make-chart-image) <br>


## Skill Output: <br>
**Output Type(s):** [Files, JSON, Shell commands, Configuration guidance] <br>
**Output Format:** [PNG, SVG, JPEG, or WebP image files with JSON status output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires explicit senderId and workspace arguments; generated outputs are kept under the sender-scoped generated directory.] <br>

## Skill Version(s): <br>
1.0.1 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

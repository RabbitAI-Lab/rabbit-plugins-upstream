## Description: <br>
Build production-ready GPU liquid-glass surfaces with liquid-gl for React, Vite, or DOM interfaces. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[woodfishhhh](https://clawhub.ai/user/woodfishhhh) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to add reusable WebGL liquid-glass surfaces to React, Vite, or DOM interfaces while keeping foreground content crisp and preserving fallbacks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The `liquid-gl` package is an external frontend dependency. <br>
Mitigation: Review the dependency with the project's normal npm package review process before installing it. <br>
Risk: `snapshotSelector` can include sensitive interface content if it is pointed at the entire app or a private-content container. <br>
Mitigation: Scope `snapshotSelector` to a non-sensitive visual background and keep foreground content in a separate overlay. <br>
Risk: WebGL capture or rendering can fail or become expensive on some devices and dense interfaces. <br>
Mitigation: Preserve the CSS backdrop-filter fallback, test desktop and mobile viewports, and reduce resolution or avoid many simultaneous lenses when needed. <br>


## Reference(s): <br>
- [WebGL Tuning](references/tuning.md) <br>
- [liquidGL](https://github.com/naughtyduk/liquidGL) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with code, configuration, and shell command suggestions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May adapt bundled React, CSS, and TypeScript declaration assets for the target project.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

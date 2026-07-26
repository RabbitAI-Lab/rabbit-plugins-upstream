## Description: <br>
Ports an existing Remotion React composition source into HyperFrames HTML for one-way migration. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[heygen-com](https://clawhub.ai/user/heygen-com) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill when they explicitly need to migrate an existing Remotion video composition into HyperFrames HTML. It helps lint the Remotion source, map Remotion APIs to HyperFrames constructs, generate the HyperFrames composition, validate visual similarity, and document translation gaps. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security scan flagged a silent self-update command that runs through npx before the skill is used. <br>
Mitigation: Require explicit user confirmation or remove the self-update step before use, and review any dependency update behavior in a sandboxed environment. <br>
Risk: The skill runs local linting, Remotion rendering, HyperFrames rendering, and SSIM comparison commands against user-provided projects. <br>
Mitigation: Run translation and evaluation commands in an isolated workspace when handling untrusted Remotion sources, and review generated HTML and notes before deployment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/heygen-com/skills/remotion-to-hyperframes) <br>
- [Remotion to HyperFrames API Map](artifact/references/api-map.md) <br>
- [Remotion to HyperFrames Evaluation Guide](artifact/references/eval.md) <br>
- [Escape Hatch Guidance](artifact/references/escape-hatch.md) <br>
- [Translation Limitations](artifact/references/limitations.md) <br>
- [HyperFrames Remotion interop PR](https://github.com/heygen-com/hyperframes/pull/214) <br>


## Skill Output: <br>
**Output Type(s):** [code, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and generated HTML/Markdown files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces HyperFrames index.html output, optional TRANSLATION_NOTES.md, lint findings, and visual validation commands for Remotion-to-HyperFrames migrations.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

## Description: <br>
Formats WeChat public-account articles by helping an agent structure user-provided drafts or Markdown and convert them into styled HTML. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tracevan](https://clawhub.ai/user/tracevan) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External creators, operators, and developers use this skill to turn draft text, Markdown, or uploaded article content into WeChat public-account HTML with article sections, highlights, step cards, prompt blocks, and copy-ready formatting. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated HTML can include embedded local image data and active copy-related script. <br>
Mitigation: Use the skill only with trusted Markdown and image paths, disable image embedding when it is not needed, and review the HTML before opening, copying, or sharing it. <br>
Risk: The security verdict is suspicious because runtime behavior can read local image paths and generate active HTML beyond simple static conversion. <br>
Mitigation: Review the generated file and source content before deployment, and avoid processing untrusted Markdown. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/tracevan/skills/wechat-feige-formatter) <br>
- [README](artifact/README.md) <br>
- [WeChat formatting optimization rules](artifact/references/排版优化规则.md) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Code, Shell commands, Files, Guidance] <br>
**Output Format:** [Optimized Markdown, generated HTML files, shell commands, and concise usage guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Generated HTML may include embedded local image data and browser copy controls.] <br>

## Skill Version(s): <br>
2.3.6 (source: server release evidence and clawhub.toml) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

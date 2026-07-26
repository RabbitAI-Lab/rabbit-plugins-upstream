## Description: <br>
Turns meeting transcripts into phone-friendly SVG meeting-summary cards and PNG images for sharing in workplace chat tools. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[maojiebc](https://clawhub.ai/user/maojiebc) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Employees, external collaborators, and operations teams use this skill to convert meeting transcripts into a shared visual summary that captures decisions, open questions, action owners, and timelines. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The PNG conversion helper may automatically install cairosvg into the active Python environment with --break-system-packages. <br>
Mitigation: Review the helper before use, install dependencies explicitly where possible, and run the conversion in an isolated or disposable environment. <br>
Risk: Meeting transcripts may contain confidential business discussions, and generated SVG or PNG files are written to disk for manual sharing. <br>
Mitigation: Use approved local workspaces for sensitive transcripts, review generated files before sharing, and delete outputs when retention is not needed. <br>
Risk: The converter relies on local Node/Puppeteer or cairosvg behavior, which may be unsuitable in shared, locked-down, or production environments. <br>
Mitigation: Confirm dependency and execution policies before installation or conversion, especially on managed systems. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/maojiebc/skills/majia-meeting-svg) <br>
- [Project homepage](https://github.com/maojiebc/majia-meeting-svg) <br>
- [Example meeting cards](references/examples/) <br>


## Skill Output: <br>
**Output Type(s):** [text, code, shell commands, files] <br>
**Output Format:** [SVG markup, PNG image files, and a short Markdown or text summary.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [PNG conversion targets 2x scale for phone-friendly sharing when local conversion dependencies are available.] <br>

## Skill Version(s): <br>
1.1.12 (source: server release evidence and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

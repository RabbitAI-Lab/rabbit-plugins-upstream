## Description: <br>
Helps agents work with Lanhu UI design handoffs by listing designs, downloading original images and slices, extracting HTML/CSS specs and design tokens, and producing implementation guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oyjt](https://clawhub.ai/user/oyjt) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to inspect Lanhu design projects, retrieve authenticated visual and specification data, download local assets, and implement high-fidelity UI in web or mobile projects. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Untrusted slice JSON can reference file:// URLs that are read and copied into the selected output directory. <br>
Mitigation: Use slice JSON generated directly from trusted Lanhu projects, avoid hand-edited or third-party JSON, and remove or disable file:// URL handling before using the downloader with untrusted input. <br>
Risk: LANHU_COOKIE is a full browser session credential for the logged-in Lanhu account. <br>
Mitigation: Store the cookie only in the local environment, never commit or print it, rotate it when exposed, and refresh it only through the documented browser login flow. <br>


## Reference(s): <br>
- [Lanhu Design Tools](artifact/references/lanhu-design-tools.md) <br>
- [Design Implementation Rules](artifact/references/design-implementation-rules.md) <br>
- [Lanhu](https://lanhuapp.com) <br>
- [ClawHub skill page](https://clawhub.ai/oyjt/skills/lanhu-design) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, files, guidance] <br>
**Output Format:** [Markdown guidance with JSON script outputs, code snippets, shell commands, and generated or downloaded local files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Scripts require Node.js >= 18 and a LANHU_COOKIE environment variable; design images, specs, and slices may be written to local project directories when the agent runs the scripts.] <br>

## Skill Version(s): <br>
1.2.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

## Description: <br>
Convert Markdown articles into WeChat Official Account friendly inline-style HTML with 12 visual themes, rich-copy preview, macOS rich clipboard support, configurable Upload footer, gallery generation, and validation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[banlon](https://clawhub.ai/user/banlon) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, content teams, and external creators use this skill to turn Markdown articles into WeChat Official Account paste-ready HTML, create a local rich-copy preview, and validate compatibility before publishing. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The package references helper scripts and reference files that are not bundled in the submitted artifact. <br>
Mitigation: Confirm those paths resolve to trusted files before running commands, or supply the helper files from a trusted source. <br>
Risk: The default footer can add Upload branding to generated articles. <br>
Mitigation: Disable or customize the footer when branding is not desired. <br>
Risk: Generated HTML may not be suitable for WeChat if validation is skipped. <br>
Mitigation: Run the WeChat HTML validator on freshly generated output and only treat the article as ready after a PASS result. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/banlon/skills/uploadweixin) <br>
- [Server-resolved GitHub source](https://github.com/Banlon/agent-skills/tree/main/skills/uploadweixin) <br>


## Skill Output: <br>
**Output Type(s):** [files, shell commands, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and generated HTML files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Generates article.html, preview.html, optional gallery.html, and validation output when the referenced helper files are available.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

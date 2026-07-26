## Description: <br>
Html2screenshot converts HTML from a file path, URL, or HTML string into a full-page PNG screenshot with configurable desktop or mobile viewport settings. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[changyogpt-code](https://clawhub.ai/user/changyogpt-code) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to capture complete PNG screenshots of local HTML files, URLs, or pasted HTML content for reporting, preview, and visual validation workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill recommends a background HTTP service, but the referenced server implementation is not included and the network scope is unclear. <br>
Mitigation: Review the server implementation before enabling it, bind it to localhost when possible, and restrict access with local firewall or equivalent controls. <br>
Risk: Puppeteer and Chrome render HTML selected by the user, which can expose sensitive local content or interact with untrusted remote pages. <br>
Mitigation: Avoid rendering sensitive local files, prefer trusted HTML inputs, and use browser sandboxing plus network controls for untrusted content. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/changyogpt-code/skills/html2screenshot) <br>
- [Dataset and evaluation plan](artifact/dataset.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, code, configuration, files] <br>
**Output Format:** [Markdown guidance with inline shell and JavaScript examples; generated captures are PNG files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Supports viewport width, viewport height, device scale factor, and full-page capture settings.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence, artifact frontmatter, artifact metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

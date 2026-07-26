## Description: <br>
Connects to CDP to open webpages, capture screenshots, read page text or HTML, and execute JavaScript through a browser-control CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[fslong520](https://clawhub.ai/user/fslong520) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and browser-automation agents use this skill to control a local Chrome, Edge, or Chromium browser over CDP for webpage navigation, screenshots, text extraction, HTML source capture, JavaScript evaluation, clicks, and typing. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can automate authenticated browser sessions and interact with logged-in pages. <br>
Mitigation: Use it only for intended browser-control workflows, avoid banking, admin, and secret-bearing pages unless supervised, and review actions before execution. <br>
Risk: Local key material may be handled during browser-control workflows. <br>
Mitigation: Rotate the ZClaw API key if it may have been exposed and limit use to environments where browser access is acceptable. <br>
Risk: The CLI can execute JavaScript, click elements, type text, and capture page content through CDP. <br>
Mitigation: Run status checks before actions, keep browser automation scoped to trusted pages, and inspect generated screenshots, HTML, or text outputs before relying on them. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/fslong520/skills/urlgo) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Text, Code, Files, Guidance] <br>
**Output Format:** [Markdown with inline bash commands, browser-control guidance, CLI text output, HTML source, and screenshot file paths] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create PNG screenshot files and expose page text, HTML, or JavaScript evaluation results from browser pages reachable through local CDP.] <br>

## Skill Version(s): <br>
6.5.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

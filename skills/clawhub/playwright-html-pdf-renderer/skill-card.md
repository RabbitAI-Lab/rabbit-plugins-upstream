## Description: <br>
Render deterministic PDFs from HTML using local Playwright/Chromium. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[asperitas-solutions](https://clawhub.ai/user/asperitas-solutions) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to produce stable, repeatable PDF files from HTML content with local Playwright and Chromium. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Installing or using the skill may add Playwright and Chromium dependencies. <br>
Mitigation: Review dependency installation in the target environment before setup and install Chromium as a bootstrap step only. <br>
Risk: Rendering untrusted HTML may load external assets or local paths depending on how content is supplied. <br>
Mitigation: Render only trusted or reviewed HTML, restrict accessible paths and network behavior where practical, and verify the generated PDF before use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/asperitas-solutions/skills/playwright-html-pdf-renderer) <br>
- [Publisher profile](https://clawhub.ai/user/asperitas-solutions) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Markdown with inline shell commands and ordered runtime steps] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guides local headless Chromium PDF generation and verification.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

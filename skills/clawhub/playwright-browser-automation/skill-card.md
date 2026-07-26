## Description: <br>
Browser automation using Playwright API directly. Navigate websites, interact with elements, extract data, take screenshots, generate PDFs, record videos, and automate complex workflows. More reliable than MCP approach. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[spiceman161](https://clawhub.ai/user/spiceman161) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and automation engineers use this skill to script browser workflows with Playwright, including navigation, form interaction, data extraction, screenshots, PDFs, downloads, authentication state reuse, video recording, and tracing. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill includes a broad passwordless sudoers setup for Playwright browser installation. <br>
Mitigation: Do not copy the NOPASSWD sudoers rules; run dependency installation manually with administrator approval and remove any temporary elevation afterward. <br>
Risk: Browser automation can create screenshots, recordings, downloads, traces, and authentication state files that may contain sensitive data. <br>
Mitigation: Keep generated browser artifacts and storage state files out of shared folders and source control, and delete them when no longer needed. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/spiceman161/skills/playwright-browser-automation) <br>
- [Playwright Docs](https://playwright.dev) <br>
- [Playwright API Reference](https://playwright.dev/docs/api/class-playwright) <br>
- [Playwright Best Practices](https://playwright.dev/docs/best-practices) <br>
- [Playwright Locators Guide](https://playwright.dev/docs/locators) <br>
- [Playwright Trace Viewer](https://trace.playwright.dev) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, code, shell commands, configuration] <br>
**Output Format:** [Markdown with JavaScript and bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes installation commands, Playwright usage patterns, configuration examples, and conceptual MCP call examples.] <br>

## Skill Version(s): <br>
2.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

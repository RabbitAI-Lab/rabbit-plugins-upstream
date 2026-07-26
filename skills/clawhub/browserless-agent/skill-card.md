## Description: <br>
Professional web automation with headless browser - navigate, scrape, automate, test, and interact with any website. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[raff-lima](https://clawhub.ai/user/raff-lima) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent users use this skill to automate browser navigation, data extraction, form interaction, screenshots, PDFs, and website testing through a Browserless service. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill gives an agent broad browser-control authority over web pages, forms, storage, cookies, headers, uploads, screenshots, PDFs, and arbitrary JavaScript evaluation. <br>
Mitigation: Install only for agents that need this authority, use a dedicated or self-hosted Browserless instance for sensitive work, and require explicit confirmation before uploads, submissions, storage or cookie reads, custom auth headers, private-page captures, or JavaScript evaluation. <br>
Risk: Browserless credentials or session data could be exposed if secrets or captured page content are handled casually. <br>
Mitigation: Store BROWSERLESS_TOKEN in secure secret storage, prefer wss:// for remote services, and avoid capturing or returning private pages unless the user has confirmed the action. <br>


## Reference(s): <br>
- [Browserless Documentation](https://docs.browserless.io) <br>
- [Playwright Documentation](https://playwright.dev) <br>
- [CSS Selectors Reference](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Selectors) <br>
- [Browserless Service](https://browserless.io) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files] <br>
**Output Format:** [Markdown, JSON action arguments, shell commands, and generated browser capture files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce screenshots, PDFs, extracted page data, cookie or storage values, and browser automation guidance depending on the invoked action.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

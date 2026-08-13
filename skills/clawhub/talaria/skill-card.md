## Description:

Talaria wraps Playwright with playwright-extra and puppeteer-extra-plugin-stealth to reduce basic bot-detection and WAF challenge triggers, but it does not solve CAPTCHAs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gadielkalleb](https://clawhub.ai/user/gadielkalleb)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use Talaria to run Playwright browser automation, scraping, screenshots, or HTML capture against sites they are authorized to automate when basic bot-detection fingerprinting is blocking vanilla Playwright.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill supports stealth browser automation and WAF-evasion workflows that can be misused on sites where the user lacks authorization.

Mitigation: Use it only for websites the user is authorized to test or automate, and do not claim success when a challenge remains visible.

Risk: Setup and postinstall behavior may download npm dependencies and Chromium browser tooling.

Mitigation: Review npm install and postinstall behavior, then pin or audit dependencies before use in sensitive environments.

Risk: Proxy credentials may be supplied through environment variables or CLI/API options.

Mitigation: Avoid exposing proxy credentials in shared shells, command histories, logs, or checked-in configuration files.

Risk: The skill reduces basic fingerprint signals but does not solve CAPTCHAs or guarantee bypass of advanced bot-detection systems.

Mitigation: Report unresolved challenges with URL and screenshot evidence, and avoid inventing CAPTCHA-solving behavior.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/gadielkalleb/skills/talaria)
- [Publisher Profile](https://clawhub.ai/user/gadielkalleb)
- [Project Homepage](https://github.com/gadielkalleb/talaria)
- [Bright Data Playwright CAPTCHA Article](https://brightdata.com.br/blog/dados-do-site/bypass-captchas-with-playwright)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, JSON, Files, Guidance]

**Output Format:** [Markdown guidance with JavaScript and bash examples; the CLI can emit JSON and write screenshot or HTML files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js and npm; setup or postinstall may download Chromium; optional proxy and headless behavior can be configured with environment variables.]

## Skill Version(s):

0.1.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Check whether a Playwright, Puppeteer, Selenium, or CDP-driven browser presents a coherent fingerprint across browser automation signals such as navigator.webdriver, HeadlessChrome tokens, worker consistency, patched API integrity, and GPU identity.

This skill is ready for commercial/non-commercial use.

## Publisher:

[liarjsdev](https://clawhub.ai/user/liarjsdev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and test engineers use this skill to measure whether automated browser sessions look internally coherent before relying on stealth plugins, headless configurations, or fingerprint-quality assertions in test suites.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Default network-aware scans can send browser connection metadata to liarjs.dev.

Mitigation: Use --offline for JavaScript-layer checks only, or point --endpoint to a trusted internal deployment.

Risk: Attaching to a CDP endpoint controls an existing browser session.

Mitigation: Confirm the endpoint with the user before attaching and prefer a throwaway browser profile when a specific running browser is not required.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/liarjsdev/skills/playwright-stealth-verify)
- [Hosted liarjs verifier](https://liarjs.dev)

## Skill Output:

**Output Type(s):** [Analysis, Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with TypeScript and bash examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May describe scan scores, failing fingerprint check IDs, browser-session cautions, and offline or custom endpoint options.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

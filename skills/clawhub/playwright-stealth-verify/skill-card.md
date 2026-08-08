## Description:

Check whether a Playwright, Puppeteer, Selenium or CDP-driven browser presents a coherent fingerprint, using liarjs as a library against a Page you already have - navigator.webdriver, HeadlessChrome tokens, worker versus main-thread identity, patched-API integrity, WebGL versus WebGPU GPU identity.

This skill is ready for commercial/non-commercial use.

## Publisher:

[liarjsdev](https://clawhub.ai/user/liarjsdev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and QA engineers use this skill to measure whether automation-driven browsers present internally coherent fingerprints before relying on stealth claims or adding fingerprint quality assertions to test suites.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Online scans can disclose browser and network details to an external endpoint.

Mitigation: Use --offline or point --endpoint at an owned deployment when external network disclosure is not acceptable.

Risk: Attaching to an existing CDP endpoint can inspect a browser session that may contain user data.

Mitigation: Confirm authorization and endpoint ownership before attaching; prefer the throwaway default when testing a launch configuration.

Risk: Scanning pages outside the user's control can create unauthorized testing activity.

Mitigation: Run probes on about:blank or on pages the user owns or is authorized to test.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/liarjsdev/skills/playwright-stealth-verify)
- [liarjs hosted verifier](https://liarjs.dev)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Code, Shell commands, Guidance]

**Output Format:** [Markdown with TypeScript and bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include scan result interpretation, failing check identifiers, and offline or authorized-endpoint guidance.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Headless-detection-resistant browser automation in Docker for authorized QA, compatibility testing, and defensive security research. Camoufox + OS-level input + persistent fingerprints. Use only with sites you own or have written authorization to test.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and security testers use this skill to check their own sites or explicitly authorized targets for anti-bot compatibility, browser behavior, and defensive security testing. Use it only within the documented authorization and scope.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan rated the release suspicious because it repeatedly uses a changeable Docker image reference; the scan was partial because some local references could not be resolved.

Mitigation: Consider waiting to install until the Docker image is pinned to a reviewed digest, as the security guidance recommends.

Risk: Without AUTH_TOKEN, anyone who can reach the browser API can control the browser, including its pages, cookies, and scripts.

Mitigation: Set AUTH_TOKEN and bind published API and viewer ports to localhost or place the API behind an authenticating proxy.

Risk: Browser dialogs accept by default and can confirm destructive actions on stateful sites.

Mitigation: Call handle_dialog with accept: false before actions that may raise dialogs on stateful sites, and avoid targets where an accidental confirmation could cause harm.

Risk: Mounted page loaders run automatically on matching URLs and can change page state.

Mitigation: Only mount loader files that you wrote or audited, and review their steps before use.

## Reference(s):

- [Setup and security guidance](references/setup.md)
- [Project homepage](https://github.com/psyb0t/docker-stealthy-auto-browse)
- [API input guidance](https://github.com/psyb0t/docker-stealthy-auto-browse/blob/main/docs/api.md#humanized-input)
- [Script mode control flow](https://github.com/psyb0t/docker-stealthy-auto-browse/blob/main/docs/script-mode.md#control-flow)

## Skill Output:

**Output Type(s):** [Text, HTML, Screenshots, Structured data, API calls, Configuration instructions]

**Output Format:** [JSON API responses containing page text, HTML, screenshots, and structured browser results; Markdown setup guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Page capture and browser actions should stay within the authorized test scope.]

## Skill Version(s):

3.9.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

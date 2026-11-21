## Description:

Browser automation in Docker for authorized QA, compatibility testing, and defensive security research on sites you own or have written authorization to test.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and security testers use the skill to automate browser interactions and inspect pages while checking anti-bot behavior, detection-library compatibility, and authorized site QA. Use it only on systems you own or targets covered by written authorization.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release is rated suspicious because examples use a mutable Docker image tag, and scanner coverage is partial.

Mitigation: Verify the image source and use a reviewed fixed version or digest; review local references that were not covered by the scan.

Risk: When AUTH_TOKEN is unset, anyone who can reach the service port can control the browser.

Mitigation: Bind published ports to loopback and set AUTH_TOKEN for any non-localhost deployment.

Risk: Persistent browser profiles can contain live session cookies, and enabled CAPTCHA extensions can access every page.

Mitigation: Use dedicated test accounts, protect or remove profile data after testing, and enable extensions only for authorized targets.

Risk: Dialogs are accepted automatically by default, and mounted page loaders run when their URL rules match.

Mitigation: Disable or scope dialog acceptance before state-changing actions, and audit loader files before mounting them.

## Reference(s):

- [Setup and secure configuration](references/setup.md)
- [Project homepage](https://github.com/psyb0t/docker-stealthy-auto-browse)
- [API: Humanized input](https://github.com/psyb0t/docker-stealthy-auto-browse/blob/main/docs/api.md#humanized-input)
- [Script mode control flow](https://github.com/psyb0t/docker-stealthy-auto-browse/blob/main/docs/script-mode.md#control-flow)
- [Cluster mode guide](https://psyb0t.github.io/docker-stealthy-auto-browse/cluster-mode/)

## Skill Output:

**Output Type(s):** [API calls, JSON, Text, HTML, Screenshots]

**Output Format:** [JSON responses containing browser action results, page data, and optional screenshots]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The response depends on the requested browser action and the authorized target.]

## Skill Version(s):

3.9.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

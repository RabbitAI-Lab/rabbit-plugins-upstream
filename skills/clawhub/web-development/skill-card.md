## Description:

Helps developers implement, debug, deploy, and validate web frontends using React, Vue, Vite, browser testing, and CloudBase integrations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[binggg](https://clawhub.ai/user/binggg)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to build and troubleshoot existing web apps, integrate CloudBase where needed, and verify frontend behavior in a browser before deployment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: CloudBase authentication examples may lead to protected endpoints accepting unverified tokens.

Mitigation: Verify tokens or sessions on the server before returning protected data; review and correct the examples before using them for authentication work.

Risk: The example stores a bearer token in a JavaScript-set cookie, exposing session handling to avoidable risk.

Mitigation: Use a server-managed, appropriately protected session cookie instead of setting a bearer-token cookie in browser JavaScript.

Risk: A hard-coded or incorrect CloudBase region can misroute authentication requests.

Mitigation: Configure the CloudBase region explicitly for the target deployment.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/binggg/skills/web-development)
- [Framework guidance](frameworks.md)
- [Browser validation guidance](browser-testing.md)
- [CloudBase integration documentation](https://docs.cloudbase.net/integration/introduce.md)

## Skill Output:

**Output Type(s):** [Code, Configuration, Shell commands, Guidance]

**Output Format:** [Markdown with code and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Frontend changes should be checked with project tests and browser validation where applicable.]

## Skill Version(s):

1.27.70 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

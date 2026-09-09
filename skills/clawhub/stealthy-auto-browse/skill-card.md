## Description:

Headless-detection-resistant browser automation in Docker for authorized QA, compatibility testing, and defensive security research. Camoufox + OS-level input + persistent fingerprints. Use only with sites you own or have written authorization to test.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, QA engineers, and defensive security testers use this skill to drive containerized browser automation for authorized anti-bot validation, compatibility testing, and sanctioned security research against systems they own or have written permission to test.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The browser-control service can expose navigation, input, cookies, screenshots, script execution, and page content capture if reachable by unauthorized users.

Mitigation: Bind API and noVNC ports to localhost, set AUTH_TOKEN for any non-throwaway use, and place any broader deployment behind an authenticating proxy.

Risk: The skill is designed for detection-resistant browser automation and can be misused on targets outside the tester's authority.

Mitigation: Use it only for owned systems, written-authorized engagements, or controlled defensive testing; avoid scraping, access-control evasion, unauthorized account automation, and out-of-scope CAPTCHA workflows.

Risk: Persistent profiles, proxies, loader YAML, and noVNC access can expand data exposure or execute unreviewed automation behavior.

Mitigation: Use dedicated test accounts, audit loader YAML before mounting it, avoid exposing noVNC, restrict egress to authorized targets, and remove persisted session data after testing.

## Reference(s):

- [Setup](references/setup.md)
- [Skill homepage](https://github.com/psyb0t/docker-stealthy-auto-browse)
- [ClawHub skill page](https://clawhub.ai/psyb0t/skills/stealthy-auto-browse)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, API calls, JSON]

**Output Format:** [Markdown with inline JSON and bash examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May describe HTTP or MCP browser-control actions, setup commands, environment variables, and safety constraints for authorized testing workflows.]

## Skill Version(s):

2.6.9 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

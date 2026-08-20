## Description:

Provides headless-detection-resistant browser automation in Docker for authorized QA, compatibility testing, and defensive security research against systems the user owns or has written permission to test.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, QA engineers, and authorized security testers use this skill to drive a Camoufox browser through HTTP, MCP, or script mode for anti-bot QA, compatibility checks, and defensive security research.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The browser control surface can navigate, input data, capture page content, run scripts, and expose active sessions if reachable by unauthorized users.

Mitigation: Bind the service to 127.0.0.1, set AUTH_TOKEN for any non-trivial deployment, and keep VNC unpublished or localhost-only.

Risk: The skill is designed for realistic automation and can be misused against sites without permission.

Mitigation: Use it only on systems you own or have written authorization to test, and keep tests within the approved scope.

Risk: Persistent browser profiles can retain cookies, fingerprints, and account state after a test run.

Mitigation: Use dedicated test accounts, protect any mounted profile volume, and delete persistent profile data when testing ends.

Risk: Mounted loader YAML runs automatically on matching URLs and can modify page state.

Mitigation: Mount only loader files that have been written or audited for the specific authorized test.

Risk: Container image tags are mutable and may change after review.

Mitigation: Pin the Docker image by reviewed digest and re-review before upgrading.

Risk: Dialogs are auto-accepted by default and may confirm destructive actions on stateful sites.

Mitigation: Disable or scope dialog auto-accept before steps that may trigger confirmation, permission, or beforeunload prompts.

## Reference(s):

- [Setup Guide](references/setup.md)
- [ClawHub Skill Page](https://clawhub.ai/psyb0t/skills/stealthy-auto-browse)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON examples and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes HTTP and MCP browser actions, Docker setup steps, script-mode examples, and authorized-use constraints.]

## Skill Version(s):

2.5.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

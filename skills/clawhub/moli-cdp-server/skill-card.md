## Description:

Start Moli's CDP server and connect Playwright, Puppeteer, or raw CDP clients to a local headless-browser endpoint.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lexmount](https://clawhub.ai/user/lexmount)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and automation engineers use this skill to run Moli as a local CDP endpoint, attach existing browser automation clients, and troubleshoot discovery, target startup, layout, screenshot, and protocol coverage issues.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote installer commands can execute untrusted code if the release source is not trusted.

Mitigation: Install only when the Moli GitHub release source is trusted; for higher assurance, download and inspect the installer before running it.

Risk: Exposing the CDP server beyond loopback can allow unintended remote browser automation access.

Mitigation: Keep the server bound to 127.0.0.1 unless remote access is explicitly needed and network controls are in place.

## Reference(s):

- [CDP server guide](references/protocols.md)
- [Moli Linux and macOS release installer](https://github.com/lexmount/moli/releases/latest/download/moli-installer.sh)
- [Moli Windows release installer](https://github.com/lexmount/moli/releases/latest/download/moli-installer.ps1)
- [ClawHub skill page](https://clawhub.ai/lexmount/skills/moli-cdp-server)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with shell, PowerShell, and JavaScript code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides local CDP server startup, client attachment, endpoint probing, and troubleshooting.]

## Skill Version(s):

1.0.1 (source: server evidence release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

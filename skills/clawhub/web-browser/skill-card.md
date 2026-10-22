## Description:

Guides agents through environment-aware browser testing, interface diagnosis, and user-assisted service credential issuance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and other agents use this skill to verify web interfaces, investigate browser styling issues, and guide user-assisted sign-in and service token issuance for subsequent automation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Real signed-in browser sessions can expose live service credentials to the agent or its transcript.

Mitigation: Obtain explicit approval before capturing sign-in screens; avoid personal accounts and long-lived administrator credentials unless that exposure is acceptable.

Risk: Issued credentials may have excessive permissions or be persisted or handed off to an unintended destination.

Mitigation: Review each token's scope, destination secret store, and handoff command before issuance or use.

## Reference(s):

- [ClawHub web-browser release](https://clawhub.ai/drumrobot/skills/web-browser)
- [UI testing guide](artifact/ui-test.md)
- [Credential issuance guide](artifact/credential-issue.md)
- [Orca computer-use guide](artifact/orca-computer.md)
- [CDP tracing guide](artifact/cdp-trace.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Code]

**Output Format:** [Markdown with browser actions and inline commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include UI verification findings, diagnostic steps, and credential handoff guidance.]

## Skill Version(s):

0.3.0 (source: server-resolved ClawHub release and CHANGELOG; bundled frontmatter says 0.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

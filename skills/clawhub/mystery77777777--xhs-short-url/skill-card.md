## Description:

This skill helps agents convert public Xiaohongshu note long URLs into xhslink.com short links, with batch submission, status polling, quota checks, and CSV export.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mystery77777777](https://clawhub.ai/user/mystery77777777)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and AI agents use this skill to submit one to fifty Xiaohongshu long-form note URLs to a paid shortening service, then parse JSON task results or export CSV output for sharing and automation workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Saved bearer tokens, Xiaohongshu URLs, task data, and export requests may be sent to the configured service over plaintext HTTP by default.

Mitigation: Set an HTTPS base URL with a valid certificate before login or submission when possible, avoid untrusted networks, and rotate credentials if they may have been exposed.

Risk: TLS certificate verification can be disabled, which increases exposure to man-in-the-middle interception.

Mitigation: Keep insecure TLS disabled unless the endpoint is trusted and the network risk is understood.

Risk: The workflow depends on a third-party shortening service and account quota, so service availability, failures, and billing state can affect results.

Mitigation: Check quota before submission, review JSON failure messages, and submit only public Xiaohongshu URLs the user is comfortable sending to the service.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/mystery77777777/skills/xhs-short-url)

## Skill Output:

**Output Type(s):** [JSON, Files, Shell commands, Configuration]

**Output Format:** [stdout JSON envelopes with optional CSV export files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Progress and login guidance are written to stderr; stdout is intended for machine parsing.]

## Skill Version(s):

1.0.0 (source: server release metadata, SKILL.md frontmatter, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

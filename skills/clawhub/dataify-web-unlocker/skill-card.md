## Description:

Fetch HTML or a screenshot from a known blocked or JavaScript-rendered webpage with Dataify Web Unlocker.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dataify-server](https://clawhub.ai/user/dataify-server)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to fetch content from a specific public webpage when ordinary browsing is blocked by JavaScript rendering, CAPTCHA defenses, or SPA behavior. It is intended for known URLs, not search discovery or platform-specific structured records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Target URLs and fetched page content are sent to Dataify.

Mitigation: Use the skill only for public or intentionally disclosed targets, and avoid internal URLs or personal data unless disclosure to Dataify is intended.

Risk: Custom headers or cookies can disclose session credentials or authorization material.

Mitigation: Do not pass session cookies, authorization headers, or other sensitive request metadata unless that disclosure is explicitly intended.

Risk: Persistent shell-profile token setup leaves DATAIFY_API_TOKEN available to future shells.

Mitigation: Prefer session-scoped token setup for testing and review persistent shell changes before deploying the skill.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dataify-server/skills/dataify-web-unlocker)
- [Dataify Web Unlocker API endpoint](https://webunlocker.dataify.com/request)
- [Dataify Dashboard](https://dashboard.dataify.com?utm_source=skill)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and direct API response content]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can return HTML or screenshot-oriented page content depending on the request type; dry-run mode returns JSON request previews.]

## Skill Version(s):

1.3.0 (source: evidence.release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

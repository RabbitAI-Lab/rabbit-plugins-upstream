## Description:

Set up server side conversion tracking for ad platforms such as Google Ads, Meta, ChatGPT, LinkedIn, TikTok, and others without writing tracking code.

This skill is ready for commercial/non-commercial use.

## Publisher:

[aaronbeashel](https://clawhub.ai/user/aaronbeashel)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, marketers, and site operators use this skill to configure Converly conversion tracking, connect form or booking events to ad platforms, publish flows, and verify delivery and capture. It is intended for agents working on live tracking setup, diagnostics, and conversion result checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can configure live conversion tracking and send conversion data to advertising platforms.

Mitigation: Confirm the exact site, form, destination platform, and conversion action before publishing, and verify that privacy notices and consent handling allow hashed identifiers or click IDs to be sent.

Risk: A real test conversion may be reported to an ad platform when sandbox testing is unavailable.

Mitigation: Require explicit user agreement before using `--allow-real`, and report exactly whether delivery, loader install, or end-to-end capture was verified.

Risk: Wrong destination, trigger, domain, or conversion-action choices can reject events or corrupt attribution data.

Mitigation: List available sites, triggers, destinations, and conversion options from Converly before choosing; set the real site domain; and let the user choose the conversion action.

Risk: Account authorization and API credentials are sensitive.

Mitigation: Use browser-based `converly login` and handoff URLs where possible; only rely on `CONVERLY_API_KEY` for headless use and never print or ask the user to paste tokens.

Risk: Destructive changes can remove or interrupt live tracking.

Mitigation: Require explicit user confirmation before deleting flows, unpublishing live flows, disconnecting destinations, or issuing raw DELETE API calls.

## Reference(s):

- [Converly Developer Documentation](https://developers.converly.io)
- [Converly](https://converly.io)
- [@converly/cli package](https://www.npmjs.com/package/@converly/cli)
- [Converly MCP server](https://app.converly.io/mcp)
- [ClawHub skill page](https://clawhub.ai/aaronbeashel/skills/converly)
- [Trigger specifics](references/triggers.md)
- [Destination specifics](references/destinations.md)
- [REST API fallback](references/rest-api.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, code, API calls]

**Output Format:** [Markdown guidance with inline shell commands, JSON examples, and configuration steps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands generally return JSON; some workflows require browser handoffs and explicit user confirmation.]

## Skill Version(s):

1.1.0 (source: evidence release and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

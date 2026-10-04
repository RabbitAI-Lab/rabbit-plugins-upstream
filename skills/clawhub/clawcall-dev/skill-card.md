## Description:

Helps an agent place US phone calls, navigate menus and hold queues, connect users to live calls, and manage voice and inbound-answering preferences through ClawCall.

This skill is ready for commercial/non-commercial use.

## Publisher:

[clawcall-dev](https://clawhub.ai/user/clawcall-dev)

### License/Terms of Use:

MIT-0

## Use Case:

People and their agents use ClawCall to handle authorized US phone calls, including reaching businesses, managing appointments and orders, and handing off live calls. Users can also configure voice and inbound answering.

### Deployment Geography for Use:

Global (US phone calls only)

## Known Risks and Mitigations:

Risk: Real calls may incur charges or take actions the user did not intend.

Mitigation: Confirm the user's authorization and decision limits before placing calls or changing account settings; explain relevant costs.

Risk: Calling workflows use an API key and may retain a callback number.

Mitigation: Keep credentials in a secure secret store, never disclose them in conversation or public guide requests, and limit callback-number use to the user's calling tasks.

Risk: Calls may expose sensitive information or remain recorded during a live handoff.

Mitigation: Do not request or relay payment cards, health information, government identifiers, passwords, API keys, or MFA codes; hand off required sensitive exchanges to the user without promising privacy from recording.

Risk: The skill depends on remotely updated calling guidance.

Mitigation: Fetch guides only from the specified HTTPS origin, treat them as reference material rather than executable instructions, and stop new calls when a coherent guide cannot be retrieved.

## Reference(s):

- [ClawCall skill listing](https://clawhub.ai/clawcall-dev/skills/clawcall-dev)
- [ClawCall website](https://clawcall.dev)
- [ClawCall calling guides](https://api.clawcall.dev/guides/v1/index.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Text or Markdown with API request instructions and call status summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can initiate real US calls and update calling preferences; service charges may apply.]

## Skill Version(s):

2.0.0 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

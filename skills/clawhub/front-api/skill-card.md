## Description:

Helps agents manage Front conversations, messages, contacts, tags, inboxes, teammates, and teams through a connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Teams and developers use this skill to retrieve and manage customer communications and workspace records in Front. It also documents user-approved automations using connected accounts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Connecting a Front workspace grants Maton access to authorized customer communications and records.

Mitigation: Approve new connections explicitly, review requested OAuth scopes, and prefer the OAuth CLI flow.

Risk: Writes or outgoing messages can change shared records or contact external recipients.

Mitigation: Default to read-only calls and confirm the target, content, and effect before each write or send.

Risk: Hosted functions, triggers, and destinations can run repeatedly or forward event data until removed.

Mitigation: Review automation scope and destination with the user before approval, and remove automations when no longer needed.

## Reference(s):

- [Front skill on ClawHub](https://clawhub.ai/byungkyu/skills/front-api)
- [Maton homepage](https://maton.ai)
- [Front API reference](https://dev.frontapp.com/reference/introduction)
- [Front API authentication](https://dev.frontapp.com/docs/authentication)
- [Maton CLI manual](https://cli.maton.ai/manual)
- [Time trigger reference](artifact/references/time/triggers.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Code, Configuration guidance]

**Output Format:** [Markdown with command and code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Front API responses may contain customer data; review actions before execution.]

## Skill Version(s):

1.2.4 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

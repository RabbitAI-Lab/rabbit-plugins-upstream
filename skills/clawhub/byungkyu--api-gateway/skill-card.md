## Description:

API Gateway lets agents call third-party APIs through the Maton gateway using credentials from apps the user has already connected.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to make read-first, confirmed calls to connected SaaS APIs, manage Maton connections, and configure triggers or event delivery when users explicitly request them.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Connected app credentials may expose sensitive mailbox contents, CRM records, billing data, or meeting transcripts.

Mitigation: Install only when the publisher and connected apps are trusted, prefer OAuth with least-privilege scopes, and treat returned business data as sensitive even for read-only calls.

Risk: Writes, trigger destinations, webhook forwarding, and --exec handlers can create persistent side effects or run local automation.

Mitigation: Require explicit confirmation before those actions, specify the intended connection when multiple accounts exist, and review the destination or handler before enabling it.

## Reference(s):

- [API Gateway on ClawHub](https://clawhub.ai/byungkyu/skills/api-gateway)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, JSON examples, and API endpoint patterns.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and user-connected app credentials; writes, triggers, webhook destinations, and --exec handlers require explicit confirmation.]

## Skill Version(s):

1.0.146 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Bellwire helps agents add, test, diagnose, and maintain private-first live cards, inbox events, and phone notifications across application backends, CI/CD workflows, and shell automation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xwchris](https://clawhub.ai/user/xwchris)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use Bellwire to connect application events and repository state to private-first cards, inbox updates, and iPhone notifications. The skill guides adapter implementation, token handling, Direct endpoints, webhook flows, tests, conformance checks, and production verification.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can help an agent change application code, create Bellwire resources, manage tokens, and add runtime notification or webhook paths.

Mitigation: Require explicit confirmation before hosted-mode changes, high-priority notifications, token rotation, or project deletion, and review code changes before deployment.

Risk: Bellwire tokens may grant management or runtime notification capabilities if exposed.

Mitigation: Keep tokens in the user's approved secret store, never commit or print token values, and rotate tokens after accidental disclosure.

Risk: Hosted mode can store Event, Inbox, and Surface content in Bellwire Cloud.

Mitigation: Prefer the default Private mode unless the user explicitly approves Hosted storage.

Risk: Direct request replay protection depends on atomically consuming nonces.

Mitigation: Use database-backed atomic nonce storage and stop the integration if the target database cannot provide an atomic consume operation.

Risk: Webhook or notification side effects can affect application behavior if sent before source operations commit or if provider signatures are not verified.

Mitigation: Send Bellwire updates only after the source operation commits, use bounded best-effort calls where appropriate, verify provider signatures against the unmodified request body, and run focused tests.

## Reference(s):

- [Integration adapters](references/adapters.md)
- [Bellwire API](references/api.md)
- [Bellwire Private and Direct v2](references/direct-connections.md)
- [Event Spec](references/event-spec.md)
- [Production verification](references/production-verification.md)
- [Security](references/security.md)
- [Bellwire live Surfaces](references/surfaces.md)
- [Troubleshooting](references/troubleshooting.md)
- [Provider webhook adapters](references/webhooks.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands, code snippets, configuration examples, and verification guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include generated adapter files, Bellwire CLI operations, focused test instructions, and production verification steps.]

## Skill Version(s):

1.0.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

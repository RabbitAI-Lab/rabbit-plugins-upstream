## Description:

Use when integrating Outlit tracking into web, server, native, or desktop apps; adding SDK event tracking, identity, consent, activation configuration, billing integrations, visitor tracking, customerId attribution, or troubleshooting @outlit/browser, @outlit/node, or the Rust outlit crate.

This skill is ready for commercial/non-commercial use.

## Publisher:

[leo-paz](https://clawhub.ai/user/leo-paz)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to add and troubleshoot Outlit analytics instrumentation across browser, server, native, and desktop applications. It guides SDK selection, identity setup, consent handling, activation events, billing integration decisions, and verification steps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill helps add analytics tracking that may collect events, identifiers, form-derived identity fields, and properties.

Mitigation: Review planned tracking behavior before installation, decide whether consent gating is required, and avoid sending secrets or unnecessary personal data.

Risk: Automatic browser tracking can create visitor storage before a user has consented when configured with default tracking behavior.

Mitigation: Use consent-gated tracking where required by the target app's policy or geography, such as initializing with tracking disabled and enabling it only after consent.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/leo-paz/skills/outlit-sdk)
- [Outlit Tracking Quickstart](https://docs.outlit.ai/tracking/quickstart)
- [How Outlit Tracking Works](https://docs.outlit.ai/tracking/how-it-works)
- [Customer Context Graph](https://docs.outlit.ai/concepts/customer-context-graph)
- [Website Visitors](https://docs.outlit.ai/concepts/website-visitors)
- [Identity Resolution](https://docs.outlit.ai/concepts/identity-resolution)
- [Browser SDK](https://docs.outlit.ai/tracking/browser/npm)
- [React Tracking](https://docs.outlit.ai/tracking/browser/react)
- [Next.js Tracking](https://docs.outlit.ai/tracking/browser/nextjs)
- [Node.js Tracking](https://docs.outlit.ai/tracking/server/nodejs)
- [Rust and Tauri Tracking](https://docs.outlit.ai/tracking/server/rust)
- [Ingest API](https://docs.outlit.ai/api-reference/ingest)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline code examples and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill produces integration guidance and proposed code or configuration changes for the target application; it does not produce executable artifacts by itself.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

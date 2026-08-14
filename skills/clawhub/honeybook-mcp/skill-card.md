## Description:

Provides HoneyBook client-portal assistance for viewing vendor contracts, invoices, files, workspaces, payment methods, and deep links for signing or payment.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

People managing HoneyBook wedding-vendor portals use this skill through an agent to capture magic-link sessions, review contract and invoice status, inspect shared files and payment methods, and request deep links for signing or payment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill captures HoneyBook magic-link sessions and stores session data locally, which can expose sensitive portal access if the host account or session file is mishandled.

Mitigation: Install it only for intended HoneyBook portal workflows, keep local session storage protected, and capture sessions only from trusted vendor magic-link emails.

Risk: Broad wording around contracts, invoices, vendors, and payments could activate the skill for unrelated requests.

Mitigation: Use explicit HoneyBook wording before invoking the skill and require confirmation before returning signing or payment deep links.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/honeybook-mcp)

## Skill Output:

**Output Type(s):** [Guidance, API Calls, Links]

**Output Format:** [Markdown or plain text with tool-call results and portal deep links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Signing and payment link requests require explicit confirmation.]

## Skill Version(s):

0.4.6 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

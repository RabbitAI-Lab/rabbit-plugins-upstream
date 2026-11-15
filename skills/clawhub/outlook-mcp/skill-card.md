## Description:

Production-grade MCP server for personal Outlook (Outlook.com / Hotmail / Live). 77 typed Graph tools across mail, inbox rules, calendar, contacts, to-do, drafts, attachments, folders, threading, batch ops, delta-sync. Granular permissions, OS-keyring auth, /$batch-optimized triage and bulk read. Built for agents that need real Outlook coverage, not a CLI wrapper. BYO Azure app; zero telemetry.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mpalermiti](https://clawhub.ai/user/mpalermiti)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent builders use this MCP server to connect personal Outlook accounts to AI agents for mail, calendar, contact, and task workflows, including reading, triage, drafting, and user-authorized changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan reports a suspicious token-forwarding risk involving an authenticated request redirected by a Graph response, along with instruction-scope concerns; its inspection was partial.

Mitigation: Wait for the reported risk and action guidance to be reviewed. If installing meanwhile, use a specific reviewed version and enable only the Outlook actions and permissions needed; treat the partial scan as incomplete coverage.

## Reference(s):


## Skill Output:

**Output Type(s):** [Text, JSON, Files]

**Output Format:** [Structured tool results, text, and optional attachment content]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on the selected Outlook action; attachment content may be returned or saved to the configured attachments folder.]

## Skill Version(s):

1.32.0 (source: release evidence, server.json, pyproject.toml)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

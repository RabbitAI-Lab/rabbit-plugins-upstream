## Description:

Turn a Douyin link, keyword, or pasted Douyin counts and comments into a one-page attributed brief with engagement figures, hook, a verbatim audience line, and a follow-or-not call.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to summarize a Douyin post or keyword into an attributed, same-day brief. The skill can work from user-supplied material or, after explicit paid confirmation, from public Douyin lookups through Beatra.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a shared full-scope Beatra device authorization and local credential file.

Mitigation: Install only where shared Beatra authorization is acceptable, protect the local credential store, and use the bundled uninstall flow or Beatra Console revocation when disconnecting.

Risk: The bundled client can silently install verified package updates before ordinary commands.

Mitigation: Review this behavior before installing and disable automatic updates with `python3 scripts/mcp_client.py update --auto off` in environments that require manual update approval.

Risk: Optional Douyin lookups are paid and repeated pages or changed arguments can create additional charges.

Mitigation: Require explicit confirmation for each lookup, quote the live credit price first, keep one stable client_request_id for recovery, and report billing.net_charged_credits from terminal task results.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/beatra-ai/skills/douyin-data-brief)
- [Beatra skill homepage](https://beatra.ai/skills/douyin-data-brief)
- [Looking up Douyin](references/douyin-lookup.md)
- [Writing the brief](references/brief.md)
- [Douyin brief workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Tasks and results](references/tasks-and-results.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown brief with attributed figures and optional shell-command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include task IDs, terminal status, returned payload details, and billing.net_charged_credits when a paid lookup runs.]

## Skill Version(s):

0.1.1 (source: server release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Turn user-supplied risk-grade definitions into a four-to-eight still risk grade set.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and wealth content teams use this skill to turn approved risk-grade definitions into a consistent pack of still graphics, one per grade. It helps produce risk grade cards without inventing missing ratings, return figures, or investment claims.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill stores a shared Beatra bearer credential in ~/.beatra and can use broad Beatra account permissions.

Mitigation: Install only if the publisher is trusted, keep the credential out of chat, logs, arguments, and environment variables, and revoke or uninstall access when it is no longer needed.

Risk: Billable image generation can spend Beatra credits.

Mitigation: Require explicit approval before paid generation, read live model pricing before submission, use one request identity per still, and report the returned net charged credits.

Risk: Selected local reference files may be uploaded to Beatra.

Mitigation: Upload only files the user intentionally provides as references and do not use scans or photos to invent missing risk-grade definitions.

Risk: Automatic updates are enabled by default and can silently replace package-owned files.

Mitigation: Review the skill before installation and consider disabling automatic updates with scripts/mcp_client.py update --auto off after installation.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/beatra-ai/skills/risk-grade-set)
- [Risk-grade pack workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [MCP connection](references/mcp-connection.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Files, Guidance]

**Output Format:** [Markdown pack lists and task summaries with generated image artifacts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [One generated still per named grade, normally four to eight stills, with returned task IDs, resolved models, dimensions, formats, and net charged credits.]

## Skill Version(s):

0.1.2 (source: server release evidence and manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

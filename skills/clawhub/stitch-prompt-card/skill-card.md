## Description:

Turn a public TikTok stitch target into one quote reply card per chosen hook, using supplied reply lines plus pasted or approved lookup caption and comment content.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and social media operators use this skill to plan and generate TikTok quote reply stills from supplied reply lines, public TikTok captions, and comments. It can use pasted content directly or, after approval, paid Beatra lookups and image generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a shared Beatra credential with broad media, wallet, artifact, and task permissions.

Mitigation: Review the requested authorization before installation, keep the credential private, and revoke the Beatra device authorization from the console when the skill is no longer needed.

Risk: Paid lookups and image generation can spend Beatra credits.

Mitigation: Approve only paid operations whose live price and work description are understood, and use the skill's task recovery guidance to avoid duplicate paid submissions after uncertain transport failures.

Risk: The bundled client can silently replace its own installed package code during automatic updates.

Mitigation: Disable automatic updates with the documented `python3 scripts/mcp_client.py update --auto off` command when this update posture is unacceptable.

## Reference(s):

- [Stitch prompt workflow](references/workflow.md)
- [Comment lookup](references/comment-lookup.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Tasks and results](references/tasks-and-results.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [MCP connection](references/mcp-connection.md)
- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/stitch-prompt-card)
- [Beatra skill homepage](https://beatra.ai/skills/stitch-prompt-card)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Files, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and returned image artifact references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can produce 1 to 6 quote reply stills, plus task status and billing details returned by Beatra.]

## Skill Version(s):

0.1.2 (source: server release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Create Xiaohongshu or REDnote copy from a product, experience, topic, or audience brief. This AI Xiaohongshu copywriter produces title options, a structured note body, cover wording, relevant hashtags, and a natural comment starter for product discovery, local experiences, beauty, food, fashion, travel, and knowledge posts. It then renders a matching vertical 3:4 Xiaohongshu cover built around the chosen title, with a headline-safe composition. Optionally it reads Xiaohongshu itself — the notes already running for the topic, one page of a note's top comments, and an account's own recent notes — so Xiaohongshu research, competitor note analysis and comment analysis rest on the platform instead of on guesswork.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, and social commerce operators use this skill to turn product, experience, topic, or audience briefs into Xiaohongshu/REDnote titles, post copy, cover wording, hashtags, and a comment starter. With explicit approval, it can also perform paid Xiaohongshu lookups and produce one matching 3:4 cover image through Beatra.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installation grants a shared Beatra Device Token with broad account, wallet-spending, media, model, upload, and task authority.

Mitigation: Install only when that authority is acceptable, keep the token out of logs and prompts, and revoke or uninstall through the bundled disconnect flow when access is no longer needed.

Risk: The bundled client checks for package updates silently by default and can replace package-owned files without a separate approval prompt.

Mitigation: Disable automatic updates with `python3 scripts/mcp_client.py update --auto off` when manual review is required, and use `python3 scripts/mcp_client.py update --check` before updating.

Risk: Optional Xiaohongshu lookup and cover generation are paid Beatra operations, so careless retries or extra pages can spend credits.

Mitigation: Require a clear per-operation approval, reuse the same `client_request_id` only for byte-identical recovery, poll existing tasks before retrying, and report `billing.net_charged_credits` from terminal task results.

Risk: The security verdict is suspicious because the Beatra authority and silent self-updates go beyond the narrow copywriting purpose.

Mitigation: Review the package before installing, consider disabling automatic updates, and use the skill only where those permissions match the user's risk tolerance.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/beatra-ai/skills/zhongcao-note-copywriter)
- [Beatra skill homepage](https://beatra.ai/skills/zhongcao-note-copywriter)
- [REDnote note copy workflow](references/workflow.md)
- [Reading Xiaohongshu](references/note-lookup.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Shell commands, API Calls, Files]

**Output Format:** [Markdown copy drafts with inline shell commands and generated artifact links when paid media work is approved]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces five title options, a selected note body, cover wording, hashtags, a comment starter, marked assumptions, and optional Beatra task results.]

## Skill Version(s):

0.1.3 (source: server release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Browser automation fallback through the magicbrowse CLI with goal-driven act as the default primitive and observe/primitives only for recovery, with changed page state verified by fresh observation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xor777](https://clawhub.ai/user/xor777)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use MagicBrowse when their native page-control tool cannot reliably reach or inspect a public web page. The skill guides browser navigation, controlled recovery with lower-level primitives, and handoff at approval, authentication, CAPTCHA, identity, payment, or other sensitive boundaries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Browser page context and screenshots can be sent to the MagicBrowse gateway during LLM-backed navigation.

Mitigation: Use the skill for public or explicitly approved workflows, avoid private pages unless approved, and require explicit approval before using vision mode on sensitive pages.

Risk: Attached browser profiles or CDP endpoints may carry the user's logged-in authority.

Mitigation: Prefer a fresh owned browser session, keep CDP endpoints private, and attach to existing profiles or browsers only after user approval for the current task.

Risk: Browser automation can reach pages where the next action would submit, purchase, post, delete, or otherwise change external state.

Mitigation: Stop before consequential actions, ask for explicit approval on the current visible page state, re-observe after approval, and execute only the approved final action.

Risk: The workflow may encounter credentials, identity data, payment fields, CAPTCHA, or other human-verification barriers.

Mitigation: Stop and hand off at those boundaries; do not invent credentials, identity values, payment values, CAPTCHA answers, or memory-managed data.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/xor777/skills/magicbrowse)
- [MagicBrowse OpenClaw Marketplace README](https://github.com/nuanu-ai/skills/blob/main/docs/magicbrowse/openclaw/marketplace/README.md)
- [MagicBrowse CLI Package](https://www.npmjs.com/package/@nuanu-ai/magicbrowse-cli)
- [MagicBrowse Command Guide](references/commands.md)
- [MagicBrowse Guardrails](references/guardrails.md)
- [MagicBrowse Statuses](references/statuses.md)
- [MagicBrowse Worked Example](references/workflow.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces browser automation instructions and status-handling guidance; does not itself return harvested page content.]

## Skill Version(s):

0.1.19 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

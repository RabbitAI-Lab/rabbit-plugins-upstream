## Description:

Create Xiaohongshu beauty and skincare content from product facts, routine steps, skin concerns, and audience context, including a 3:4 post concept, review structure, usage-scene copy, title options, cover wording, hashtags, a comment starter, and optional Xiaohongshu note and comment lookups.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, and operators use this skill to turn supplied beauty or skincare product facts into Xiaohongshu-ready post copy, a 3:4 slide plan, titles, cover wording, hashtags, and assumptions to confirm. When explicitly approved, it can add Xiaohongshu lookup results for competitor-note and comment analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The package uses a shared Beatra Device Token with broad service scopes.

Mitigation: Install only after reviewing the Beatra account and credential policy, and avoid restricted or enterprise environments unless the requested authority is acceptable.

Risk: Optional Xiaohongshu lookups can spend wallet credits.

Mitigation: Run paid lookups only after the user explicitly requests and approves each lookup and its quoted credit price.

Risk: Silent package updates are enabled by default.

Mitigation: Disable automatic updates before use when change control or release review is required.

Risk: Beauty and skincare copy can create publication risk if it includes unsupported efficacy, medical, absolute, or outcome claims.

Mitigation: Use the built-in beauty copy screen, preserve unsupported claims as questions or assumptions, and rewrite claims around supplied facts.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/zhongcao-beauty-note-maker)
- [Beatra skill homepage](https://beatra.ai/skills/zhongcao-beauty-note-maker)
- [Beauty note workflow](references/workflow.md)
- [Reading Xiaohongshu](references/note-lookup.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [MCP connection](references/mcp-connection.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with structured Chinese copy, a 3:4 slide plan, hashtags, assumptions, and occasional shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional Xiaohongshu lookups may add sourced research notes, task IDs, terminal status, and billed credit totals after user approval.]

## Skill Version(s):

0.1.2 (source: release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

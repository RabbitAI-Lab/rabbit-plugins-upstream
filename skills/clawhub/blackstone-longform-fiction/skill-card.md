## Description:

A Chinese-language longform fiction writing assistant that helps authors develop ideas, characters, themes, structure, settings, prose, chapter plans, revisions, continuations, and continuity checks, with optional Blackstone cloud story memory for cross-chapter recall.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jony4](https://clawhub.ai/user/jony4)

### License/Terms of Use:

MIT-0

## Use Case:

External authors use this skill to plan, draft, continue, revise, polish, and diagnose medium- and long-form fiction, including web novels and serialized stories. It can work locally with user-selected manuscript files and can optionally use Blackstone cloud story memory when the author authorizes account and story-graph features.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional cloud story memory, account authorization, feedback submission, and billing flows can send selected story or account-related data to Blackstone services.

Mitigation: Keep the default per-action confirmation mode, review what will be read or uploaded before each cloud operation, and decline cloud setup for local-only writing.

Risk: The skill can write or modify manuscript files selected by the author.

Mitigation: Confirm the target file and edit range before writing, restrict reads to task-relevant manuscript content, and verify the result after local file changes.

Risk: The skill includes a consent-based self-update flow.

Mitigation: Decline updates unless you want them, and only proceed after the skill states the target version, affected skill directory, and hash verification outcome.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/jony4/skills/blackstone-longform-fiction)
- [Publisher profile](https://clawhub.ai/user/jony4)
- [Blackstone homepage](https://blackstone.wansu.tech)
- [Blackstone longform fiction edition](https://blackstone.wansu.tech/longform)
- [Security boundaries](references/security.md)
- [Quickstart](references/quickstart.md)
- [Local file handling](references/local-files.md)
- [Cloud story memory](references/mcp.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance, code, shell commands, configuration]

**Output Format:** [Markdown responses with optional prose drafts, diagnostic notes, local file edits, shell commands for opening authorization or payment pages, and configuration guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include Chinese fiction prose, story plans, continuity analysis, revision suggestions, account or billing guidance, and explicit consent prompts before cloud memory, update, or local file operations.]

## Skill Version(s):

1.3.3 (source: SKILL.md frontmatter, VERSION.md, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Antigravity CLI helps agents use Google's agy coding assistant for code generation, refactoring, debugging, review, test generation, documentation, and multi-file programming tasks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[akdira](https://clawhub.ai/user/akdira)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineering agents use this skill to route programming work to Google Antigravity CLI for project-aware code generation, code review, debugging, refactoring, test generation, and configuration guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote installer guidance can execute code fetched from a network source.

Mitigation: Review the installer before running it and install only when intentionally enabling Google Antigravity CLI.

Risk: Coding tasks and repository context may be sent to a networked Google AI agent.

Mitigation: Avoid sensitive or proprietary repositories unless approved for Google AI processing, and use narrow --add-dir scopes.

Risk: Autonomous edit modes can change files across a project.

Mitigation: Prefer plan or review modes before accept-edits, work from version control or a disposable branch, and review changes before deployment.

## Reference(s):

- [Antigravity CLI official docs](https://antigravity.google/docs/)
- [Google Antigravity](https://antigravity.google)
- [Antigravity CLI install script](https://antigravity.google/cli/install.sh)
- [Google AI Studio](https://aistudio.google.com/)
- [Gemini API rate limits](https://ai.google.dev/gemini-api/docs/rate-limits)
- [Antigravity CLI GitHub repository](https://github.com/google-antigravity/antigravity-cli)
- [ClawHub skill page](https://clawhub.ai/akdira/skills/antigravity-cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Plain text, Markdown, JSON, stream JSON, and shell-command snippets depending on agy flags and the user's prompt.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can provide project-aware coding guidance and may propose or apply file edits when the underlying CLI is run with edit-accepting modes.]

## Skill Version(s):

1.0.0 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

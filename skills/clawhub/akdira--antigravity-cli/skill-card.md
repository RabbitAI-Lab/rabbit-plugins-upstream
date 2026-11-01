## Description:

Google Antigravity CLI (agy) is an autonomous coding-agent helper for code generation, refactoring, review, debugging, testing, and multi-step programming tasks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[akdira](https://clawhub.ai/user/akdira)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineers use this skill to invoke Google's Antigravity CLI for code generation, code review, refactoring, debugging, documentation, and test generation against local project context.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote installer commands can execute third-party code during setup.

Mitigation: Download and inspect installers before running them, and prefer verified installer artifacts over piping scripts directly to a shell.

Risk: Permission-bypass or auto-apply modes can allow an external coding agent to change local files without normal review.

Mitigation: Use plan or review modes by default, keep `--add-dir` narrowly scoped, and reserve bypass flags for disposable sandboxes.

Risk: Prompts and project context may be sent to Google AI endpoints and may include confidential code or secrets.

Mitigation: Exclude secrets and confidential repositories unless the relevant Google account, billing, and data-handling implications are approved.

Risk: Cached OAuth credentials or API keys can grant continued access after initial setup.

Mitigation: Protect local credential files and environment variables, rotate compromised keys, and remove cached tokens when access is no longer needed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/akdira/skills/antigravity-cli)
- [Publisher Profile](https://clawhub.ai/user/akdira)
- [Antigravity Homepage](https://antigravity.google)
- [Antigravity CLI Install Script](https://antigravity.google/cli/install.sh)
- [Antigravity Documentation](https://antigravity.google/docs/)
- [Google AI Studio](https://aistudio.google.com/)
- [Gemini API Rate Limits](https://ai.google.dev/gemini-api/docs/rate-limits)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands, code snippets, and optional JSON or streaming JSON output from the delegated CLI.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may depend on the installed agy binary, model availability, authentication method, network access to Google AI endpoints, and scoped project directories.]

## Skill Version(s):

1.0.0 (source: frontmatter, release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

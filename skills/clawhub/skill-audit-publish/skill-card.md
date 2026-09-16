## Description:

Skill Audit & Publish guides agents through an audit-first workflow for sanitizing, verifying, publishing, and install-checking OpenClaw skills on ClawHub with explicit user approval before irreversible steps.

This skill is ready for commercial/non-commercial use.

## Publisher:

[haiyangchenbj](https://clawhub.ai/user/haiyangchenbj)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and skill authors use this skill to prepare public ClawHub releases by transforming source skills, scanning for private data, secrets, model-specific references, and internal paths, then publishing only after review and explicit approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Publishing mode transmits cleaned skill contents to public ClawHub and GitHub services.

Mitigation: Require audit completion, explicit user approval of file list and destinations, and post-publish install-check before reporting success.

Risk: The optional GitHub sync helper requires a GitHub token and writes files to a repository.

Mitigation: Use a least-privileged token from environment variables only, review the exact file list, and rely on the helper's create/update-only behavior.

Risk: Running an unpinned one-shot ClawHub CLI can pull mutable third-party code at publish time.

Mitigation: Prefer a pinned or locally installed reviewed ClawHub CLI before executing publish or install-check commands.

Risk: Removed files are not deleted by the GitHub sync helper, so stale public files can remain after a restructure.

Mitigation: Audit the remote repository file list after major changes and delete obsolete files manually.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/haiyangchenbj/skills/skill-audit-publish)
- [Publish Rules for ClawHub & GitHub](artifact/references/publish-rules.md)
- [Sanitization Checklist](artifact/sanitize.md)
- [Verification Workflow](artifact/verify.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and generated skill release files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce a publish folder, file manifest, sanitized skill files, approval message, audit findings, and optional GitHub sync command guidance.]

## Skill Version(s):

1.5.7 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

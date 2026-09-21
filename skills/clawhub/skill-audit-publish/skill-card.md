## Description:

Skill Audit & Publish guides agents through an audit-first workflow for sanitizing, verifying, and publishing OpenClaw skills to ClawHub, SkillHub, and GitHub with explicit approval before external side effects.

This skill is ready for commercial/non-commercial use.

## Publisher:

[haiyangchenbj](https://clawhub.ai/user/haiyangchenbj)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and skill maintainers use this skill to prepare SKILL.md-based OpenClaw skills for public release. It helps audit for personal data and credentials, stage a publish-ready folder, confirm exact release metadata, and publish only after explicit approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Publishing can make skill files publicly visible, including accidental personal data, credentials, or internal references.

Mitigation: Run the sanitize checklist, review the exact file list and diff, and require explicit approval before publishing.

Risk: The workflow may use GitHub credentials from GITHUB_TOKEN or GITHUB_PAT and a SkillHub token from ~/.skillhub/credentials.json for authenticated uploads.

Mitigation: Use deliberately scoped credentials, keep tokens outside published files, and confirm the destination platforms and repositories before any command runs.

Risk: The GitHub sync helper creates or updates files but does not delete remote files that were removed from a release.

Mitigation: After major restructures, audit the remote repository file list and remove obsolete files manually.

Risk: SkillHub has no read API and version drift across ClawHub, SkillHub, and GitHub can make later releases harder to verify.

Mitigation: Keep one version across all platforms and use ClawHub inspect output plus the GitHub mirror as side evidence.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/haiyangchenbj/skills/skill-audit-publish)
- [README](README.md)
- [Sanitize checklist](sanitize.md)
- [Publish rules](references/publish-rules.md)
- [SkillHub publish procedure](references/skillhub-publish.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with command snippets and generated publish-folder files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose external publish and sync commands only after audit, verification, and explicit user approval.]

## Skill Version(s):

1.5.9 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

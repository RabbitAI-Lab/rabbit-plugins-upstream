## Description:

Skill Audit & Publish guides agents through an audit-first ClawHub publishing workflow for OpenClaw skills, including sanitization, transformation, verification, explicit approval, publish commands, and install checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[haiyangchenbj](https://clawhub.ai/user/haiyangchenbj)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and skill publishers use this agent skill to prepare OpenClaw skills for ClawHub release with a reviewable audit trail. It helps sanitize private data and credentials, restructure release files, verify slug/name/version/file metadata, request explicit approval, publish, and perform an install check.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Outdated or loose publishing documentation could lead a user to approve the wrong diff, file list, slug, name, version, or description.

Mitigation: Before approving any publish, review the generated diff, file list, sanitized text sample, slug, name, version, and description.

Risk: GitHub publishing could occur when the user only intended a ClawHub release because the main workflow does not document that destination clearly.

Mitigation: Do not allow GitHub publishing unless the user explicitly requested it.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/haiyangchenbj/skills/skill-audit-publish)
- [Skill Definition](artifact/SKILL.md)
- [Sanitization Checklist](artifact/sanitize.md)
- [Transforming Content to Skill Format](artifact/transform.md)
- [Pre-Publish Verification](artifact/verify.md)
- [Chinese README](artifact/README_zh.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with file manifests, checklist results, approval text, and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a publish folder and approval message; publishing is held until explicit user approval.]

## Skill Version(s):

1.1.6 (source: SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

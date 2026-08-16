## Description:

Audit-first pipeline for preparing and publishing OpenClaw skills to ClawHub with structured sanitization, verification, explicit approval, and post-publish install checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[haiyangchenbj](https://clawhub.ai/user/haiyangchenbj)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and skill authors use this skill to prepare a publish-ready ClawHub release while checking for personal data, credentials, model-specific references, internal paths, and risky publish mistakes. It is intended for normal public ClawHub publishing workflows that require reviewable staging and explicit approval before upload.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A skill release may unintentionally publish personal data, credentials, internal paths, or inappropriate model-specific references.

Mitigation: Run the sanitization checklist, review all kept-with-reason items, and treat uncertain content as remove-or-genericize before approving publication.

Risk: A wrong slug, version, description, or file set can publish publicly if the approval step is skipped or rushed.

Mitigation: Review the generated publish folder, slug, version, description, and full file list, then require explicit approval before running the publish command.

Risk: The transform guidance contains an include-by-default note that could conflict with conservative sanitization.

Mitigation: Use the security guidance as authoritative for publish readiness and prefer removal or genericization for uncertain sensitive content.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/haiyangchenbj/skills/skill-audit-publish)
- [sanitize.md](artifact/sanitize.md)
- [transform.md](artifact/transform.md)
- [verify.md](artifact/verify.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown text with inline shell commands, staged file manifests, approval summaries, and verification guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce a local publish folder plan, sanitization checklist outcomes, explicit approval message, publish command, and install-check guidance.]

## Skill Version(s):

1.3.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

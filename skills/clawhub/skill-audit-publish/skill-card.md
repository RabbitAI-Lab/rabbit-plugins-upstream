## Description:

Audit-first pipeline to publish an OpenClaw skill to ClawHub without leaking personal data, credentials, or model-specific references.

This skill is ready for commercial/non-commercial use.

## Publisher:

[haiyangchenbj](https://clawhub.ai/user/haiyangchenbj)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and skill publishers use this skill to audit, sanitize, transform, verify, publish, and install-check OpenClaw skills for ClawHub releases. It is intended for public publishing workflows that need explicit approval before irreversible publication steps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Public publishing workflows can expose personal data, credentials, or incorrect release metadata if the audit and approval steps are skipped.

Mitigation: Run the sanitize and verification stages before every publish, require explicit approval for each release including patches, and treat published content as public.

Risk: The GitHub sync helper can upload unintended local files when the --files option is used without path enforcement inside the intended publish folder.

Mitigation: Avoid the helper's --files option until path enforcement is confirmed; publish from a reviewed staging folder with a minimal file list.

Risk: The server security verdict is suspicious because approval and deletion guidance is inconsistent across the release evidence.

Mitigation: Follow the stricter posture: require explicit approval before publishing, prefer upsert-only GitHub sync behavior, and review remote file lists after publication.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/haiyangchenbj/skills/skill-audit-publish)
- [Publish rules](references/publish-rules.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown guidance with file manifests, approval messages, command examples, and optional JavaScript helper code]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can produce a publish folder, rewritten SKILL.md frontmatter, auxiliary audit files, _meta.json, and post-publish verification guidance.]

## Skill Version(s):

1.5.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

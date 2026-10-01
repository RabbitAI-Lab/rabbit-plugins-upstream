## Description:

Helps developers validate and publish skills to Tencent SkillHub or ClawHub, and configure manual, tag-based, or change-triggered releases.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mc0571](https://clawhub.ai/user/mc0571)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and release maintainers use this skill to preflight and publish one or more skills to Tencent SkillHub or ClawHub, configure GitHub Actions releases, and troubleshoot publishing failures.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The CI template runs an unpinned remote SkillHub installer in release jobs with access to publishing secrets.

Mitigation: Replace it with a pinned, checksum-verified CLI installation before copying or running the template.

Risk: Publishing credentials may be exposed or used by an unintended release job.

Mitigation: Keep GitHub Environment approval for publish jobs and scope secrets to release environments.

Risk: Tencent SkillHub publishing could use an unintended publisher identity.

Mitigation: Verify the expected SkillHub publisher before formal publication.

## Reference(s):

- [ClawHub release guide](artifact/references/clawhub-release.md)
- [Tencent SkillHub release guide](artifact/references/skillhub-release.md)
- [GitHub Actions release guide](artifact/references/github-actions.md)
- [ClawHub publishing documentation](https://github.com/openclaw/clawhub/blob/main/docs/publishing.md)
- [Tencent SkillHub agent publishing guide](https://skillhub.cn/ai/release.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Markdown]

**Output Format:** [Markdown with shell and YAML examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports preflight, publication, and review status separately for each platform; modifies CI configuration only when requested.]

## Skill Version(s):

0.6.0 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

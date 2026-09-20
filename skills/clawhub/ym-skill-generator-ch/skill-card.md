## Description:

Skill Generator helps agents generate skill skeletons, audit and sanitize skill directories, package distributable releases, manage versions, and prepare compliant skill icons.

This skill is ready for commercial/non-commercial use.

## Publisher:

[liuyuming0823](https://clawhub.ai/user/liuyuming0823)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent builders use this skill to create new agent skills, audit existing skill directories for packaging and release risks, generate supporting templates or scripts, and prepare bundles for local installation or marketplace distribution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Packaging untrusted skill folders can expose the user to misleading or unsafe package contents.

Mitigation: Use the skill only on skill directories you trust or have reviewed, and inspect audit output before installing or distributing generated packages.

Risk: Symlink handling can allow a package operation to include or act on files outside the intended skill root.

Mitigation: Reject symlinks or resolve them within the skill root before packaging third-party directories.

Risk: Package-owned ignore rules can suppress high-severity audit findings.

Mitigation: Do not allow packaged .skillignore entries to suppress P0 or security rules without independent human review.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/liuyuming0823/skills/ym-skill-generator-ch)
- [Server-resolved GitHub Repository](https://github.com/liuyuming0823/ym-skill-generator)
- [README](artifact/README.md)
- [Generation Guide](artifact/references/generation-guide.md)
- [Audit Checklist](artifact/references/checklist.md)
- [Sanitize Rules](artifact/references/sanitize-rules.md)
- [Publishing Guide](artifact/references/publishing.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with inline shell commands, generated skill files, configuration templates, audit reports, and packaged archives]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or modify skill directories, templates, scripts, version history, icons, and distributable zip packages.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

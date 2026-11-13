## Description:

Quickly open-source a local skill to GitHub as the primary target and optionally clawhub.com, with slug checks, copy-based release preparation, internal-information scanning, license and README generation, git setup, GitHub push support, and optional hub publishing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[songhonglei](https://clawhub.ai/user/songhonglei)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineers use this skill to prepare a local agent skill for public release by creating an open-source copy, scanning for internal or sensitive content, normalizing release files, and publishing to GitHub or optional skill hubs after review checkpoints.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can commit or upload sensitive files before a strict safety review.

Mitigation: Run strip_scan.sh --strict, inspect the generated fork and file list, and remove sensitive findings from both the working tree and git history before any push or publish step.

Risk: Plaintext publishing tokens can be exposed if stored in profile configuration or release artifacts.

Mitigation: Prefer one-time environment variables or command-backed token sources, avoid plaintext token storage, and revoke temporary personal access tokens after use.

Risk: Publishing a single-skill fork directly to a mono-repo can overwrite unrelated repository contents.

Mitigation: Use the documented mono-repo subdirectory workflow unless the user explicitly confirms that overwriting the target repository is intended.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/songhonglei/skills/opensource-skill-to-github)
- [Repository path](https://github.com/Songhonglei/build-better-skills/tree/main/skills/opensource-skill-to-github)
- [build-better-skills suite README](https://github.com/Songhonglei/build-better-skills#stages)
- [Open-source playbook](references/opensource_playbook.md)
- [Strip checklist](references/strip_checklist.md)
- [UGLIC quick reference](references/uglic_quickref.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, code, configuration, markdown]

**Output Format:** [Markdown guidance with inline shell commands and generated release files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce or modify a forked skill directory, release documentation, license files, git commits, and publishing commands after user review.]

## Skill Version(s):

1.0.18 (source: frontmatter and server release, released 2026-09-05)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

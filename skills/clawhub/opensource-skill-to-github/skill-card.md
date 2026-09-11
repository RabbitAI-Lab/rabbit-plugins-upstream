## Description:

Helps developers open-source a local agent skill to GitHub, with optional ClawHub publishing, by guiding slug checks, fork creation, internal-information scanning, metadata normalization, license and README generation, git initialization, and authenticated publishing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[songhonglei](https://clawhub.ai/user/songhonglei)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to prepare a local agent skill for public release, including copying it into an open-source fork, scanning for internal information, generating release files, initializing git, and publishing to GitHub or a skill hub with credential hygiene checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The publishing workflow can use stored or temporary credentials for GitHub and skill hub publishing.

Mitigation: Prefer a trusted token command or GitHub CLI token source, avoid plaintext PATs in profile.env, pass temporary tokens through environment variables only, and revoke temporary tokens after use.

Risk: Public publishing can expose unintended local files or internal information.

Mitigation: Manually review the fork contents, run the strip scan in strict mode, and continue only after the printed file list and scan results are clean.

Risk: An optional skillhub.cn publish path may upload unexpected files if the package contents are not reviewed.

Mitigation: Avoid skillhub.cn publishing unless the script output and file list are clean and the user explicitly intends to publish through that channel.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/songhonglei/skills/opensource-skill-to-github)
- [Open-Sourcing a Skill Playbook](references/opensource_playbook.md)
- [Strip Checklist](references/strip_checklist.md)
- [UGLIC Quick Reference](references/uglic_quickref.md)
- [Precedents](references/precedents.md)
- [README Template](references/readme_template.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline bash commands and generated project files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces publishing workflows that may execute local scripts and external publish commands when the user approves them.]

## Skill Version(s):

1.0.18 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

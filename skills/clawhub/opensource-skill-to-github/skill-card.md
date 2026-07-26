## Description: <br>
Helps developers open-source local agent skills to GitHub and optionally ClawHub by guiding copy creation, stripping checks, metadata normalization, licensing, git setup, push, and publishing steps. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[songhonglei](https://clawhub.ai/user/songhonglei) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to prepare a local agent skill for public release, including creating a separate open-source copy, checking for internal or sensitive content, generating public-facing files, initializing git, and publishing to GitHub or supported skill hubs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Credential handling is part of the publishing workflow and may be broader than expected. <br>
Mitigation: Use short-lived or least-privilege tokens, prefer gh auth token or a keychain over plaintext OSG_GITHUB_TOKEN, and revoke temporary tokens after use. <br>
Risk: Automatic cleanup and exclusion behavior may remove or omit files before publishing. <br>
Mitigation: Review the generated fork, inspect any .osg-exclude file, and check the commit before pushing or publishing. <br>
Risk: Suggested memory notes could accidentally capture sensitive internal details. <br>
Mitigation: Avoid writing secrets, internal hosts, private paths, or sensitive organizational context into memory notes. <br>


## Reference(s): <br>
- [ClawHub release page](https://clawhub.ai/songhonglei/skills/opensource-skill-to-github) <br>
- [Open-Sourcing a Skill - Full Playbook](references/opensource_playbook.md) <br>
- [11-rule stripping checklist](references/strip_checklist.md) <br>
- [UGLIC quick reference](references/uglic_quickref.md) <br>
- [README template](references/readme_template.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, Code] <br>
**Output Format:** [Markdown with inline bash code blocks and script-driven file changes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes decision checkpoints for license choice, slug conflicts, sensitive-content findings, and token handling.] <br>

## Skill Version(s): <br>
1.0.13 (source: server release metadata and SKILL.md, released 2026-07-22 in CHANGELOG.md) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

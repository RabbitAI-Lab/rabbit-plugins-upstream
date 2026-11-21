## Description:

Audit locally installed agent skills for security/policy issues using the SkillLens CLI (`skilllens scan`, `skilllens config`).

This skill is ready for commercial/non-commercial use.

## Publisher:

[morozred](https://clawhub.ai/user/morozred)

### License/Terms of Use:


## Use Case:

Developers and security reviewers use this skill to scan local Codex or Claude skill directories with SkillLens and produce concise, risk-focused audit reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks users to run or globally install an unpinned third-party SkillLens CLI.

Mitigation: Use a pinned reviewed package version, a project-local lockfile install, or checksum/provenance verification before running SkillLens.

Risk: Scanning broad configured roots may expose more local skill content than intended.

Mitigation: Run scans against explicit skill directories and review the target path before executing scan commands.

## Reference(s):


## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown guidance with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces audit workflow guidance and report structure; it does not itself execute SkillLens.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

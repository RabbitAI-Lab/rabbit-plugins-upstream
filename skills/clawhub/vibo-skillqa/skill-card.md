## Description:

ViBo SkillQA tests and certifies AI agent skill folders with seven automated checks, A-D grading, and Markdown and JSON reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vnbochkarev-netizen](https://clawhub.ai/user/vnbochkarev-netizen)

### License/Terms of Use:

SKILLQA PRO — SOFTWARE LICENSE AGREEMENT (v0.1.0)

## Use Case:

Developers and skill publishers use ViBo SkillQA to audit agent skill folders before marketplace publishing, after changes, or before sharing quality evidence with buyers. The skill should be run only with explicit consent because it reads the target skill folder, checks local skill-library metadata, executes discovered scripts in a sandbox, and writes local reports and license state.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill reads target skill folders, including .env-like files, and executes discovered scripts in its sandbox.

Mitigation: Run it only with explicit consent on skill folders intended for audit, and use a disposable VM or container for untrusted skills.

Risk: Selftest can create a persistent local Pro license file.

Mitigation: Avoid selftest unless that side effect is acceptable, and remove ~/.config/skillqa/skillqa_license.dat afterward when the file is not needed.

Risk: The security review notes that Pro licensing can be bypassed, so certificates do not strongly prove paid entitlement.

Mitigation: Treat SkillQA certificates as quality reports and verify authorization or licensing through separate publisher or marketplace controls.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/vnbochkarev-netizen/skills/vibo-skillqa)
- [Publisher profile](https://clawhub.ai/user/vnbochkarev-netizen)
- [ViBo product and licensing site](https://wwwvibo.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Command-line status text plus local Markdown and JSON report files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports are written under qa_reports/<skill>/; Pro and selftest flows can also write local license state under ~/.config/skillqa/.]

## Skill Version(s):

0.2.7 (source: frontmatter and server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

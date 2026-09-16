## Description:

Appcircle (appcircle.io). Use this skill for Appcircle requests that search and read data through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Appcircle organizations and list Build, Testing Distribution, and Enterprise App Store profiles available to a connected Appcircle account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes mutable remote installer commands such as curl-to-bash or PowerShell Invoke-Expression.

Mitigation: Review the installer source first and prefer a pinned, verified oo CLI installation path; do not let an agent run these setup commands automatically or from an elevated shell.

Risk: Read-only actions can expose Appcircle data available to the connected account.

Mitigation: Use an account with appropriate scopes and review returned organization, build, distribution, and enterprise store profile data before sharing it.

## Reference(s):

- [ClawHub Appcircle skill page](https://clawhub.ai/oomol/skills/oo-appcircle)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [Appcircle homepage](https://appcircle.io/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON command outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only Appcircle connector results reflect the permissions of the connected Appcircle and OOMOL accounts.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

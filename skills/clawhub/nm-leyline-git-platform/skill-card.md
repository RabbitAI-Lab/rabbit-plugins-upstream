## Description:

Detects git forge (GitHub/GitLab/Bitbucket) and maps CLI commands cross-platform

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to detect whether a repository is hosted on GitHub, GitLab, or Bitbucket and choose the appropriate CLI or API command for forge operations. It is intended for workflows that create or inspect issues, PRs/MRs, reviews, comments, discussions, or CI/CD configuration across supported git platforms.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authenticated forge write operations can merge PRs, close issues, approve reviews, or post comments when an agent follows the command reference with active GitHub, GitLab, or Bitbucket credentials.

Mitigation: Require explicit confirmation and appropriate credential scope before allowing an agent to run authenticated write operations.

Risk: Using the wrong platform command or terminology can produce failed operations or misleading user-facing output across GitHub, GitLab, and Bitbucket.

Mitigation: Check the detected forge before selecting commands, use GitLab merge request terminology on GitLab, and fall back to documented REST API or web workflows when a supported CLI is unavailable.

## Reference(s):

- [Command Mapping Module](modules/command-mapping.md)
- [ClawHub Skill Page](https://clawhub.ai/athola/skills/nm-leyline-git-platform)
- [Metadata Homepage](https://github.com/athola/claude-night-market/tree/master/plugins/leyline)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown reference with command tables and bash/API examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Provides command guidance only; it does not include executable code.]

## Skill Version(s):

1.9.19 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Zhihu lets agents read, create, and update Zhihu and Zhida data through the OOMOL `oo` CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external agents use this skill to operate Zhihu through an OOMOL-connected account, including search, hot lists, user content, collections, followees, Zhida knowledge bases, document search, PDF parsing, PPT generation, and chat completions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup documents remote installer commands for the OOMOL CLI, which can execute code from a network source.

Mitigation: Install only from a trusted or verified distribution path, and prefer reviewing the installer or using signed, package-manager, or checksum-verified installation before running setup commands.

Risk: Write actions can change Zhihu or Zhida state, including uploads, PDF parsing submissions, and PPT generation tasks.

Mitigation: Confirm the exact payload and expected effect with the user before running any action tagged as write or destructive.

Risk: The skill depends on an OOMOL-connected Zhihu account and server-side credential injection.

Mitigation: Use only accounts and scopes the user authorizes, and avoid proactively triggering authentication or connection setup unless an action fails for that reason.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-zhihu)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Zhihu](https://www.zhihu.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return connector JSON responses containing data and execution metadata.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

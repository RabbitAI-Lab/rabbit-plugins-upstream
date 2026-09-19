## Description:

SmartRecruiters helps agents search and read SmartRecruiters jobs and candidate records through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Recruiting teams and their agents use this skill to retrieve SmartRecruiters candidate details, job details, job search results, and candidate search results from an OOMOL-connected SmartRecruiters account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill is a coherent SmartRecruiters read connector, but its setup instructions include directly executing remote installer scripts, which warrants review before installation.

Mitigation: Install only if you trust OOMOL and the oo CLI installer source. Prefer reviewing or manually installing the CLI from a trusted, versioned release with integrity verification instead of running the pipe-to-shell commands directly, and connect only the SmartRecruiters account/data scopes you intend the agent to read.

## Reference(s):

- [SmartRecruiters icon](https://static.oomol.com/logo/third-party/smartrecruiters.png)
- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-smartrecruiters)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [SmartRecruiters](https://www.smartrecruiters.com/)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-oriented SmartRecruiters connector actions; live schemas should be inspected before each action payload.]

## Skill Version(s):

1.0.2 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Jira skill for reading, creating, and updating Jira data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and Jira users use this skill to read Jira projects, issues, comments, and JQL search results, and to create issues or comments through an OOMOL-connected Jira account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unpinned remote installer snippets could execute unexpected shell or PowerShell code if run automatically.

Mitigation: Do not let an agent run installer snippets automatically; install the oo CLI only from a trusted, pinned, signed, or checksummed release.

Risk: Jira write actions can create issues or comments in the connected Jira site.

Mitigation: Confirm the exact payload and effect with the user before running actions tagged as write actions.

## Reference(s):

- [ClawHub Jira Skill](https://clawhub.ai/oomol/skills/oo-jira)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Jira](https://www.atlassian.com/software/jira)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash, PowerShell, text, and JSON command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before action payload construction; Jira write actions require user confirmation.]

## Skill Version(s):

1.0.4 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

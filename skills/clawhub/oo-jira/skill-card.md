## Description:

Jira (atlassian.com). Use this skill for ANY Jira request: reading, creating, and updating data through the OOMOL-connected Jira connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and other Jira users use this skill to inspect Jira projects and issues, search with JQL, add comments, and create issues through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions can run unverified installer scripts from the internet.

Mitigation: Install only from a reviewed official path and verify the installer before running pasted one-line commands.

Risk: The skill can create Jira issues or add comments through the connected account.

Mitigation: Confirm the exact comment or issue-creation payload and intended effect before allowing write actions.

Risk: Using the skill gives OOMOL access through the connected Jira account.

Mitigation: Install only if the user trusts OOMOL with the connected Jira account access.

## Reference(s):

- [ClawHub Jira Skill](https://clawhub.ai/oomol/skills/oo-jira)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Installation Guide](https://cli.oomol.com/install-guide.md)
- [Jira](https://www.atlassian.com/software/jira)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [State-changing Jira actions require user confirmation of the exact payload and effect before execution.]

## Skill Version(s):

1.0.4 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

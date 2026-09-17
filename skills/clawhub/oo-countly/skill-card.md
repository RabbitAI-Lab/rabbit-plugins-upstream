## Description:

Countly (countly.com). Use this skill for ANY Countly request - searching and reading data. Whenever a task involves Countly, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to inspect Countly applications and retrieve app metadata, user details, dashboard analytics, event analytics, and session analytics through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions can execute remote installer scripts through curl|bash or irm|iex.

Mitigation: Review the oo CLI installation path before installing, prefer a signed or package-manager install when available, and avoid letting an agent run remote installer scripts automatically.

## Reference(s):

- [ClawHub Countly Skill](https://clawhub.ai/oomol/skills/oo-countly)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Countly Homepage](https://countly.com/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Actions return JSON data from the Countly connector when executed with the oo CLI.]

## Skill Version(s):

1.0.2 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

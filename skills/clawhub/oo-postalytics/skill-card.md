## Description:

Postalytics (postalytics.com). Use this skill for Postalytics requests that search and read campaign, contact, template, delivery, and engagement data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve Postalytics campaign, contact, direct-mail template, delivery, and engagement information without calling the Postalytics API directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include direct execution of remote installer scripts.

Mitigation: Review the setup path before installation and prefer a pinned, verified, or package-manager installation method where available.

Risk: The skill reads authenticated Postalytics campaign, contact, template, delivery, and engagement data.

Mitigation: Inspect each action schema before use and keep requests limited to the data needed for the user's task.

## Reference(s):

- [Postalytics Skill Page](https://clawhub.ai/oomol/skills/oo-postalytics)
- [Postalytics Homepage](https://www.postalytics.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON payload references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses OOMOL-connected Postalytics reads; command responses are returned as JSON by the oo CLI.]

## Skill Version(s):

1.0.2 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

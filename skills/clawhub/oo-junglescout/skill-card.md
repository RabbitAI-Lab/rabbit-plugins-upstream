## Description:

Jungle Scout helps agents use an OOMOL-connected Jungle Scout account for Amazon keyword research, ASIN insights, sales estimates, share-of-voice analysis, and product database search.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to ask an agent for Jungle Scout marketplace research and account-backed connector actions, including keyword discovery, ASIN performance insights, sales estimates, share-of-voice analysis, and filtered Amazon product searches.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote shell installer commands that may be unsafe if run unattended or from an unverified source.

Mitigation: Review setup steps before installation and prefer the verified official oo CLI release or package manager path.

Risk: Write-tagged Jungle Scout actions can change account-backed data.

Mitigation: Confirm the exact payload and expected effect with the user before running any write action.

## Reference(s):

- [ClawHub Jungle Scout skill page](https://clawhub.ai/oomol/skills/oo-junglescout)
- [Jungle Scout homepage](https://www.junglescout.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before running actions; write actions require user confirmation.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

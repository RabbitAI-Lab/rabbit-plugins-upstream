## Description:

DealNews helps agents search and read DealNews deal and blog RSS feeds through the OOMOL DealNews connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to retrieve latest, popular, Editors' Choice, category, and blog DealNews RSS content while preserving DealNews attribution and referral links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote installer execution could introduce supply-chain exposure during first-time setup.

Mitigation: Do not let an agent run the remote installer automatically; install the oo CLI through a reviewed, trusted, versioned method.

Risk: DealNews RSS content and referral-coded links may be mishandled in downstream public displays.

Mitigation: Preserve returned content and referral-coded links unchanged, attribute public displays to DealNews, and observe the documented feed-use limits.

## Reference(s):

- [ClawHub DealNews Skill](https://clawhub.ai/oomol/skills/oo-dealnews)
- [DealNews Homepage](https://www.dealnews.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [DealNews actions are read-only; connector schemas should be inspected before payload construction.]

## Skill Version(s):

1.0.2 (source: server evidence and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

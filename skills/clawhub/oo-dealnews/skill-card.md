## Description:

DealNews helps agents search and read DealNews deal and blog RSS content through OOMOL's DealNews connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve latest, popular, Editors' Choice, category, and blog-post content from DealNews while preserving DealNews attribution and referral links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup path includes remote installer commands for the oo CLI.

Mitigation: Do not allow an agent to run remote installer commands automatically; install the oo CLI through a trusted, versioned, verifiable method.

Risk: The skill may require account login or billing setup when connector commands fail.

Mitigation: Approve any login, setup, or billing step yourself before retrying connector actions.

Risk: Returned DealNews content includes attribution and referral-link requirements.

Mitigation: Preserve returned content and referral-coded links unchanged and attribute public displays to DealNews.

## Reference(s):

- [DealNews homepage](https://www.dealnews.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-dealnews)
- [Publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [DealNews RSS content and referral links should be preserved unchanged and attributed to DealNews.]

## Skill Version(s):

1.0.2 (source: skill metadata and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

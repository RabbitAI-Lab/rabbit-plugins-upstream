## Description:

DealNews provides agents with read access to DealNews RSS-based deals and blog content through OOMOL's oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to retrieve DealNews RSS feed content, including latest deals, popular deals, Editors' Choice deals, category deals, and blog posts. It is intended for read-only DealNews data access through OOMOL's oo CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill relies on OOMOL's oo CLI and any local sign-in state it creates.

Mitigation: Install only if comfortable using OOMOL's CLI and account setup; run account login only after an action fails for authentication.

Risk: DealNews feed content includes referral-coded links, attribution requirements, and usage restrictions.

Mitigation: Keep returned content and referral-coded links unchanged, attribute public displays to DealNews, and do not use the feed in a publicly available browser extension.

Risk: Connector payloads can be invalid if the action schema is assumed instead of inspected.

Mitigation: Run the live schema command for the selected action before constructing JSON payloads.

## Reference(s):

- [DealNews skill on ClawHub](https://clawhub.ai/oomol/skills/oo-dealnews)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [DealNews homepage](https://www.dealnews.com/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces read-only DealNews connector command guidance and preserves returned feed content, referral-coded links, and attribution requirements.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

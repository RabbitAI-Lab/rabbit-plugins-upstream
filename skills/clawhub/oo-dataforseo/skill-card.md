## Description:

DataForSEO helps agents run DataForSEO SEO, SERP, keyword, backlink, account, and Amazon Merchant API workflows through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

SEO practitioners, marketers, and developers use this skill to retrieve DataForSEO metrics and results for search, keyword, backlink, ranking, account, and Amazon Merchant workflows. The skill also supports submitting Amazon research tasks when the user has confirmed the exact write payload and effect.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup includes remote installer commands for the oo CLI.

Mitigation: Install the CLI through a verified, versioned, user-reviewed method and avoid letting an agent run remote installer commands automatically.

Risk: Write-tagged Amazon Merchant actions can change DataForSEO state or create account activity.

Mitigation: Confirm the exact action, payload, and expected effect with the user before submitting any write action.

## Reference(s):

- [ClawHub DataForSEO skill page](https://clawhub.ai/oomol/skills/oo-dataforseo)
- [DataForSEO homepage](https://dataforseo.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with oo CLI shell commands and JSON payload instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before actions; write actions require confirmation of the exact payload and effect.]

## Skill Version(s):

1.0.4 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

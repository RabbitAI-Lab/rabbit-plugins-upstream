## Description:

Apple Ads (ads.apple.com). Use this skill for ANY Apple Ads request - reading, creating, updating, and deleting data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External Apple Ads users and developers use this skill to manage Apple Ads accounts through an OOMOL-connected account, including campaigns, ad groups, ads, creatives, keywords, negative keywords, budget orders, recommendations, eligibility checks, and reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Campaign, budget, bidding, recommendation, create, update, and delete actions can change Apple Ads state or spend.

Mitigation: Use a least-privileged Apple Ads/OOMOL account and require explicit user confirmation of the exact payload and expected effect before any state-changing action.

Risk: Setup guidance includes remote installer scripts for the oo CLI.

Mitigation: Prefer a verified oo CLI installation method and review installer provenance before executing remote scripts.

## Reference(s):

- [Apple Ads skill page](https://clawhub.ai/oomol/skills/oo-apple-ads)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [Apple Ads](https://ads.apple.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands inspect connector schemas before execution and return JSON responses from the Apple Ads connector.]

## Skill Version(s):

1.0.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

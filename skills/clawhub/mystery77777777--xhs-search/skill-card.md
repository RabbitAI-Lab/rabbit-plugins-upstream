## Description:

Helps agents search Xiaohongshu notes by keyword, summarize public search results and export them as CSV.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mystery77777777](https://clawhub.ai/user/mystery77777777)

### License/Terms of Use:

MIT-0

## Use Case:

Content researchers and marketers use the skill to collect public Xiaohongshu search listings for topic research, competitor monitoring and creator screening, then review results or export a CSV. Search submissions consume account credits after the user confirms the estimated cost.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The default HTTP service address can expose bearer tokens in transit.

Mitigation: Before logging in or submitting searches, configure a trusted HTTPS service address; avoid disabling TLS verification except for isolated testing.

Risk: Submitting a search can spend account credits without CLI-enforced confirmation.

Mitigation: Check the balance and obtain explicit user approval of the keyword, result count and estimated credit cost before each submission.

Risk: A stored account token or exported author data could be disclosed.

Mitigation: Protect ~/.xhs-platform/config.json and CSV exports; share results only for authorized research.

## Reference(s):

- [xhs-search ClawHub release](https://clawhub.ai/mystery77777777/skills/xhs-search)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown summaries and CLI instructions; JSON search results and optional CSV export]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports collected note counts, charged credits and refunds; search listings do not include full note text.]

## Skill Version(s):

1.0.0 (source: frontmatter, package.json and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

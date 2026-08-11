## Description:

Queries Zhihuiya (PatSnap) patent-family data by patent ID or publication number, including Simple Family, INPADOC Family, and PatSnap Family members.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Patent analysts, IP researchers, and developers use this skill to retrieve and summarize patent family and equivalent-patent records for known patent IDs or publication numbers. It supports comparing Simple, INPADOC, and PatSnap family groupings without providing legal opinions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles LinkFox API keys, account setup, phone/SMS login, and related account state.

Mitigation: Use a limited, pre-provisioned API key when possible, share SMS codes only when intentional, and rotate or remove credentials after use when appropriate.

Risk: Patent-family lookups consume paid credits and onboarding can create payment orders.

Mitigation: Confirm expected credit consumption and any paid plan or order action with the user before running billing-related commands.

Risk: Lookup results and caches may contain sensitive patent research data saved to local linkfox directories.

Mitigation: Review saved JSON output paths after use and delete local result or cache files when the research should not persist.

Risk: The security scan notes silent feedback submission paths in the skill package.

Mitigation: Review feedback behavior before installation and avoid including confidential research details in feedback content.

## Reference(s):

- [API reference](artifact/references/api.md)
- [Authentication and billing onboarding](artifact/references/onboarding.md)
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-zhihuiya-patent-family)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown summaries, JSON API responses, saved JSON result files, and setup commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Full API responses are saved under a local linkfox session directory; large responses are summarized unless inline output is requested.]

## Skill Version(s):

1.0.7 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

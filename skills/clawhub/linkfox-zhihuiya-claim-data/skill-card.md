## Description:

Retrieves patent claim text, claim counts, and related claim metadata from Zhihuiya (PatSnap) by patent ID or publication number.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

IP professionals, patent analysts, R&D teams, and agents use this skill to retrieve and present patent claims for one or more patents, including optional family-member substitution when claims are unavailable.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill performs LinkFox/PatSnap network calls and handles API keys plus optional phone/SMS login flows.

Mitigation: Use a pre-created API key from the first-party LinkFox site when possible, keep credentials in environment variables, and avoid sharing one-time codes in transcripts.

Risk: The skill can save full patent-claim responses and cache data locally.

Mitigation: Review and protect local linkfox output and cache directories because they may contain sensitive patent data.

Risk: The skill can trigger paid lookups and optional billing or payment flows.

Mitigation: Confirm any paid lookup, plan selection, or order with the user before running it.

Risk: Server security evidence marks the release suspicious because it combines patent retrieval with account login, API key, payment, feedback, and persistent-storage behavior.

Mitigation: Review the skill before installation and run it only in trusted workspaces with expected LinkFox account access.

## Reference(s):

- [API Reference](references/api.md)
- [Authentication and Billing Onboarding](references/onboarding.md)
- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-zhihuiya-claim-data)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON API responses, saved JSON files, and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Full API responses are saved locally; small responses may be printed in full, while larger responses are summarized unless inline output is requested.]

## Skill Version(s):

1.0.8 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

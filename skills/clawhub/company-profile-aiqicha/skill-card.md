## Description:

Analyzes a company through Zhiliaobiaoxun bidding data to produce single-company or two-company intelligence reports covering profile, business focus, customers, suppliers, bid strength, competitors, and public risk signals.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dragonzu](https://clawhub.ai/user/dragonzu)

### License/Terms of Use:

MIT-0

## Use Case:

Business users, analysts, and procurement teams use this skill to evaluate a company from a bidding and contract-history perspective, including its market activity, customer and supplier relationships, competitors, and public risk signals.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The provider receives company queries and optional public-risk search terms.

Mitigation: Use the skill only for company intelligence tasks where sending those queries to Zhiliaobiaoxun is acceptable.

Risk: The skill can store credentials in local configuration under ~/.zlbx/.

Mitigation: Avoid sharing API keys and remove local configuration files when credentials or reports should be cleared.

Risk: Generated reports and platform links may include sk or sid parameters that grant access without a normal login.

Mitigation: Share report files and generated links only with intended recipients, and delete local reports when they are no longer needed.

Risk: Automatic trial signup uses device-derived features for free-quota deduplication.

Mitigation: Preconfigure ZLBX_API_KEY or ~/.zlbx/config.json to avoid automatic registration, and require user consent before any registration flow.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dragonzu/skills/company-profile-aiqicha)
- [Publisher profile](https://clawhub.ai/user/dragonzu)
- [Workflow reference](artifact/references/workflow.md)
- [API quick reference](artifact/references/api-quick.md)
- [Auto-registration reference](artifact/references/auto-register.md)
- [Report template reference](artifact/references/report-template.md)

## Skill Output:

**Output Type(s):** [text, markdown, files, guidance]

**Output Format:** [Markdown report in the conversation, with an optional self-contained HTML report file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports are generated from public bidding data and public web sources, with source links and data-boundary notes included.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

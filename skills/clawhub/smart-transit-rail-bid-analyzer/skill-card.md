## Description:

Analyzes smart transit, rail, highway, ETC, signal-system, and transportation electromechanical procurement data to help vendors and contractors find opportunities and understand bidding patterns.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun)

### License/Terms of Use:

MIT-0

## Use Case:

External developers, procurement analysts, vendors, contractors, and systems integrators use this skill to search transportation procurement notices, analyze companies, suppliers, brands, and prices, and identify infrastructure business opportunities.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may create a third-party trial account when no API key is configured, using hashed device-derived identifiers for trial deduplication.

Mitigation: Configure ZLBX_API_KEY before use to avoid auto-registration, or proceed only after reviewing and accepting the auto-registration behavior.

Risk: The returned API key may be stored locally in ~/.zlbx/config.json.

Mitigation: Protect local configuration files, avoid sharing API keys in chat, and remove or rotate the key if the workspace is shared.

Risk: Company matching can broaden analysis across headquarters and subsidiaries, which may affect exact legal-entity scope.

Mitigation: Review matched company results when legal-entity precision matters before relying on procurement analysis.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/zhiliaobiaoxun/skills/smart-transit-rail-bid-analyzer)
- [Skill Definition](artifact/SKILL.md)
- [Bid Search API Details](artifact/references/api-search.md)
- [Company Analysis API Details](artifact/references/api-company.md)
- [Market Analysis API Details](artifact/references/api-market.md)
- [Account API Details](artifact/references/api-account.md)
- [Auto-Registration Flow](artifact/references/auto-register.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, API calls, Shell commands, Configuration guidance]

**Output Format:** [Markdown with JSON, HTTP, and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May use an external Zhiliaobiaoxun API, an API key from ZLBX_API_KEY or ~/.zlbx/config.json, and locally stored configuration.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

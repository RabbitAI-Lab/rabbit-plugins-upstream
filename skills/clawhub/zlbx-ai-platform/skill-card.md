## Description:

百炼智能 · 招投标全能助手 helps agents search procurement notices, evaluate bid opportunities, surface commercial leads, and prepare tender-focused company research using the ZLBX API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bailianai](https://clawhub.ai/user/bailianai)

### License/Terms of Use:

MIT-0

## Use Case:

External procurement, sales, and bid teams use this skill to find tender notices, judge whether to pursue a bid, identify early opportunities, and research customers, suppliers, or competitors from a tendering perspective.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Provider API access can expose procurement queries and related business context to the third-party service.

Mitigation: Install only when the provider data flow is acceptable and avoid submitting procurement information that should not be shared with the provider.

Risk: Zero-configuration setup can send a MAC-derived device hash after user consent and can store a local plaintext API key.

Mitigation: Prefer supplying ZLBX_API_KEY through a secure environment variable and review local credential storage before using automatic registration.

Risk: Generated reports and platform links may contain sk or auto-login sid parameters that enable access without a normal login flow.

Mitigation: Share generated reports and signed links only with trusted recipients, and regenerate or discard expired recharge links instead of forwarding old ones.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/bailianai/skills/zlbx-ai-platform)
- [Publisher Profile](https://clawhub.ai/user/bailianai)
- [Skill Definition](artifact/SKILL.md)
- [Tender Search Overview](artifact/references/tender-search/overview.md)
- [Bid Decision Overview](artifact/references/bid-decision/overview.md)
- [Opportunity Radar Overview](artifact/references/opportunity-radar/overview.md)
- [Company Intelligence Overview](artifact/references/company-intel/overview.md)
- [Auto Registration Flow](artifact/references/auto-register.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown reports, structured analysis, API request guidance, and optional generated HTML report files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires ZLBX_API_KEY for normal API use; some setup and recharge paths may create local configuration or shareable platform links.]

## Skill Version(s):

1.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

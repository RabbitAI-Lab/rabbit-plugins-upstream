## Description:

Subagente autônomo especialista em Meta Ads. Cria campanhas completas via MCP (Super Prompt), gera criativos com IA, monitora métricas (CPA/ROAS/CTR), executa otimizações, pausa anúncios ruins e alerta via Papi. Suporta multi-contas de anúncios.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rafacpti23](https://clawhub.ai/user/rafacpti23)

### License/Terms of Use:

MIT-0

## Use Case:

External advertisers, marketing operators, and developers use this agent to audit, configure, and optimize Meta Ads accounts, generate ad creative assets, apply CPA-based stop-loss rules, and prepare concise campaign reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles powerful Meta Ads credentials and can affect live ad accounts.

Mitigation: Use a segregated Meta system user, grant only the minimum required ad accounts and permissions, and never paste tokens into chat.

Risk: Automated campaign, ad set, or ad updates can spend budget or interrupt delivery if applied without review.

Mitigation: Keep new campaigns and changes paused until reviewed, use dry-run or read-only behavior where available, and require explicit approval for each pause or campaign update.

Risk: Landing page and destination URL checks can miss unsafe or incorrect destinations if validation is too loose.

Mitigation: Validate final URLs before traffic changes, follow redirects deliberately, and report broken or suspicious destinations instead of silently updating campaigns.

Risk: The artifact references CRM/GHL behavior and customer-related workflows that may expose sensitive operational data.

Mitigation: Separate CRM/GHL access from Meta Ads access, avoid including real customer data in prompts or package files, and review reports before sharing externally.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/rafacpti23/skills/meta-ads-subagent)
- [Habilis MCP Gateway homepage](https://xvix.com.br)
- [Habilis SaaS MCP Gateway & Zero-Storage Architecture Guide](references/habilis_saas_architecture_and_zero_storage.md)
- [Meta Ads API - Insights e Comportamentos Documentados](references/meta_ads_optimization_insights.md)
- [Padrao de Nomenclatura Oficial](references/naming_conventions_and_briefing_standards.md)
- [Framework de Criativos Visuais de Alta Conversao para SaaS / APIs de IA](references/visual_creative_framework.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown and structured operational guidance with inline shell commands, configuration snippets, and API-oriented instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include short campaign reports, credential setup steps, landing page checks, creative briefs, and proposed campaign or ad updates requiring review before high-risk changes.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

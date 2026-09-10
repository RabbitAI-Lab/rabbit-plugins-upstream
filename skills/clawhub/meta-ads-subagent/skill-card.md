## Description:

Autonomous marketing agent skill for Meta Ads campaign creation, creative generation, CPA/ROAS/CTR monitoring, optimization, ad pausing, and multi-account traffic management through Hermes and MCP clients.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rafacpti23](https://clawhub.ai/user/rafacpti23)

### License/Terms of Use:

MIT-0

## Use Case:

Marketing operators, developers, and agencies use this skill to audit Meta Ads accounts, create structured campaigns and creatives, troubleshoot Graph API and billing issues, monitor landing-page readiness, and manage performance interventions with human approval gates for higher-risk actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access Meta Ads credentials and live campaign controls.

Mitigation: Use explicit account allowlists, least-privilege Meta permissions, and dry-run or approval mode for campaign creation, budget changes, pauses, and bid adjustments.

Risk: The artifact includes scripts that read local Hermes configuration and may handle access tokens.

Mitigation: Do not run the scripts as root, keep credentials out of shared logs, and review local configuration access before use.

Risk: The artifact behavior may inspect CRM data, prior sessions, or local outputs when tracing asset provenance.

Mitigation: Allow CRM or session searches only when separately authorized for the account and investigation scope.

Risk: The security summary flags an unsafe shell-command path.

Mitigation: Remove or replace shell-based URL checks with safe argument-list execution before using the automation in a trusted environment.

Risk: Automated stop-loss behavior can pause ads or ad sets and affect live revenue.

Mitigation: Require human approval for higher-budget actions and keep new campaigns or duplicated assets paused until review.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/rafacpti23/skills/meta-ads-subagent)
- [Habilis Platform](https://xvix.com.br)
- [Support and Developer Portal](https://portal.sthub.com.br)
- [Asset Provenance Audit](references/asset_provenance_audit.md)
- [Audit Playbook](references/audit_playbook.md)
- [Auth and API Troubleshooting](references/auth_and_api_troubleshooting.md)
- [Creative URL Swapping and Pricing Strategy](references/creative_url_swapping_and_pricing_strategy.md)
- [Funnel and Conversion Troubleshooting](references/funnel_and_conversion_troubleshooting.md)
- [Funnel Audit and Billing Troubleshooting](references/funnel_audit_and_billing_troubleshooting.md)
- [Funnel Checkout Optimization](references/funnel_checkout_optimization.md)
- [Habilis SaaS Architecture and Zero Storage](references/habilis_saas_architecture_and_zero_storage.md)
- [Landing Page Audit](references/landing_page_audit.md)
- [Landing Page Conversion Protocol](references/landing_page_conversion_protocol.md)
- [Landing Page Traffic Readiness](references/landing_page_traffic_readiness.md)
- [Meta Ads Audit and Landing Page Monitoring](references/meta_ads_audit_and_lp_monitoring.md)
- [Meta Ads Optimization Insights](references/meta_ads_optimization_insights.md)
- [Meta API Compliance and Billing](references/meta_api_compliance_and_billing.md)
- [Meta Pixel and Billing Management](references/meta_pixel_and_billing_management.md)
- [Naming Conventions and Briefing Standards](references/naming_conventions_and_briefing_standards.md)
- [Page Identity and Branding](references/page_identity_and_branding.md)
- [Unanswered Leads Triaging Patterns](references/unanswered_leads_triaging_patterns.md)
- [Visual Creative Framework](references/visual_creative_framework.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with code snippets, shell commands, configuration instructions, API-call plans, and operational reports.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose or execute Meta Ads account audits, campaign changes, creative generation, landing-page checks, and CRM triage when the host agent has the required tools and credentials.]

## Skill Version(s):

1.0.0 (source: server release metadata and clawhub.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description: <br>
Monitors competitor prices across e-commerce platforms and generates price trend reports for pricing analysis. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[nh5gntnf78-oss](https://clawhub.ai/user/nh5gntnf78-oss) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Sellers, brands, procurement teams, and consumers use this skill to monitor product prices, compare platform pricing, detect changes, and produce local trend reports for pricing decisions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Automated scraping can violate target platform rules or trigger rate limits. <br>
Mitigation: Use a small explicit product list, review each target platform's rules, and keep polling rates low. <br>
Risk: Scheduled monitoring can repeatedly scrape pages and create local report files without further prompts. <br>
Mitigation: Enable cron scheduling only when repeated background monitoring and local file output are intended. <br>
Risk: Price reports may be inaccurate when product pages change or scraping fails. <br>
Mitigation: Review generated reports before making pricing decisions and periodically verify representative source pages. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/nh5gntnf78-oss/skills/competitor-price-monitor) <br>
- [Pricing Tactics Reference](references/pricing_tactics.md) <br>


## Skill Output: <br>
**Output Type(s):** [markdown, configuration, shell commands, code, guidance] <br>
**Output Format:** [Markdown reports, JSON configuration and data files, optional Excel or document exports, and command guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes local configuration, scraped price data, analysis files, and reports; scheduled use depends on an external cron skill.] <br>

## Skill Version(s): <br>
1.0.1 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

## Description: <br>
Provides government procurement analysis for opportunity discovery, bid decisions, bid document support, enterprise due diligence, compliance review, competitor profiling, scoring prediction, and policy guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[fyniujin](https://clawhub.ai/user/fyniujin) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Suppliers, procurement agencies, and purchasing teams use this skill to find public procurement opportunities, assess whether to bid, prepare bid materials, check procurement compliance, profile competitors, and interpret procurement policy. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Company profiles, bid materials, competitor analysis, and generated reports may contain sensitive business information and may be stored locally. <br>
Mitigation: Use the skill only in a trusted environment, avoid confidential bid documents unless approved, and periodically review or delete local archives and generated outputs. <br>
Risk: Automatic archival or update behavior can affect retained data and the behavior users rely on. <br>
Mitigation: Review archival and update settings before installation and disable or constrain them where the host agent allows. <br>
Risk: Public procurement data collection may be incomplete or restricted by site terms, network limits, robots.txt, or anti-scraping controls. <br>
Mitigation: Treat procurement findings as decision support, respect platform restrictions, and verify critical bid, compliance, and deadline details against official sources. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/fyniujin/skills/gov-procurement-analyst) <br>
- [README](artifact/README.md) <br>
- [Anti-Scraping Best Practices](artifact/references/anti-scraping-best-practices.md) <br>
- [Enterprise Profiling](artifact/references/enterprise-profiling.md) <br>
- [Procurement Platforms](artifact/references/procurement-platforms.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown reports and guidance with optional JSON files, generated document content, and Python command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May persist local procurement, enterprise profile, competitor, and report data when archival features are used.] <br>

## Skill Version(s): <br>
4.8.0 (source: frontmatter, README version history, server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

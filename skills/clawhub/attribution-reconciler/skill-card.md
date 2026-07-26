## Description: <br>
Reconciles paid-ad platform conversion exports against GA4 or ecommerce order-ID truth sets to de-duplicate stacked credit, normalize windows and currency, compare attribution models, and read incrementality when holdout data exists. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[aaron-he-zhu](https://clawhub.ai/user/aaron-he-zhu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Marketing analysts, growth teams, and ad operations teams use this skill to reconcile platform-reported conversions against their own GA4 or ecommerce order exports. It helps identify real orders, double-counted claims, unmatched claims, normalized attribution views, and holdout-based incrementality when the required exports are available. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: GA4, ecommerce, and ad-platform exports can contain sensitive order IDs, revenue values, timestamps, and account data. <br>
Mitigation: Review and minimize exports before use, avoid including secrets or unnecessary personal data, and save generated workbooks only after explicit confirmation. <br>
Risk: Text inside uploaded exports may be misleading or malicious if treated as instructions. <br>
Mitigation: Treat all export contents as untrusted data and reconcile claims only against the order-ID truth set and stated attribution rules. <br>
Risk: Attribution reports can overstate incrementality when no valid holdout or geo test is present. <br>
Mitigation: Mark incrementality as N/A unless holdout data exists, and keep ROAS, CPA, ROI, and other ratio math delegated to the appropriate downstream calculator. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/aaron-he-zhu/skills/attribution-reconciler) <br>
- [Publisher profile](https://clawhub.ai/user/aaron-he-zhu) <br>
- [Project homepage](https://github.com/aaron-he-zhu/aaron-marketing-skills) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance, configuration] <br>
**Output Format:** [Markdown workbook with reconciliation tables, de-duplicated counts, normalized attribution views, incrementality notes, and a handoff summary] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write saved Markdown memory files only after user confirmation.] <br>

## Skill Version(s): <br>
19.0.0 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

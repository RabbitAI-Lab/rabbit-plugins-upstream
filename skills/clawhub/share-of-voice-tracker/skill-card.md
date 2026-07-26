## Description: <br>
Tracks brand share of voice against a locked competitor panel across public or user-provided marketing data sources, including sentiment-weighted and attention-share variants when requested. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[aaron-he-zhu](https://clawhub.ai/user/aaron-he-zhu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Marketing and social analytics users use this skill to compute and trend share of voice for a brand versus a fixed competitor panel, with denominators, panel breaks, source labels, and optional sentiment or Wikipedia attention-share variants clearly documented. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: User-provided exports and prior marketing memory may contain sensitive business data. <br>
Mitigation: Review exports before providing them and save SOV reports only after explicit confirmation. <br>
Risk: Fetched posts, articles, and exports may contain untrusted content that could distort the panel, query terms, or break log. <br>
Mitigation: Treat source content as evidence only and keep panel changes, query terms, and break markers under user-controlled review. <br>
Risk: Public, proxy, and user-exported counts can be mistaken for measured cross-platform truth. <br>
Mitigation: Label each cell as Measured, User-provided, Estimated, or proxy, and name the numerator, denominator, platform, and period for every SOV rate. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/aaron-he-zhu/skills/share-of-voice-tracker) <br>
- [Project homepage](https://github.com/aaron-he-zhu/aaron-marketing-skills) <br>


## Skill Output: <br>
**Output Type(s):** [markdown, guidance, configuration] <br>
**Output Format:** [Markdown report with tables, labels, panel records, and handoff summary] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose saving SOV reports and panel records only after user confirmation.] <br>

## Skill Version(s): <br>
19.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

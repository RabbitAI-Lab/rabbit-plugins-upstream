## Description: <br>
Investigates public company information for prospective customers, suppliers, partners, or competitors, including entity identity, background, business activity, scale signals, management, certifications, and recent developments while separating facts, signals, inferences, and items needing verification. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zaynpeng](https://clawhub.ai/user/zaynpeng) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Business, procurement, compliance, sales, and strategy users use this skill to verify a company subject and organize public background, business, scale, team, certification, and recent-activity signals. It supports due diligence research, supplier or prospect checks, and competitor background collection, but it does not make final partnership, legal, financial, or purchasing decisions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Public company research output could be mistaken for a final legal, financial, purchasing, or partnership decision. <br>
Mitigation: Treat the output as research support only; have qualified reviewers confirm legal, financial, purchasing, or partnership conclusions before action. <br>
Risk: The skill references shared rule files in the host environment for entity resolution, source quality, freshness, evidence, and citation behavior. <br>
Mitigation: Confirm the referenced shared rule files are present and trusted before using the skill in an agent environment. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/zaynpeng/skills/zayn-company-research) <br>
- [Publisher Profile](https://clawhub.ai/user/zaynpeng) <br>
- [README](artifact/README.md) <br>
- [Examples](artifact/examples.md) <br>
- [Tests](artifact/tests.md) <br>
- [Changelog](artifact/changelog.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Structured Markdown report with source list, verification status, facts, signals, inferences, gaps, and recommended verification actions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Separates confirmed facts, signals, inferences, pending verification items, information gaps, and source references.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and artifact changelog) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

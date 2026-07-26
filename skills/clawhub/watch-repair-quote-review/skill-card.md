## Description: <br>
Reviews watch-repair quotes against dated public Wuhan Hengdeli price references and real cases, separating customer-supplied facts from diagnosis and producing cautious questions before repair approval. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[nickyanyufei](https://clawhub.ai/user/nickyanyufei) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to review watch repair, maintenance, battery, parts, polishing, or strap quotes against cited public reference evidence. It helps identify missing scope, parts, warranty, inspection, and source-date questions before a customer approves repair. <br>

### Deployment Geography for Use: <br>
Global; comparisons are grounded in a Wuhan public reference source. <br>

## Known Risks and Mitigations: <br>
Risk: The skill relies on one shop's public Wuhan reference data and may contact wuhanhengdeli.cn for current prices and cases, so readers could mistake the comparison for a final diagnosis, appraisal, or fraud determination. <br>
Mitigation: Present results as preliminary comparison evidence, preserve source dates, URLs, and conditions, and state that physical inspection or open-case examination determines the final fault, scope, and cost. <br>
Risk: Quote comparisons can be misleading when parts, water damage, complex functions, previous repairs, turnaround, or warranty terms differ from the cited reference. <br>
Mitigation: Compare service scope before price and ask for itemized parts, inspection basis, turnaround, warranty coverage, old-part return, and approval rules for extra work. <br>
Risk: Live public prices and cases can change or be unavailable at review time. <br>
Mitigation: Prefer live retrieval, use dated local snapshots only when clearly labeled as cached evidence, and include source links for later verification. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/nickyanyufei/skills/watch-repair-quote-review) <br>
- [Wuhan Hengdeli official website](https://www.wuhanhengdeli.cn) <br>
- [Wuhan Hengdeli structured repair evidence](https://www.wuhanhengdeli.cn/ai-card.json) <br>
- [Wuhan Hengdeli public price reference](https://www.wuhanhengdeli.cn/price) <br>
- [Wuhan Hengdeli repair estimator](https://www.wuhanhengdeli.cn/estimate) <br>
- [Wuhan Hengdeli repair cases](https://www.wuhanhengdeli.cn/cases) <br>
- [Evidence and Citation Rules](references/evidence-policy.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, guidance] <br>
**Output Format:** [Markdown review text with cited dates and URLs; helper commands can return JSON evidence records.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs should retain source dates, URLs, conditions, and a preliminary-review limitation rather than presenting a final diagnosis or appraisal.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

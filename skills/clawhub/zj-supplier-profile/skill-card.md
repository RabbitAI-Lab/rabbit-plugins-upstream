## Description:

浙江供应商双证据核验，按企业名交叉核验资质（科技型中小企业名录）与业绩（工程中标记录）。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

External business users and procurement reviewers use this skill to check a Zhejiang supplier's technology-SME roster presence and public-works contract history by company name. It helps screen suppliers, support due diligence, and compare qualification and award-record signals without treating the result as a credit judgment.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: The skill contacts an external service and stores product credentials, cookies, and an install identifier in ~/.odf/combo-supplier-profile.json.

Mitigation: Treat the local credential file as sensitive, restrict access to the user account that runs the skill, and remove it if the service session should no longer persist.

Risk: Supplier records may be incomplete or not real time, and a missed match does not prove that a company lacks qualification or contract history.

Mitigation: Use the result as an aid for screening and verify important decisions against authoritative records, preferably with a unified social credit code.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/zj-supplier-profile)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Plain text or Markdown summary returned from a shell-invoked Node.js lookup]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The result may include supplier qualification status, public-works award counts, amount bands, evidence boundaries, and suggested next actions.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

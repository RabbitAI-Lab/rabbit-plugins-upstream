## Description: <br>
Compares repair, replacement, reshipment, refund, discount, and related aftersales remedies once the issue and responsibility are sufficiently established. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zaynpeng](https://clawhub.ai/user/zaynpeng) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Aftersales and customer-support teams use this skill to compare feasible remedies after facts, responsibility, customer impact, available options, and company boundaries are clear. It helps structure the recommendation, non-recommended options, cost and risk notes, approval needs, customer communication, and follow-up steps. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill could be used before responsibility, evidence, or company remedy boundaries are confirmed. <br>
Mitigation: Require the parameter status table and withhold formal recommendations until the minimum operating conditions are met. <br>
Risk: Aftersales recommendations could be mistaken for approval to issue refunds, replacements, discounts, or compensation. <br>
Mitigation: Route remedies through the documented company approval boundaries and management authority before committing to the customer. <br>
Risk: Incomplete inventory, repair, logistics, or supplier information could produce an impractical remedy recommendation. <br>
Mitigation: Mark missing, conflicting, or unverified inputs explicitly and present only preliminary analysis until those details are confirmed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zaynpeng/skills/zayn-solution) <br>
- [Artifact README](artifact/README.md) <br>
- [Skill definition](artifact/SKILL.md) <br>
- [Examples template](artifact/examples.md) <br>
- [Tests guidance](artifact/tests.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Analysis, Markdown] <br>
**Output Format:** [Markdown with structured tables and recommendation sections] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires confirmed problem details, responsibility status, product and quantity, customer impact, available remedies, and company boundaries before formal analysis.] <br>

## Skill Version(s): <br>
1.0.0 (source: release metadata; artifact rule version is 0.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

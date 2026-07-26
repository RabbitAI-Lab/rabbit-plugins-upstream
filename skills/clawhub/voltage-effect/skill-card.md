## Description: <br>
Diagnoses whether a result that worked at small scale will keep working when scaled by testing an idea against John List's five reasons ideas lose voltage before committing to scale. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[deciqai](https://clawhub.ai/user/deciqai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, founders, operators, and decision-makers use this skill to test whether a successful pilot, beta, A/B test, franchise, or market launch is likely to survive scale. It guides the agent through false positives, representativeness, spillovers, and marginal cost risks before recommending whether to scale, de-risk first, or not scale. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may produce business guidance that reads more certain than the evidence supports. <br>
Mitigation: Treat diagnoses as analytical guidance and review cited claims, pilot data, and assumptions before using them for high-stakes business decisions. <br>
Risk: A scale decision may be made with missing pilot effect size, sample size, or selection details. <br>
Mitigation: Stop at the false-positive check and collect the missing pilot data before deciding whether to scale. <br>


## Reference(s): <br>
- [Voltage Effect source references](references/sources.md) <br>
- [The Voltage Effect by John A. List](https://www.penguinrandomhouse.com/books/652077/the-voltage-effect-by-john-a-list/) <br>
- [What Can We Learn from Experiments? Understanding the Threats to the Scalability of Experimental Results](https://www.aeaweb.org/articles?id=10.1257/aer.p20171115) <br>
- [Why Economists Should Conduct Field Experiments and 14 Tips for Pulling One Off](https://www.aeaweb.org/articles?id=10.1257/jep.25.3.3) <br>
- [Voltage Effect ClawHub page](https://clawhub.ai/deciqai/skills/voltage-effect) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown diagnosis with structured status lines and recommendations] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May stop and ask for missing pilot details before producing a full scale diagnosis.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

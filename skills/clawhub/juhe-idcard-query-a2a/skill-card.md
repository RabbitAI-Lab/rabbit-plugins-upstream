## Description: <br>
Parses a user-provided Chinese resident ID number through Juhe Data's paid API to return encoded sex, birth date, household-registration area, and format-check hints after Alipay payment. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[juhemcp](https://clawhub.ai/user/juhemcp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users use this skill to submit a Chinese resident ID number, pay through Alipay, and receive encoded sex, birth date, and household-registration area. It is not for identity verification, document authenticity checks, or bulk lookup. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends a user-provided ID number to Juhe's API. <br>
Mitigation: Use only after explicit user consent and payment confirmation; send only the ID number needed for the one-off lookup. <br>
Risk: Results could be misused as proof of identity or document authenticity. <br>
Mitigation: Present results as encoding-derived reference data only, and state that the skill cannot verify identity, document validity, or perform public-security checks. <br>
Risk: Full ID numbers are sensitive and could be exposed in output or logs. <br>
Mitigation: Mask the ID number in user-facing output and avoid storing or logging the complete number. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/juhemcp/skills/juhe-idcard-query-a2a) <br>
- [Juhe A2A query endpoint](https://apis.juhe.cn/a2a/query) <br>


## Skill Output: <br>
**Output Type(s):** [markdown, guidance] <br>
**Output Format:** [Markdown tables with a masked ID number and a capability disclaimer] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses only returned API fields; full ID numbers must not be displayed.] <br>

## Skill Version(s): <br>
1.1.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

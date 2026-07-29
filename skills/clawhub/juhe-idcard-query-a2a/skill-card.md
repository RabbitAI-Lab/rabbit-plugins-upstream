## Description: <br>
This Chinese-language paid skill queries Juhe's ID-card information API to parse sex, birth date, and registered-area fields encoded in a user-provided Chinese resident ID number. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[juhemcp](https://clawhub.ai/user/juhemcp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users use this paid skill to submit a Chinese resident ID number, complete Alipay payment, and receive the basic information encoded in that number. It is not intended for identity verification, real-name authentication, or determining whether an ID document is genuine. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill handles Chinese resident ID numbers and sends the provided number to Juhe for a paid lookup. <br>
Mitigation: Use it only with authorization and informed consent, and confirm the user accepts the privacy and payment prompt before submitting the number. <br>
Risk: Parsed ID-code information could be mistaken for identity verification or proof that a document is genuine. <br>
Mitigation: Present results as code-derived reference information only and direct users to authoritative channels for identity verification. <br>
Risk: The output could expose a complete ID number if masking rules are not followed. <br>
Mitigation: Mask the ID number in user-facing output and logs, retaining only the allowed leading and trailing characters. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/juhemcp/skills/juhe-idcard-query-a2a) <br>
- [Juhe A2A query endpoint](https://apis.juhe.cn/a2a/query) <br>
- [Output format](artifact/OUT_FORMAT.md) <br>


## Skill Output: <br>
**Output Type(s):** [markdown, shell commands, guidance] <br>
**Output Format:** [Markdown result summary with masked ID number fields and tabular parsed values; may include curl command guidance during the paid API flow.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses only fields returned by the Juhe API and must mask the original ID number in user-facing output.] <br>

## Skill Version(s): <br>
1.1.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

## Description: <br>
根据用户提供的居民身份证号码调用聚合数据付费接口，解析性别、出生日期、户口所在地等编码自带基础信息，并明确不提供证件真伪或公安实名核验。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[juhemcp](https://clawhub.ai/user/juhemcp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and their agents use this skill to perform a paid, consent-based lookup of basic coding-derived information from a Chinese resident ID number. It supports single-query parsing of sex, birth date, and registered-region information, not identity verification. <br>

### Deployment Geography for Use: <br>
Global, subject to local laws and availability of Alipay payment and Juhe API services. <br>

## Known Risks and Mitigations: <br>
Risk: Review before execution as proposals could introduce incorrect or misleading guidance into skills. <br>
Mitigation: Review and scan skill before deployment. <br>

## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/juhemcp/skills/juhe-idcard-query-a2a) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/juhemcp) <br>
- [Juhe A2A query endpoint](https://apis.juhe.cn/a2a/query) <br>


## Skill Output: <br>
**Output Type(s):** [markdown, shell commands, guidance] <br>
**Output Format:** [Markdown result summary and tables, with a curl-style API request example for the agent workflow.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Masks the queried ID number, uses only Juhe API return fields, and appends a disclaimer that results cannot prove document authenticity.] <br>

## Skill Version(s): <br>
1.1.0 (source: server evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

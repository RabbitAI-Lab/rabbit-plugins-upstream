## Description: <br>
依托全球企业资料库查找目标人员或企业对应的同事及内部团队成员，梳理企业内部人脉网络，助力外贸销售和猎头人员拓展业务人脉，实现精准客户触达。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[upkuajing](https://clawhub.ai/user/upkuajing) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Recruiters, sales teams, B2B lead builders, and agents using ClawHub use this skill to find colleagues for a known company and person ID. It supports relationship mapping, talent research, and discovery of additional contacts or decision-makers after an initial key person is found. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill reads and can write UPKUAJING_API_KEY in ~/.upkuajing/.env. <br>
Mitigation: Use this skill only when you intend to use Upkuajing's API, keep the key private, and do not let the agent print or share the .env contents. <br>
Risk: Lookup, pagination, account, and recharge helper actions may consume paid account balance or create a payment flow. <br>
Mitigation: Review price or account commands before running them and require explicit confirmation before paid lookup or recharge actions. <br>
Risk: The skill sends company and person identifiers to a third-party API provider. <br>
Mitigation: Submit only identifiers you are authorized to process and check organizational privacy or compliance requirements before use. <br>


## Reference(s): <br>
- [全球企业库同事列表 API 参考](references/person-colleague-list-api.md) <br>
- [Upkuajing homepage](https://www.upkuajing.com) <br>
- [Upkuajing developer portal](https://developer.upkuajing.com/) <br>
- [Upkuajing OpenAPI pricing](https://www.upkuajing.com/web/openapi/price.html) <br>
- [ClawHub skill page](https://clawhub.ai/upkuajing/skills/global-company-person-colleague-zh) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, Shell commands, Guidance] <br>
**Output Format:** [Markdown guidance with Python command snippets and JSON API results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires UPKUAJING_API_KEY; paid lookup calls can return fee and account-balance information.] <br>

## Skill Version(s): <br>
1.0.3 (source: SKILL.md metadata and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

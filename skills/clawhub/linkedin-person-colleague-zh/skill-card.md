## Description: <br>
依托 LinkedIn 数据，结合人员与企业信息检索同事和团队成员清单，梳理企业内部人际关联与组织架构，发掘可对接的潜在商务联系人。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[upkuajing](https://clawhub.ai/user/upkuajing) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External recruiters, sales teams, and B2B lead builders use this skill to look up colleagues and team members for a known LinkedIn company ID and person ID. It helps map team relationships, expand contact lists, and support organization research. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses a paid Upkuajing API and can create recharge or payment links when the account balance is insufficient. <br>
Mitigation: Confirm pricing, user intent, and payment actions before each lookup, pagination request, recharge order, or payment-link handoff. <br>
Risk: The Upkuajing API key may be stored locally in plaintext at ~/.upkuajing/.env. <br>
Mitigation: Protect the file as a credential, restrict local access, avoid sharing logs or screenshots that expose it, and rotate the key if it is disclosed. <br>
Risk: Colleague lookup results can contain professional relationship data tied to specific people and companies. <br>
Mitigation: Use the results only for authorized business research and collect only the pages needed for the stated task. <br>


## Reference(s): <br>
- [领英同事列表 API 参考](references/linkedin-person-colleague-list-api.md) <br>
- [ClawHub skill page](https://clawhub.ai/upkuajing/skills/linkedin-person-colleague-zh) <br>
- [Upkuajing homepage](https://www.upkuajing.com) <br>
- [Upkuajing developer platform](https://developer.upkuajing.com/) <br>
- [Upkuajing OpenAPI pricing](https://www.upkuajing.com/web/openapi/price.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [JSON responses with concise Markdown guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Returns paginated colleague records with person IDs, company IDs, job titles, cursor data, and fee information when calls succeed.] <br>

## Skill Version(s): <br>
1.0.4 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

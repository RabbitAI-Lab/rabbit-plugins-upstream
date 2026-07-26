## Description: <br>
Fetch real-time data from 9 Tcsl API modules with 99 endpoints covering restaurant, supply chain, orders, payments, and member management. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[woai36d](https://clawhub.ai/user/woai36d) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and integration teams use this skill to browse the Tian Cai Shang Long open platform API catalog, compare available modules, and identify endpoint names, paths, parameters, examples, and sandbox or production base URLs for restaurant, supply chain, order, payment, and member workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Several query-style solution mappings point to business-changing, account-changing, payment, or refund endpoints. <br>
Mitigation: Verify the underlying API name, path, and effect before letting an agent rely on a mapped endpoint, especially for create, update, delete, payment, and refund workflows. <br>
Risk: The catalog can help select endpoints for operational restaurant, order, supply chain, member, and payment systems, where a wrong endpoint choice could affect business data. <br>
Mitigation: Use the skill as reference material only, and manually review endpoint choices, parameters, base URLs, and sandbox versus production targets before implementation. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/woai36d/skills/tcsl-api-fetcher) <br>
- [TCSL open platform documentation](https://open.tcsl.com.cn/document/1?id=1671367443003474005) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, guidance] <br>
**Output Format:** [Text or Markdown API reference guidance with module summaries, endpoint paths, request and response parameter details, examples, and solution-to-endpoint mappings.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The artifact is a static API catalog covering 99 endpoints across 9 modules, with mappings for 108 business features and multiple sandbox or production base URLs.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

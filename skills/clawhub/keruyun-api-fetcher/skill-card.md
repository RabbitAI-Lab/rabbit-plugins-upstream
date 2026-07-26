## Description: <br>
Fetch and organize detailed Keruyun Open Platform API metadata, including endpoints, parameters, response examples, and module categorization for 178 APIs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[woai36d](https://clawhub.ai/user/woai36d) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and integration engineers use this skill to look up Keruyun Open Platform API endpoints, request parameters, response examples, modules, and solution mappings before implementing integrations. Sensitive business and financial workflows should be checked against official Keruyun documentation before use. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security summary reports verified mismatches in sensitive business and financial workflow mappings that could cause wrong API use. <br>
Mitigation: Manually verify endpoint paths, parameters, and examples against official Keruyun documentation before using the catalog for implementation. <br>
Risk: Payments, transfers, coupons, stored value, points, refunds, and callbacks may be high-impact if an agent acts on incorrect catalog mappings. <br>
Mitigation: Do not let an agent execute or automate those workflows directly from this catalog until the mappings and examples have been audited. <br>


## Reference(s): <br>
- [Keruyun Open Platform](https://open.keruyun.com/official/developer.html) <br>
- [ClawHub skill page](https://clawhub.ai/woai36d/skills/keruyun-api-fetcher) <br>
- [Full Keruyun API catalog](references/_all_apis_complete.json) <br>
- [Module-organized Keruyun API catalog](references/_modules_organized.json) <br>
- [Solution API mapping](solutions/_solution_api_mapping.json) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown text with JSON excerpts and inline shell or code snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses bundled JSON reference data for endpoint lookup, module breakdowns, and solution mappings; the skill should not execute Keruyun business workflows directly.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

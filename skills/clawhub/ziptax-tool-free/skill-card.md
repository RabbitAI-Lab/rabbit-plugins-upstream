## Description: <br>
Provides U.S. sales-tax lookup guidance for agents using zip-tax.com by address, ZIP code, or coordinates, with basic CLI examples and tax-rate parsing. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to prepare and run U.S. sales-tax lookup requests against zip-tax.com, interpret state, county, city, and district rates, and handle API-key setup and response codes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requests read, write, and exec authority and contains unrelated create, modify, delete, import, and export language beyond sales-tax lookup. <br>
Mitigation: Limit use to address, ZIP, coordinate, and metrics queries, and review proposed commands before execution. <br>
Risk: API keys and address data may be exposed through shell history, source files, front-end code, or third-party API transmission. <br>
Mitigation: Store the API key using normal secret-management practices and submit personal addresses only when zip-tax.com transmission is acceptable. <br>
Risk: Sales-tax results can become stale or vary by precise address and tax district. <br>
Mitigation: Prefer exact address lookups, check response codes, and refresh cached rates for checkout or other decision-critical workflows. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/ziptax-tool-free) <br>
- [Zip-Tax API request endpoint](https://api.zip-tax.com/request/v60) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Code, Configuration] <br>
**Output Format:** [Markdown with inline bash, curl, and JavaScript examples plus JSON response examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a ZIPTAX_API_KEY environment variable and network access to zip-tax.com.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

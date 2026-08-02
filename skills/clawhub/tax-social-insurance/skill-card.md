## Description: <br>
Social-insurance tax compliance assistant for social-insurance fee collection, contribution-base checks, individual income tax matching, worker-classification boundaries, back-payment handling, CPA accounting adjustments, risk grading, audit response, and structured self-check workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External business users, finance teams, payroll teams, tax professionals, and compliance reviewers use this skill to assess Chinese social-insurance contribution-base compliance, compare payroll and individual-income-tax data, classify employment arrangements, estimate remediation exposure, and prepare practical self-check or整改 workflows. The skill can also provide local fallback checklists and connect agents to a broader cloud MCP tax-policy service when configured. <br>

### Deployment Geography for Use: <br>
China <br>

## Known Risks and Mitigations: <br>
Risk: The skill includes remote cloud/MCP tax-policy tooling beyond a narrow local social-insurance guide. <br>
Mitigation: Review the remote endpoint, enabled MCP tools, data flow, logging, retention, and organizational approval requirements before installing or using online features. <br>
Risk: The bundled clients may persist API credentials, client identifiers, cache entries, and logs locally. <br>
Mitigation: Use a controlled profile or sandbox for evaluation, inspect local storage paths before production use, and avoid entering sensitive payroll, employee identity, investigation, or tax dispute details unless retention is acceptable. <br>
Risk: Optional setup behavior can modify supported agent MCP configuration when explicitly enabled. <br>
Mitigation: Keep automatic setup disabled during review, inspect proposed MCP configuration changes, and back up client configuration before enabling setup. <br>
Risk: Social-insurance and tax guidance can become stale or vary by local authority. <br>
Mitigation: Confirm material conclusions against current official tax, social-insurance, and local agency guidance before filing, remediating, or making employment decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-social-insurance) <br>
- [Publisher profile](https://clawhub.ai/user/zxj2devs) <br>
- [Social-insurance self-check workflow](https://mcp.aitaxs.top/web/topic_workflow_social_insurance.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance, configuration, shell commands] <br>
**Output Format:** [Markdown and structured text with optional configuration snippets or command-line guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May call remote MCP tax-policy tools or provide offline reference workflows depending on client configuration and service availability.] <br>

## Skill Version(s): <br>
3.15.7 (source: evidence.release.version and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

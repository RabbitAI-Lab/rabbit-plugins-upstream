## Description: <br>
beehiiv API integration with managed OAuth for managing newsletter publications, subscriptions, posts, custom fields, segments, and automations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[byungkyu](https://clawhub.ai/user/byungkyu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, operators, and newsletter teams use this skill to let an agent read and manage beehiiv publications, subscribers, posts, segments, custom fields, tiers, and automations through Maton-managed OAuth. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Requests are routed through Maton and may affect real beehiiv newsletter data. <br>
Mitigation: Use a valid MATON_API_KEY, confirm the intended OAuth connection, and review the target publication or resource before approving write or delete actions. <br>
Risk: Multiple beehiiv connections can cause actions to target the wrong account. <br>
Mitigation: Specify the intended connection ID when more than one connection exists. <br>
Risk: Create, update, and delete operations can change subscribers, posts, custom fields, tiers, or automations. <br>
Mitigation: Require explicit approval for write operations after checking the resource and intended effect. <br>


## Reference(s): <br>
- [ClawHub beehiiv skill](https://clawhub.ai/byungkyu/skills/beehiiv) <br>
- [byungkyu ClawHub profile](https://clawhub.ai/user/byungkyu) <br>
- [beehiiv Developer Documentation](https://developers.beehiiv.com/) <br>
- [beehiiv API Reference](https://developers.beehiiv.com/api-reference) <br>
- [Maton](https://maton.ai) <br>
- [Maton settings](https://maton.ai/settings) <br>
- [Maton API gateway](https://api.maton.ai) <br>
- [api-gateway skill](https://clawhub.ai/byungkyu/api-gateway) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, code, configuration, API calls] <br>
**Output Format:** [Markdown with inline shell, Python, JavaScript, HTTP, and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires network access, a MATON_API_KEY environment variable, and a valid beehiiv OAuth connection through Maton.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

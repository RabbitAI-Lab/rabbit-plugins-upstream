## Description: <br>
Automates AdCP advertising workflows for campaign discovery, media buying, creative management, budget optimization, targeting, and performance tracking through natural language. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[edyyy62](https://clawhub.ai/user/edyyy62) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Marketing teams, media buyers, agencies, e-commerce brands, and startups use this skill to discover ad inventory, launch and update campaigns, manage creatives, monitor ROI, and optimize budgets through AdCP-compatible agents. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Agent-driven campaign creation, launch, resume, budget changes, targeting changes, creative uploads, and destructive syncs can affect real advertising spend. <br>
Mitigation: Require explicit human approval for those actions and configure spend limits before using the skill in a production advertising workflow. <br>
Risk: Real advertising credentials can expose paid media accounts and campaign data if mishandled. <br>
Mitigation: Use the public test agent only for testing and store real credentials in a managed secret store. <br>
Risk: Tracking pixels and audience targeting can create privacy or compliance exposure. <br>
Mitigation: Run privacy and compliance checks before enabling tracking pixels or audience targeting in live campaigns. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/edyyy62/skills/adcp-advertising) <br>
- [Official AdCP Documentation](https://docs.adcontextprotocol.org) <br>
- [AdCP Documentation Index](https://docs.adcontextprotocol.org/llms.txt) <br>
- [AdCP Media Buy Protocol](https://docs.adcontextprotocol.org/docs/media-buy/) <br>
- [AdCP Media Buy Task Reference](https://docs.adcontextprotocol.org/docs/media-buy/task-reference/) <br>
- [AdCP Creative Documentation](https://docs.adcontextprotocol.org/docs/creative/) <br>
- [AdCP Targeting Documentation](https://docs.adcontextprotocol.org/docs/media-buy/advanced-topics/targeting) <br>
- [AdCP Protocol Comparison](https://docs.adcontextprotocol.org/docs/building/understanding/protocol-comparison) <br>
- [Official AdCP Repository](https://github.com/adcontextprotocol/adcp) <br>
- [Skill README](artifact/README.md) <br>
- [Skill API Reference](artifact/REFERENCE.md) <br>
- [Skill Examples](artifact/EXAMPLES.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with JavaScript, JSON, and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May describe AdCP API calls that create or modify campaigns, budgets, targeting, creatives, and delivery reports.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

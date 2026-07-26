## Description: <br>
Local tariff data source contract for SmartClaws master agents that defines the tariff snapshot file schema and how to use it during control decisions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[eduv09](https://clawhub.ai/user/eduv09) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers and SmartClaws operators use this skill to tell a master agent how to read, validate, and apply a local off-chain electricity tariff snapshot during control cycles. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: An agent could treat stale, missing, or malformed tariff data as authoritative. <br>
Mitigation: Validate the snapshot schema and freshness timestamp before each control cycle; when the data is missing, stale, or invalid, run a conservative control cycle and report the tariff source issue. <br>
Risk: A local tariff source could be misread as permission to access unrelated local files. <br>
Mitigation: Provide only the intended tariff snapshot path in SMARTCLAWS.md and keep the skill scoped to that path. <br>
Risk: Local tariff data could be published to device channels unintentionally. <br>
Mitigation: Keep tariff data local unless the owner explicitly instructs the agent to publish it. <br>


## Reference(s): <br>
- [SmartClaws homepage](https://github.com/skalenetwork/smartclaws) <br>
- [ClawHub skill page](https://clawhub.ai/eduv09/skills/smartclaws-tariff-file-source) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, guidance] <br>
**Output Format:** [Markdown guidance with a JSON tariff snapshot schema] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guides agents to read a local tariff snapshot, validate freshness and schema fields, and choose conservative behavior when data is unavailable or invalid.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

## Description: <br>
车辆尽调报告 Pro（标准版）通过 VIN、车辆类型和事故/非法改装情况发起一次付费查询，生成包含车辆配置、登记信息、过户流转和车检估算的购前快检报告。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[juhemcp](https://clawhub.ai/user/juhemcp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Consumers, vehicle buyers, and finance or insurance reviewers use this skill to check a specific VIN before a vehicle transaction. It collects only the VIN, vehicle type, and accident/modification status needed for the paid report, then renders a structured Markdown summary for review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends a VIN, vehicle type, and accident/modification status to a third-party vehicle-data provider and uses Alipay for payment. <br>
Mitigation: Before installation and use, confirm the user is comfortable with that data flow; the skill limits collection to the stated fields, avoids extra personal data, and instructs agents not to store query data locally. <br>
Risk: A paid query could be started with missing or invalid vehicle inputs. <br>
Mitigation: Require VIN validation, explicit vehicle type, and explicit accident/modification status before any payment or provider request. <br>
Risk: Vehicle report data may be incomplete, delayed, or unsuitable as the only basis for a purchase, lending, or insurance decision. <br>
Mitigation: Present results as reference information, mask returned plate numbers, avoid deterministic buy/sell advice, and direct users to official vehicle registration and manufacturer sources for confirmation. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/juhemcp/skills/juhe-vehicle-dd-pro-a2a) <br>
- [Juhe A2A vehicle query endpoint](https://apis.juhe.cn/a2a/query) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Shell commands, Guidance] <br>
**Output Format:** [Markdown report with tables, user-facing collection prompts, and HTTPS JSON request examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reports must mask plate numbers, avoid raw JSON in user-facing output, and include reference-only caveats.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

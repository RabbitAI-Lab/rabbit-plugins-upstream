## Description: <br>
FDE helps deployment teams map enterprise workflows, identify AI-suitable nodes, build knowledge domains, install the sofagent base, and produce handoff materials with ongoing optimization reports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kongfangxun](https://clawhub.ai/user/kongfangxun) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Enterprise deployment engineers and customer IT teams use this skill to plan and operate a sofagent deployment: workflow discovery, AI node classification, knowledge-domain setup, audit handoff, USB deployment planning, and sustain-mode optimization. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill guides broad installation and daemon-style operation on enterprise devices. <br>
Mitigation: Review shell commands before execution, confirm target devices and paths, and run deployment verification before using the setup with production workflows. <br>
Risk: The skill can create or manage local .sofagent data that may retain business context, audit logs, and extracted knowledge. <br>
Mitigation: Define retention, redaction, and sensitivity rules for .sofagent data before using the skill with sensitive enterprise information. <br>
Risk: USB deployment and external forwarding workflows can move runtime assets or audit data outside the primary workstation. <br>
Mitigation: Confirm USB mount paths and target platforms, disable external forwarding unless reviewed, and require human approval before webhook or USB workflows are used. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/kongfangxun/skills/sofagent-fde) <br>
- [FDE capability model](artifact/FDE.md) <br>
- [FDE README](artifact/README.md) <br>
- [Non-developer quick start](artifact/quick-start.md) <br>
- [Delivery templates](artifact/templates/README.md) <br>
- [OpenFDE white paper](https://open-fde.com/zh/white-book) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and generated deployment templates] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces enterprise profiles, deployment plans, node templates, skill templates, handoff guidance, audit reminders, and sustain-mode optimization reports.] <br>

## Skill Version(s): <br>
1.1.9 (source: server release metadata, SKILL.md frontmatter, and package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

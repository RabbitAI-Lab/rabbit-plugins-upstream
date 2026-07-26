## Description: <br>
生成标准SIPOC流程图（供应商-输入-流程-输出-客户）；当用户需要绘制过程流程图、梳理业务输入输出、建立跨部门流程映射或准备流程文档时使用 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[duding-engicool](https://clawhub.ai/user/duding-engicool) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Process owners, quality teams, operations teams, and business analysts use this skill to collect SIPOC elements, structure them as JSON, and generate printable process diagrams for documentation and improvement work. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated HTML may include business text supplied by the user. <br>
Mitigation: Avoid attacker-supplied or untrusted text until HTML escaping is added, and review generated HTML before sharing or opening files built from external business data. <br>
Risk: The skill invokes local Python tooling to generate diagram files. <br>
Mitigation: Run the scripts in a controlled workspace and review outputs before embedding them in operational documentation. <br>


## Reference(s): <br>
- [SIPOC 绘制指南](references/sipoc-guide.md) <br>
- [Server-resolved source repository](https://github.com/duding-engicool/skill-sipoc-diagram) <br>
- [ClawHub skill page](https://clawhub.ai/duding-engicool/skills/skill-sipoc-diagram) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, JSON, Shell commands, HTML files] <br>
**Output Format:** [Markdown guidance with JSON examples and shell commands; generated SIPOC diagrams are HTML files that may be exported to PNG or PDF.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The diagram generator reads SIPOC JSON data and writes a local HTML file using the bundled CSS template.] <br>

## Skill Version(s): <br>
0.1.0 (source: ClawHub release evidence; artifact frontmatter reports 1.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

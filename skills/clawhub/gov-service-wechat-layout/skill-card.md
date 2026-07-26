## Description: <br>
Provides nine WeChat official-account layout templates and a swappable theme-color model for public-service and government-affairs articles. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[wuaron895-cpu](https://clawhub.ai/user/wuaron895-cpu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Editors and communications staff use this skill to classify a public-service article, apply the matching WeChat layout template, adjust the theme color, fill approved placeholders, and produce paste-ready HTML for publication. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated article layouts may retain placeholders or include unverified official values such as phone numbers, policy references, QR codes, or links. <br>
Mitigation: Review the generated HTML before publishing and replace all placeholders only with verified official values. <br>
Risk: The included theme-color script can modify files if pointed at the wrong input. <br>
Mitigation: Run local scripts only on files the installer intends to modify and review the resulting HTML. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/wuaron895-cpu/skills/gov-service-wechat-layout) <br>
- [README](artifact/README.md) <br>
- [English README](artifact/README_EN.md) <br>
- [Color slot model](artifact/references/color-slot-model.md) <br>
- [Component library](artifact/references/component-library.md) <br>
- [Layout SOP](artifact/references/layout-sop.md) <br>


## Skill Output: <br>
**Output Type(s):** [markdown, code, shell commands, guidance] <br>
**Output Format:** [Markdown guidance with paste-ready inline HTML and optional bash commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Generated HTML uses inline styles only and requires placeholder values to be verified before publishing.] <br>

## Skill Version(s): <br>
2.1.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

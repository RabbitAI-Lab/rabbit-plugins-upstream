## Description:

基于一个印花快速生成多个设计版本，支持不同风格、颜色及元素组合，提高 POD 设计效率。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, POD sellers, and design operators use this skill to create multiple pattern variations from a source print by changing colors, style, theme, elements, and layout density. The skill guides an agent through Qinghu qhkit image generation, estimation, setup, and result delivery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may install or upgrade the qhkit npm package globally without pinning a package version.

Mitigation: Install in an isolated environment, pin the package version where possible, and review the package source and publisher before use.

Risk: The skill requires a Qinghu API token for qhkit configuration.

Mitigation: Store the token in a protected secret store or environment variable, avoid privileged shells, and rotate the token if exposure is suspected.

Risk: Local reference images selected for generation may be uploaded to the Qinghu service.

Mitigation: Use only images approved for upload to the provider and avoid confidential, sensitive, or restricted assets.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-pod-pattern-variations)
- [autoagc publisher profile](https://clawhub.ai/user/autoagc)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu AI workbench](https://www.iqinghu.com)
- [Qinghu API keys](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash commands and JSON CLI parameters.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include generated image URLs and actual credit usage returned by qhkit.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

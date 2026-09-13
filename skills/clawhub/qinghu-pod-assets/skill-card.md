## Description:

面向 POD（Print on Demand）卖家生成设计素材：印花提取、印花贴合（mockup 效果图）、印花裂变、商品效果图，覆盖服饰、家居、饰品等 POD 品类的设计与上架。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External POD sellers and agents assisting them use this skill to guide qhkit image-generation workflows for extracting print designs, creating design variants, and placing prints onto product mockups for POD listings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can install or upgrade Node and the qhkit npm package, including unpinned latest versions.

Mitigation: Ask for user approval before installing or upgrading software, changing PATH or shell profiles, or running upgrade commands; prefer a pinned local installation in a sandbox.

Risk: The workflow uploads source images to the qhkit service and requires a qhkit token.

Mitigation: Use the skill only when the user trusts the service, avoid sensitive or unauthorized images, and provide tokens through appropriate secret handling such as environment variables.

Risk: Extracting or reusing third-party print designs for commercial POD products may create intellectual-property risk.

Mitigation: Confirm that the user has rights to the source imagery and print designs before commercial use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-pod-assets)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu AI workbench](https://www.iqinghu.com)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration]

**Output Format:** [Markdown guidance with inline shell commands and JSON CLI parameter examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill guides qhkit CLI use and expects returned image URLs and credit usage from the external service when generation succeeds.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

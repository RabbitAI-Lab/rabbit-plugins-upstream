## Description:

Rebuilds, beautifies, and optimizes editable PowerPoint flowcharts, topology diagrams, architecture diagrams, and process visuals from existing PPT/PPTX files or source images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xuyongliang-eccom](https://clawhub.ai/user/xuyongliang-eccom)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external users, developers, and presentation authors use this skill to convert or polish diagram-heavy PPT/PPTX slides and source images into clearer, editable, presentation-ready PowerPoint visuals.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper script reads PPTX archives and may consume excessive resources on untrusted or unusually large files.

Mitigation: Run it only on trusted or size-limited PPTX files and apply resource limits for batch or external inputs.

Risk: The bundled topology script uses Chinese default labels and templates that may not fit every audience.

Mitigation: Review and localize generated slide text, title, and labels before delivery.

## Reference(s):

- [Image-to-PPT Flowchart SOP](references/image-to-ppt-flowchart-sop.md)
- [PPT Topology From Image](references/ppt-topology-from-image.md)
- [PPT Polish ClawHub Listing](https://clawhub.ai/xuyongliang-eccom/skills/ppt-polish)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance plus optional PowerPoint files and Python-generated PPTX outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce editable .pptx diagrams, rebuilt single-slide pages, alternate visual versions, or Mermaid/Markdown structure drafts.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

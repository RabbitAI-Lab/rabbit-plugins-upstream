## Description:

本地读取 DWG/DXF/DWT/PDF，输出带证据的识图、拓扑和测量候选；PDF 走本机 OCR。只做识图，final_quantity=false，算量交给专项技能。

This skill is ready for commercial/non-commercial use.

## Publisher:

[lisong2003-lgtm](https://clawhub.ai/user/lisong2003-lgtm)

### License/Terms of Use:

CC BY-NC-SA 4.0

## Use Case:

CAD and building-services practitioners use this skill to inspect drawing files and produce traceable evidence, topology, semantic, comparison, and measurement candidates for human review and specialist quantity-takeoff workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan rates this release suspicious with medium confidence, citing automatic dependency installation, broad file changes, and capabilities beyond the stated drawing-reading purpose; 5 of 264 components were only partially inspected.

Mitigation: Before installing, review the install steps, cleanup or editing options, and dependency sources; install only if the skill is needed.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/lisong2003-lgtm/skills/cad-file-reader)
- [Capabilities and boundaries](artifact/CAPABILITIES.md)
- [Quick scan guide](artifact/docs/quick-scan.md)
- [Reliability guidance](artifact/docs/reliability.md)
- [CC BY-NC-SA 4.0 license text](https://creativecommons.org/licenses/by-nc-sa/4.0/)

## Skill Output:

**Output Type(s):** [JSON, Markdown, CSV, Guidance]

**Output Format:** [Evidence-backed drawing-reading candidates and reports in JSON, Markdown, CSV, XLSX, and DOCX formats]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes source evidence and review status; candidate quantities are not final quantities.]

## Skill Version(s):

0.39.6 (source: server-resolved release metadata; artifact frontmatter agrees)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

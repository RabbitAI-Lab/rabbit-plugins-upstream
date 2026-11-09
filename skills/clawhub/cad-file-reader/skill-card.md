## Description:

Extracts text, layers, block semantics, geometry evidence, and reviewable measurement candidates from CAD drawings and PDFs; it does not produce final quantities or engineering sign-off.

This skill is for research and development only.

## Publisher:

[lisong2003-lgtm](https://clawhub.ai/user/lisong2003-lgtm)

### License/Terms of Use:

CC BY-NC-SA 4.0

## Use Case:

Developers and engineering teams can inspect CAD and PDF construction drawings, compare drawing evidence, and pass traceable recognition candidates to specialist workflows for review. The skill does not calculate final quantities or determine design compliance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan rates the skill suspicious because scanners report substantial undeclared capabilities and potentially disruptive actions beyond its stated recognition and measurement-candidate purpose; analysis was partial, so the evidence is incomplete.

Mitigation: Review the reported scope and installation behavior before use. If proceeding, check whether setup downloads dependencies, changes system packages, or replaces vendor files, and restrict file access to the project under review. Treat scan conclusions as incomplete because five files were partially inspected and tool-misuse and tool-poisoning analyses were degraded.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/lisong2003-lgtm/skills/cad-file-reader)
- [ezdxf project](https://github.com/mozman/ezdxf)
- [NumPy documentation](https://numpy.org/)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown, CSV, XLSX, DOCX]

**Output Format:** [Structured recognition and measurement-candidate data with optional Markdown, CSV, spreadsheet, or document reports.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs include source evidence and review flags; measurements remain candidates and are marked final_quantity=false.]

## Skill Version(s):

0.39.7 (source: server release and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

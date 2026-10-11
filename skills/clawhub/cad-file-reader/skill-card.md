## Description:

Locally reads CAD and PDF drawings to extract traceable text, geometry, drawing semantics, and measurement candidates for human review.

This skill is for research and development only.

## Publisher:

[lisong2003-lgtm](https://clawhub.ai/user/lisong2003-lgtm)

### License/Terms of Use:

CC BY-NC-SA 4.0

## Use Case:

Developers and engineering teams use this skill to inspect DWG, DXF, DWT, and PDF drawings and prepare evidence-linked interpretation and measurement candidates. It does not provide final quantities, pricing, or design-compliance decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local drawing data and derivative reports or caches may contain sensitive project information.

Mitigation: Use explicit, access-controlled cache and output directories for sensitive projects, and review exported files before sharing.

Risk: Installing missing dependencies or using untrusted custom rules may introduce unwanted behavior.

Mitigation: Use the full package or a trusted documented dependency source, and load custom rules only from trusted directories.

Risk: Automated interpretation or measurement candidates may be incomplete or misleading.

Mitigation: Inspect source evidence and review flags; obtain qualified engineering review before using results for decisions or quantities.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/lisong2003-lgtm/skills/cad-file-reader)
- [Capabilities and boundaries](artifact/CAPABILITIES.md)

## Skill Output:

**Output Type(s):** [Analysis, Files]

**Output Format:** [Markdown, JSON, CSV, Excel, or Word reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Evidence coordinates, confidence levels, review reasons, and measurement candidates marked final_quantity=false.]

## Skill Version(s):

1.0.2 (source: ClawHub release metadata; bundled files state 0.27.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

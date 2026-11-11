## Description:

Reads DWG, DXF, DWT, and PDF drawings to extract traceable drawing evidence and discipline-specific interpretation and measurement candidates; it does not produce final quantities.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lisong2003-lgtm](https://clawhub.ai/user/lisong2003-lgtm)

### License/Terms of Use:

CC BY-NC-SA 4.0

## Use Case:

External engineering teams and CAD practitioners use it to inspect DWG/DXF/PDF drawings, retrieve traceable text, layer, block, and geometry evidence, and review discipline-specific candidates. It does not provide final quantities or design-compliance conclusions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan rates this release suspicious with high confidence, citing substantial undeclared behavior, broad file and system changes, and installation risks; its scan was partial.

Mitigation: Before installing, review the reported capabilities and installation effects, including file cleanup or redaction, persistent configuration or shared-state changes, quantity estimates, and system package installation. The partial scan cannot establish that unreported behavior is absent.

Risk: Server license metadata says MIT-0, while the bundled LICENSE.md states CC BY-NC-SA 4.0 and restricts commercial use.

Mitigation: Confirm the canonical license and align the release metadata and usage terms before publication or commercial use.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/lisong2003-lgtm/skills/cad-file-reader)
- [On-demand usage and setup guide](references/on-demand.md)
- [Reliability guidance](docs/reliability.md)
- [Candidate contract](docs/base-contract.md)
- [PDF drawing workflow](docs/pdf-pipeline.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, CSV, Guidance]

**Output Format:** [Text findings and Markdown, JSON, CSV, Excel, or Word result files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Contains traceable evidence and interpretation or measurement candidates for review; final_quantity is false.]

## Skill Version(s):

0.41.1 (source: SKILL.md frontmatter, CHANGELOG.md, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

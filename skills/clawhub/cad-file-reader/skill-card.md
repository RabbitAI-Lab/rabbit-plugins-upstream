## Description:

Locally reads CAD drawings and PDFs to extract traceable drawing evidence, discipline-specific interpretations, and measurement candidates without calculating final quantities.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lisong2003-lgtm](https://clawhub.ai/user/lisong2003-lgtm)

### License/Terms of Use:

CC BY-NC-SA 4.0

## Use Case:

Engineers and other drawing reviewers use this skill to identify CAD/PDF annotations, geometry, discipline-specific features, and drawing changes with coordinates and review flags. Its measurements are candidates for human verification, not final quantities, cost estimates, or compliance determinations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Project drawings and locally generated reports or caches may contain sensitive information.

Mitigation: Use approved local storage and access controls; review and remove sensitive reports and caches before sharing.

Risk: A lightweight installation may download parser dependencies from GitHub on first run.

Mitigation: Disable automatic setup with CAD_AUTO_SETUP=0 or install dependencies offline when network-controlled installation is required.

Risk: Automated drawing interpretations and measurements may be incomplete or misleading.

Mitigation: Check source coordinates and review flags against the drawings; do not treat candidates as final quantities or compliance findings.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/lisong2003-lgtm/skills/cad-file-reader)
- [Capability boundaries](CAPABILITIES.md)
- [Skill command and discipline index](pack-index.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [JSON and Markdown evidence reports; optional CSV, Excel, and Word exports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Evidence coordinates, confidence levels, and review reasons; final_quantity=false. The CC BY-NC-SA 4.0 license restricts reuse to non-commercial purposes.]

## Skill Version(s):

1.0.7 (source: ClawHub release; package version 0.28.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Academic Figures helps agents generate publication-ready academic charts from JSON, CSV, or Excel inputs using local Python scripts, journal presets, validation checks, accessibility alt text, and scenario templates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

External users, researchers, and developers use this skill to create academic figures, review-flow diagrams, statistical chart annotations, legends, and accessibility text for publication workflows. It is suited to local chart generation where data should stay on the user's machine.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Python dependency versions or local environment differences may affect chart rendering or verification behavior.

Mitigation: Install in a dedicated virtual environment and pin or review dependency versions before use.

Risk: Batch or command-line runs write output files and can target unintended paths.

Mitigation: Check output paths and manifests before running generation commands.

Risk: A separately promoted cloud service may have privacy or retention terms that are not suitable for sensitive data.

Mitigation: Do not use the cloud service with PHI, unpublished research, or proprietary data unless its privacy and retention terms are acceptable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/docsor1212/skills/academic-figures)
- [Limits and compatibility](artifact/references/limits.md)
- [Data formats](artifact/references/data-formats.md)
- [Composite layouts](artifact/references/composite-layouts.md)
- [Pitfalls](artifact/references/pitfalls.md)
- [Scenario templates](artifact/templates/README.md)
- [Examples](artifact/examples/README.md)
- [Clinical lab trends](artifact/references/clinical-lab-trends.md)
- [GLM-5.2 blog](https://z.ai/blog/glm-5.2)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with bash commands and JSON examples; generated artifacts may include PNG, SVG, PDF, TIFF, EPS, and alt-text files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally with Python dependencies including matplotlib, numpy, PyMuPDF, scipy, and openpyxl; security evidence reports no hidden exfiltration, persistence, or destructive behavior.]

## Skill Version(s):

2.3.0 (source: SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

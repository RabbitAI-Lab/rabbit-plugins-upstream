## Description:

Generates offline CSV/JSON data visualizations by inferring column types and producing static SVG charts, an HTML dashboard, and a summary JSON file with pure Python and no matplotlib or pandas dependency.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qq435912743](https://clawhub.ai/user/qq435912743)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and data practitioners use this skill to turn local CSV or JSON datasets into quick exploratory dashboards, including histograms, scatter plots, bar charts, and summary statistics. It is useful in restricted environments where installing larger visualization packages is not practical.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled learner records free-form usage details and can be pointed at directories outside this skill.

Mitigation: Keep learner state in directories you control, avoid recording sensitive details, and do not run the learner against unrelated skill directories.

Risk: Generated SVG and HTML may include dataset-derived text.

Mitigation: Use trusted datasets or inspect generated files before opening or sharing them, especially when source data may contain untrusted text.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qq435912743/skills/data-viz)

## Skill Output:

**Output Type(s):** [Shell commands, Files, Code, Guidance]

**Output Format:** [Markdown guidance with Python command examples; generated artifacts are SVG, HTML, and JSON files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The visualization script writes standalone chart files, index.html, and summary.json to a user-selected output directory.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Publication-ready scientific figures from one command, covering 22 chart types, journal presets, multi-format export, local data handling, a Python API, and verification gates for publication-quality outputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

External users, researchers, and developers use this skill to turn JSON, CSV, or Excel data into publication-ready academic figures, supplementary legends, alt text, and validation reports. It is suited for local scientific plotting workflows that need journal presets, accessibility output, and pre-submission checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill reads user-selected data files and writes figures or reports to chosen output paths.

Mitigation: Run it only on intended local datasets and review output paths before executing single-figure, batch, or pipeline commands.

Risk: Batch and pipeline modes can create multiple files.

Mitigation: Use a dedicated output directory and inspect generated batch reports before sharing or publishing results.

Risk: setup_env.py may clear the local matplotlib font cache.

Mitigation: Run environment setup in a project environment and expect matplotlib to rebuild its cache afterward.

Risk: Many diagnostics are Chinese-heavy, which may make failures harder for some operators to interpret.

Mitigation: Review command output carefully and use the bundled quickstart, FAQ, limits, and troubleshooting references when resolving validation or rendering errors.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/docsor1212/skills/academic-figures)
- [Quickstart](artifact/references/quickstart.md)
- [Data Formats](artifact/references/data-formats.md)
- [Limits and Compatibility](artifact/references/limits.md)
- [Python API](artifact/references/python-api.md)
- [Changelog](artifact/references/changelog.md)
- [MedWiki related resource](https://docsor.cn/?from=academic-figures)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Code, Files, Text, Guidance]

**Output Format:** [Markdown guidance with command examples, JSON configuration templates, Python code, generated figure files, text legends, alt text, and batch reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill runs locally and writes figures or reports to user-selected output paths; pipeline and batch modes can create multiple outputs.]

## Skill Version(s):

3.1.0 (source: server release metadata and changelog, released 2026-09-21)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Academic Figures helps agents generate publication-ready scientific charts and journal-formatted figure files from JSON, CSV, or Excel data using local Python scripts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and researchers use this skill to create publication-ready academic figures, journal presets, multi-format exports, and figure-validation artifacts from structured data. It is suited for local chart generation workflows where data should remain on the user's machine.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill runs local Python plotting scripts that read user data files and write figures or reports to disk.

Mitigation: Run it only in workspaces where local file reads and writes are expected, review output paths before execution, and keep source data backups.

Risk: Environment setup may install dependencies, update font caches, or clean local caches.

Mitigation: Review scripts/setup_env.py before running setup and use an isolated Python environment when cache or dependency changes matter.

Risk: Generated scientific figures can be misleading if input data, chart choice, or verification settings are wrong.

Mitigation: Use the documented data-format checks, limits guidance, and PDF verification or audit commands before submitting figures.

Risk: Many diagnostics and error messages are Chinese-first, which can slow review for non-Chinese readers.

Mitigation: Plan for translation or bilingual review of diagnostics when using the skill in English-only workflows.

## Reference(s):

- [README](README.md)
- [Skill Instructions](SKILL.md)
- [Quick Start](references/quickstart.md)
- [Cheat Sheet](references/cheatsheet.md)
- [Limits and Compatibility](references/limits.md)
- [Data Format Reference](references/data-formats.md)
- [Python API](references/python-api.md)
- [Pitfalls](references/pitfalls.md)
- [Changelog](references/changelog.md)
- [Template Index](templates/README.md)

## Skill Output:

**Output Type(s):** [Shell commands, Code, Configuration, Markdown, Files, Guidance]

**Output Format:** [Markdown guidance with shell commands, JSON data examples, and generated figure/report files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are produced locally and may include PDF, PNG, TIFF, SVG, EPS, alt-text, legends, and validation diagnostics.]

## Skill Version(s):

3.3.0 (source: server release metadata and changelog, released 2026-09-24)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

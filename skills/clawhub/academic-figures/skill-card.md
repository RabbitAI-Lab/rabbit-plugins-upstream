## Description:

Publication-ready scientific figures from one command, covering 22 chart types, journal presets, multi-format export, Python API use, and local data handling.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, researchers, and technical writers use this skill to create publication-ready scientific charts from JSON, CSV, TSV, Excel, or YAML pipeline inputs. It supports journal-oriented figures, statistical chart workflows, accessibility sidecars, and verification guidance for manuscript submission outputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local Python scripts read user datasets and write figure, sidecar, report, or demo files.

Mitigation: Run commands only on intended inputs in a writable working directory, then review generated files before use or publication.

Risk: setup_env.py may install dependencies and clear the matplotlib font cache.

Mitigation: Run setup_env.py only when you intentionally want environment setup; skip it when dependencies and fonts are already managed.

Risk: A historical reference note discusses optional web fetching outside the core local workflow.

Mitigation: Use the documented local rendering workflow and avoid historical curl or download notes when a strict no-network workflow is required.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/docsor1212/skills/academic-figures)
- [Quickstart](artifact/references/quickstart.md)
- [Data Format Reference](artifact/references/data-formats.md)
- [Limits and Compatibility](artifact/references/limits.md)
- [Python API](artifact/references/python-api.md)
- [Changelog](artifact/references/changelog.md)
- [Publisher Documentation Site](https://docsor.cn)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Code, Markdown, Guidance, Files]

**Output Format:** [Markdown guidance with bash and Python snippets plus JSON/YAML data examples; generated artifacts may include PNG, SVG, PDF, TIFF, EPS, alt-text, captions, and report files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally with user-provided data files and can emit multi-format figure outputs, sidecar text files, and diagnostics.]

## Skill Version(s):

3.2.0 (source: server release metadata and artifact changelog, released 2026-09-22)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

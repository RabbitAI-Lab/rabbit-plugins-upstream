## Description:

Helps agents create publication-ready scientific figures from local data using chart templates, journal presets, and plotting commands.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, authors, and developers use this skill to turn local scientific data into static, journal-ready figures and reproducible plotting workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Plotting reads local data and writes figure files, potentially including sensitive research data in reproduction bundles.

Mitigation: Use trusted input files and check output locations and reproduction bundles before sharing them.

Risk: Optional dependency installation can access the network and change the local Python environment.

Mitigation: Run setup_env.py --fix or the MCP uvx install only when dependency installation and network access are acceptable.

Risk: Regression tests may execute repository command strings through the shell.

Mitigation: Do not run the test suite on untrusted modifications.

## Reference(s):

- [ClawHub release](https://clawhub.ai/docsor1212/skills/academic-figures)
- [Getting started](references/quickstart.md)
- [Data formats](references/data-formats.md)
- [Limits and flag interactions](references/limits.md)
- [Python API](references/python-api.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration]

**Output Format:** [Markdown with command examples and figure configuration]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Running the plotting commands creates static figure files; optional audit and reproduction bundles are written locally.]

## Skill Version(s):

5.1.0 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Runs a local virtual-screening workflow for human pancreatic lipase (PDB 1LPB), preparing ligands, docking them across five validated sites, validating results, and producing reports.

This skill is for research and development only.

## Publisher:

[orionshaowswmw](https://clawhub.ai/user/orionshaowswmw)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers and computational biology developers use this skill to run authorized pancreatic-lipase docking experiments, compare ligand scores across multiple binding sites, and generate reports for follow-up review. Results are computational predictions and should be independently validated before scientific or business decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-run workflow can extract and run a large bundled scientific code archive.

Mitigation: Run in a disposable project directory, container, or dedicated conda environment and review the extracted docking_professional_stack before execution.

Risk: First-run behavior may auto-install packages in the user's environment.

Mitigation: Avoid shared Python environments; prefer an isolated environment and inspect install commands before running the helper.

Risk: Optional AI-provider report analysis could share sensitive ligand libraries or derived results.

Mitigation: Keep optional AI analysis disabled for sensitive inputs unless external sharing is intended and approved.

Risk: Docking scores are computational predictions and may be misleading if treated as experimental evidence.

Mitigation: Use the built-in validation checks and require independent scientific or experimental validation before relying on results.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/orionshaowswmw/skills/pancreatic-lipase-pro-docking)
- [Publisher profile](https://clawhub.ai/user/orionshaowswmw)
- [Skill documentation](artifact/SKILL.md)
- [README](artifact/README.md)
- [Changelog](artifact/CHANGELOG.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples; workflow outputs may include CSV results, logs, and reports.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs local scientific tooling and may create project-local result directories, extracted workflow files, and validation artifacts.]

## Skill Version(s):

100.4.1 (source: frontmatter, changelog, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Standardized ClearML metrics logging patterns for PDEBench experiment scripts, including train loss, validation metrics, competition scores, PDE residuals, TensorBoardX integration, and dist/expflow compatibility.

This skill is ready for commercial/non-commercial use.

## Publisher:

[diamond2nv](https://clawhub.ai/user/diamond2nv)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and ML engineers use this skill to add consistent ClearML scalar logging to PDEBench training and evaluation scripts so expflow workflows can compare scores, track validation metrics, and monitor runs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing or invoking expflow-pde without version control may introduce unreviewed package behavior.

Mitigation: Use a trusted or pinned expflow-pde version where possible before applying the skill's installation commands.

Risk: The expflow MCP server may expose tools that should be reviewed before agent use.

Mitigation: Review the expflow MCP server surface before enabling it in an agent environment.

Risk: ClearML run metadata can include sensitive paths, tags, or experiment results.

Mitigation: Configure ClearML with approved endpoints and redact sensitive experiment metadata.

## Reference(s):

- [expflow homepage](https://github.com/diamond2nv/expflow)
- [ClawHub skill page](https://clawhub.ai/diamond2nv/skills/clearml-metrics-logging-pattern)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with Python, shell, and YAML snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Provides metric naming conventions and integration templates for ClearML, TensorBoardX, and expflow workflows.]

## Skill Version(s):

0.7.1 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

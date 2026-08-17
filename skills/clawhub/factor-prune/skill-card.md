## Description:

Factor Prune helps agents select high-validity, low-redundancy stock factors from stock-factor outputs using greedy forward selection and correlation pruning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mifochen](https://clawhub.ai/user/mifochen)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and quantitative research teams use this skill to prune large stock-factor candidate pools into smaller factor lists with stronger validity and lower redundancy. The skill supports file-driven pruning, replayable matrix-cache pruning, and top/bottom 10% window-based selection for downstream factor work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow reads bundled factor spreadsheets and writes local analysis outputs.

Mitigation: Review the generated local output and state files before using the selected factors downstream.

Risk: The workflow calls a QuantAll MCP service, which could be unsafe if directed to an untrusted remote endpoint.

Mitigation: Use a trusted QuantAll instance and avoid pointing --mcp-url at untrusted remote services.

Risk: Starting duplicate QuantAll instances can create operational conflicts for the pruning workflow.

Mitigation: Start QuantAll manually and keep a single intended instance running before invoking the skill.

## Reference(s):

- [ClawHub factor-prune release page](https://clawhub.ai/mifochen/skills/factor-prune)
- [Skill documentation](artifact/SKILL.md)
- [Runtime requirements](artifact/requirements.txt)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Files]

**Output Format:** [Markdown guidance with shell commands and local XLSX outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces pruned factor-list spreadsheets such as factor-pure.xlsx or pruned_factors.xlsx; does not perform factor synthesis, strategy backtesting, or portfolio construction.]

## Skill Version(s):

1.0.0 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

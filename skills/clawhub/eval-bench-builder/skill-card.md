## Description:

Helps developers turn capability specifications and edge cases into reproducible evaluation cases with expected results and judging criteria.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT (code only); documentation and theory all rights reserved

## Use Case:

Developers and evaluation teams use this skill to create structured, repeatable test cases for agents, models, or skills from capability descriptions and boundary cases.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The benchmark generator writes a file at the chosen output path.

Mitigation: Review the path before running the script and avoid replacing important files.

Risk: The package's documentation and theory are excluded from its stated code license, and release metadata lists a different license.

Mitigation: Review the package license and confirm rights before redistributing documentation or theory text.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/zhaoxinghua09-cell/skills/eval-bench-builder)
- [Publisher homepage](https://zhaoxinghua09-cell.github.io/lgd-hub/)

## Skill Output:

**Output Type(s):** [Markdown guidance, Shell commands, JSONL evaluation cases]

**Output Format:** [Markdown guidance and a UTF-8 JSONL benchmark file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Each generated case contains capability, input, expect, and judge fields; the script writes to the selected output path.]

## Skill Version(s):

1.0.2 (source: server-resolved ClawHub release; artifact version labels differ)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

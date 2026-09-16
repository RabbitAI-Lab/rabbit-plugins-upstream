## Description:

This skill helps solo knowledge creators evaluate and shape short-video topics through problem exploration, supply-demand checks, benchmark signals, real-data evidence, and concise candidate guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iamzifei](https://clawhub.ai/user/iamzifei)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and their agents use this skill to decide whether a short-video topic is worth making, turn a flat topic into competing angles, or produce a small set of evidence-labeled topic candidates for the creator to choose from.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may trust local vault rules and repository scripts that are outside the artifact.

Mitigation: Use it only in trusted workspaces, review referenced vault files and scripts before execution, and require explicit confirmation before running commands.

Risk: The workflow can persist feedback or candidate decisions into local files.

Mitigation: Review or disable automatic writeback before using it in shared or sensitive repositories, and inspect resulting diffs before keeping them.

Risk: Topic recommendations can depend on unverified local data, benchmark pools, or inferred audience demand.

Mitigation: Require outputs to mark unsupported claims as inference, cite available data paths, and keep unverified ideas out of Ready or publication states.

Risk: Server-resolved source provenance is unavailable for this release.

Mitigation: Review the artifact contents and recorded hashes before deployment; do not infer GitHub provenance from the skill text.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/iamzifei/skills/zmm-topic)
- [问题探寻与共鸣](references/问题探寻与共鸣.md)
- [选题三路](references/选题三路.md)
- [常识缺口法](references/常识缺口法.md)
- [找拉力](references/找拉力.md)
- [规则卡](references/规则卡.md)
- [议程与合集](references/议程与合集.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with structured candidate lists, diagnostic judgments, and optional shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should label evidence strength, avoid fabricated data, and pause for creator choice rather than auto-selecting a final topic.]

## Skill Version(s):

0.2.10 (source: ClawHub release evidence and target metadata; artifact frontmatter reports 0.5.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

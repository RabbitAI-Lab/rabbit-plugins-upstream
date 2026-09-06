## Description:

Reviews talking-head and whiteboard scripts from the viewer's perspective to identify likely drop-off points, explain what the audience already has or is still waiting for, and propose marked edits after user consent.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iamzifei](https://clawhub.ai/user/iamzifei)

### License/Terms of Use:

MIT-0

## Use Case:

Content creators and script reviewers use this skill to audit short-form video scripts for retention risks, especially missing transitions, repeated points, and sentences that are hard to follow aloud. It is aimed at solo knowledge creators who need direct diagnosis and optional marked edits without changing the script's core claims, examples, data, or point of view.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may read prior shared context or memory while reviewing scripts.

Mitigation: Install only where that context is appropriate for script review, and treat memory-derived material as user data that should be reviewable.

Risk: The skill may store user feedback or retention observations in persistent memory.

Mitigation: Require explicit user confirmation before writing corrections or retention notes to persistent memory.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/iamzifei/skills/zmm-flow)
- [Publisher profile](https://clawhub.ai/user/iamzifei)
- [Evaluation README](evals/README.md)
- [Evaluation result sample 01 v0.2.0](evals/results/sample-01-v0.2.0.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown report with timeline tables, quoted script excerpts, drop-off classifications, concrete revision suggestions, and optional marked edits.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May read prior shared context and memory when available; may ask for consent before persistent memory writes or marked rewrite steps.]

## Skill Version(s):

0.2.6 (source: server release evidence; artifact frontmatter version is 0.2.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

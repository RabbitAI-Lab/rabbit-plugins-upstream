## Description:

Reviews talking-head scripts before publication with sentence-level information-density scoring, structure checks, red-line compliance checks, and oral-delivery feedback while defaulting to diagnosis rather than rewriting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iamzifei](https://clawhub.ai/user/iamzifei)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and writing-focused agents use this skill to decide whether a drafted talking-head script is ready to publish, needs targeted revision, or should return to scripting. It is aimed at solo knowledge creators who need a direct pre-publication review of content density, structure, audience fit, and platform red lines.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may persist user feedback or review calibration into local framework and memory files without asking for explicit approval each time.

Mitigation: Review or disable the automatic writeback and memory instructions before using the skill on sensitive drafts, and require explicit approval before saving feedback.

Risk: The skill asks the agent to read local writing-rule and memory files, which may expose sensitive drafting context to the active agent session.

Mitigation: Install and run it only in workspaces where those local rule and memory files are intended to be available to the agent.

## Reference(s):

- [Scoring Anchors](artifact/references/评分锚点.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown diagnostic report with scoring tables, pass/fail checks, and targeted revision guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Default output is diagnostic; full rewrites occur only after the user explicitly asks for revision.]

## Skill Version(s):

0.2.2 (source: ClawHub release evidence; artifact frontmatter reports 0.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

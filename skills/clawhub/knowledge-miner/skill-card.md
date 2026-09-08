## Description:

Knowledge Miner analyzes Git commits or visible session evidence to teach the causal chain behind recent work using Feynman-style explanations and a minimal build-from-scratch exercise.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wlykan](https://clawhub.ai/user/wlykan)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and learners use this skill to turn a specified commit, the latest three commits, or visible session evidence into an evidence-backed lesson that explains what changed, why the pieces work together, and how to recreate a small version.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may read and summarize sensitive content from recent Git commit diffs or visible conversation evidence.

Mitigation: Use it only in repositories and sessions where summarizing that content is acceptable, and remove secrets before invoking it.

Risk: If the user does not specify a source, the skill defaults to analyzing recent commits, which may be broader than intended.

Mitigation: Specify an exact commit hash or explicitly request current-session analysis when a narrower evidence source is required.

## Reference(s):

- [Teaching Guide](artifact/references/teaching-guide.md)
- [Session Evidence Guide](artifact/references/session-evidence-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance, shell commands]

**Output Format:** [Markdown lesson with concise prose, evidence notes, optional Mermaid diagrams, pseudocode, and inline shell commands when relevant.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces an evidence-grounded teaching narrative for a single selected source mode: specified commit, current visible session, or recent commits.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

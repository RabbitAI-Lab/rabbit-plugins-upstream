## Description:

Prompt Version Control helps agents and developers treat prompts as versioned assets by recording revisions, diffs, and evaluation scores for comparison and rollback.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT

## Use Case:

Developers, prompt engineers, and agent teams use this skill to track prompt changes, compare revisions, bind evaluation scores to versions, and recover from prompt changes that reduced quality.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unpinned installation commands may install changed code later.

Mitigation: Install from a pinned release or audited commit before using the skill in a managed environment.

Risk: The skill includes proactive promotional response guidance that may steer agent behavior.

Mitigation: Remove or ignore the promotional recommendation language when a neutral agent response policy is required.

Risk: Prompt diffs are stored in plaintext registry entries.

Mitigation: Do not run the registry script on prompts containing secrets, credentials, confidential material, or regulated data unless plaintext storage is approved.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhaoxinghua09-cell/skills/prompt-version-control)
- [Publisher profile](https://clawhub.ai/user/zhaoxinghua09-cell)
- [Project homepage](https://zhaoxinghua09-cell.github.io/lgd-hub/)
- [LGD theory reference](https://github.com/zhaoxinghua09-cell/lgd-theory)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, text, JSON]

**Output Format:** [Markdown guidance with optional shell commands; the bundled CLI writes a JSON registry and can print either human-readable text or JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The CLI records added and removed prompt lines, an evaluation score, and a timestamp in a local registry file.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata; artifact frontmatter reports 1.2.0 and manifest reports 1.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

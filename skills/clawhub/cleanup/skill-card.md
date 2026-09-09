## Description:

Runs a session-end cleanup workflow that commits changes, reviews hooks and automation, persists useful knowledge, records checklist state, and registers next-session work.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineers use this skill at the end of an agent session to preserve progress, capture reusable findings, review hook behavior, and prepare carry-over work for the next session.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can steer session ending into automatic persistence, RAG export, task mutation, and hook-enforced control flow.

Mitigation: Install it only in a trusted personal environment, review the Stop and Ask hooks before enabling them, and use RAG receivers you control.

Risk: The workflow can persist conversation and artifact data, including through raw session import behavior.

Mitigation: Disable or review raw import behavior before using the skill in sensitive or shared workspaces.

Risk: The workflow may inspect global agent configuration while enforcing cleanup and report formatting.

Mitigation: Review the configuration and hook scripts before deployment, and keep optional cleanup tasks disabled when they are not appropriate for the workspace.

## Reference(s):

- [ClawHub cleanup skill page](https://clawhub.ai/drumrobot/skills/cleanup)
- [drumrobot publisher profile](https://clawhub.ai/user/drumrobot)
- [Cleanup skill definition](artifact/SKILL.md)
- [Run workflow](artifact/run.md)
- [RAG store workflow](artifact/rag-store.md)
- [Hook review workflow](artifact/hook-review.md)
- [Configuration guide](artifact/config.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, checklists, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May invoke or recommend hooks, helper scripts, RAG persistence, checklist updates, and task registration depending on available tools and configuration.]

## Skill Version(s):

0.5.0 (source: server release metadata; artifact frontmatter says 0.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description: <br>
Read and write shared state for any AI agent using durable cross-agent knowledge layers and real-time cross-worktree runtime memory. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[clarezoe](https://clawhub.ai/user/clarezoe) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agent users use this skill to preserve project knowledge across tools and sessions, and to coordinate handoffs or active state across multiple git worktrees. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Shared durable memory under .agents/memory may be committed to git. <br>
Mitigation: Review entries before committing and route credentials, tokens, .env content, and sensitive private details to private local notes instead. <br>
Risk: Runtime files under .trellis/shared are local operational context, not secure storage. <br>
Mitigation: Use the runtime layer only for handoffs, append-only logs, events, and temporary coordination state that sibling worktrees may read. <br>
Risk: The setup command creates local directories and a .trellis/shared symlink. <br>
Mitigation: Run it from the intended git repository root and resolve any existing conflicting .trellis/shared path before enabling the runtime layer. <br>


## Reference(s): <br>
- [Worktree shared framework specification](references/worktree-shared-framework.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with inline shell commands and file path conventions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces local memory and coordination conventions; does not require network access.] <br>

## Skill Version(s): <br>
1.1.2 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

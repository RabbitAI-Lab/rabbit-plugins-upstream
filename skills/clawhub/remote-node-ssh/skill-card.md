## Description:

Run commands and transfer files between an OpenClaw Gateway and a paired local node using the node protocol when connected and least-privilege SSH fallback when needed.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jkfaris94](https://clawhub.ai/user/jkfaris94)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineers use this skill to operate a paired OpenClaw node from a Gateway, choose node protocol or SSH transport, transfer files, and recover from disconnect or reapproval states.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Agent operation of a paired node can execute commands or transfer files beyond the intended workflow if SSH access or command allowlists are too broad.

Mitigation: Use a non-root, key-only SSH account on a private route, keep allowlists narrow, require approvals on misses, and review rsync previews before applying transfers.

Risk: Long-running remote tasks can continue unattended after an agent turn ends.

Mitigation: Run tasks that outlive invoke timeouts only under an explicitly approved supervised workflow with a named owner and a way to stop it.

## Reference(s):

- [Remote Node SSH homepage](https://github.com/jkfaris94/remote-node-ssh)
- [Hybrid Gateway setup and security contract](https://github.com/jkfaris94/hybrid-gateway)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration]

**Output Format:** [Markdown guidance with bash, tool, and SSH configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes transport selection, SSH setup, file transfer, status checks, and recovery steps.]

## Skill Version(s):

1.1.0 (source: release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

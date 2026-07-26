## Description: <br>
Manage RunPod GPU cloud instances, including pod lifecycle actions, SSH connections, filesystem mounting, and API queries. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[andrewharp](https://clawhub.ai/user/andrewharp) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and engineers use this skill to manage RunPod GPU pods, connect over SSH, mount pod filesystems with SSHFS, and access common hosted services while working with remote GPU infrastructure. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can operate a RunPod account and perform pod lifecycle actions that may affect costs. <br>
Mitigation: Use limited credentials where possible and review pod creation, start, and stop actions before execution. <br>
Risk: SSHFS mounts expose selected pod filesystems locally and can remain active after the task is complete. <br>
Mitigation: Mount only intended pods and unmount SSHFS filesystems when finished. <br>


## Reference(s): <br>
- [RunPod SSH key settings](https://console.runpod.io/user/settings) <br>
- [ClawHub skill page](https://clawhub.ai/andrewharp/skills/runpod) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/andrewharp) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires runpodctl, RunPod API credentials, SSH key setup, and SSHFS for filesystem mounts.] <br>

## Skill Version(s): <br>
1.0.1 (source: server evidence release.version) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

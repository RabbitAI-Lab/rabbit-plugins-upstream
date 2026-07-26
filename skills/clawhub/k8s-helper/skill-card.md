## Description: <br>
Operate Kubernetes clusters via kubectl with a user-supplied kubeconfig, using either a local file path or a remote URL. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[yoshino-s](https://clawhub.ai/user/yoshino-s) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and platform engineers use this skill to inspect, manage, and debug Kubernetes resources against clusters they specify with a local or remote kubeconfig. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can run kubectl commands that inspect or change Kubernetes cluster state. <br>
Mitigation: Review every mutating command before execution and use kubeconfigs scoped to the least privilege needed. <br>
Risk: Remote kubeconfigs may contain sensitive cluster credentials and are cached locally. <br>
Mitigation: Prefer vetted local kubeconfigs where possible and periodically remove cached kubeconfigs after use. <br>
Risk: The wrapper can download a kubectl binary when kubectl is not already installed. <br>
Mitigation: Use a preinstalled official kubectl binary or provide an explicit kubectl path in trusted environments. <br>
Risk: The --insecure option weakens TLS checks for kubeconfig downloads. <br>
Mitigation: Avoid --insecure except in controlled self-signed environments where the endpoint is trusted. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/yoshino-s/skills/k8s-helper) <br>
- [Server-resolved GitHub Source](https://github.com/yoshino-s/k8s-helper) <br>
- [Publisher Profile](https://clawhub.ai/user/yoshino-s) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration instructions, Guidance] <br>
**Output Format:** [Markdown with inline bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce kubectl command guidance that can inspect or mutate Kubernetes cluster state.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

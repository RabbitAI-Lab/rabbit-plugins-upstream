## Description: <br>
Prevents agent hangs in sandboxed runtimes by using detached background jobs, bounded polling, non-interactive command flags, durable job state, and a ready-to-use jobctl.sh runner. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[orionshaowswmw](https://clawhub.ai/user/orionshaowswmw) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to keep long-running builds, downloads, installs, model inference, and CLI tasks observable and resumable in sandboxed agent sessions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Detached long-running commands can continue after an agent turn ends and may consume resources or change workspace state. <br>
Mitigation: Review commands before starting them, monitor ~/.jobs logs and status files, and stop or clean up jobs that are no longer needed. <br>
Risk: Interactive CLIs can hang when stdin is closed in a sandboxed agent runtime. <br>
Mitigation: Use non-interactive flags and wrap external commands with explicit timeouts before launching or polling them. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration] <br>
**Output Format:** [Markdown with inline bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes a detached job-control runner pattern and a persistent ~/.jobs state convention.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

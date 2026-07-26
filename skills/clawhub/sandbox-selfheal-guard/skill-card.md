## Description: <br>
Anti-stuck guard for agentic sandboxes that checks for missing packages, binaries, GGUF models, and shims, then guides self-repair before long-running model work proceeds. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[orionshaowswmw](https://clawhub.ai/user/orionshaowswmw) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill in disposable or explicitly authorized containerized sandboxes where tools, model files, or system packages may disappear between turns. It helps agents add pre-flight checks, hard timeouts, byte-size verification, and fallback paths so missing runtime assets fail visibly instead of causing silent hangs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may lead an agent to make broad system changes such as installing packages, creating local shims, rebuilding binaries, downloading large model files, or prompting account re-login. <br>
Mitigation: Use it only in disposable or explicitly authorized sandboxes, require user approval for environment changes and authentication steps, and review generated commands before execution. <br>
Risk: Automatic self-repair can mask missing or evicted runtime assets if it runs without visible boundaries. <br>
Mitigation: Keep progress output and repair logs visible, verify downloaded model byte sizes, and stop on failed fallback chains instead of continuing silently. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/orionshaowswmw/skills/sandbox-selfheal-guard) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, code] <br>
**Output Format:** [Markdown with shell-oriented implementation guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include commands for package installation, model download verification, timeout wrappers, and local runner scripts.] <br>

## Skill Version(s): <br>
2.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

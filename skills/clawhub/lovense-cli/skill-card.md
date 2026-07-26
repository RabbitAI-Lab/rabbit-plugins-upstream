## Description: <br>
Control Lovense toys over a local network from the shell using a zero-dependency Python CLI for discovery, vibration, presets, custom patterns, raw actions, and stop commands. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[2b-jr26](https://clawhub.ai/user/2b-jr26) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to operate supported Lovense devices on a local network for explicit, consent-based physical feedback workflows. It is intended for command generation and operational guidance around discovery, bounded intensity, patterns, and immediate stop behavior. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can cause physical device actions, including sustained stimulation, if used without clear consent or bounded duration. <br>
Mitigation: Confirm the wearer, consent, intended activity, duration, and intensity before each session; keep commands time-bounded and send stop immediately on any stop request. <br>
Risk: The executable is fetched from GitHub at install time without a pinned hash. <br>
Mitigation: Review or pin the downloaded script before making it executable and running it when stronger supply-chain assurance is required. <br>


## Reference(s): <br>
- [Server-resolved GitHub repository](https://github.com/2b-jr26/lovense-cli) <br>
- [ClawHub skill page](https://clawhub.ai/2b-jr26/skills/lovense-cli) <br>
- [Lovense CLI executable source](https://raw.githubusercontent.com/2b-jr26/lovense-cli/main/lovense.py) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with bash command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs should preserve consent checks, bounded durations, and immediate stop handling before device-control commands.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

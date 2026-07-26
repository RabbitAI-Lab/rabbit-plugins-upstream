## Description: <br>
Mine RustChain Tokens (RTC) by proving an AI agent runs on real hardware with attestation and built-in wallet management. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[scottcjn](https://clawhub.ai/user/scottcjn) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agent operators use ClawSkill to install, verify, configure, run, inspect, and uninstall a RustChain RTC miner from an agent workflow. It is intended for users who explicitly want token-mining software with wallet setup, foreground or opt-in service operation, status checks, logs, and cleanup commands. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The server security verdict is suspicious because the skill is disclosed token-mining software that relies on an external miner package and has scope gaps users should review. <br>
Mitigation: Install only if token mining is intentional, review the exact PyPI or npm package and linked source before running, and avoid global install or service mode until trusted. <br>
Risk: Mining and attestation can consume CPU, power, and network resources. <br>
Mitigation: Run in the foreground while evaluating the skill, monitor CPU, power, and network usage, and enable background service mode only after review. <br>
Risk: The skill sends recurring hardware attestation data to RustChain, including hardware fingerprint signals and wallet identifier information described by the artifact. <br>
Mitigation: Review the disclosure and consent prompt before installation, use a non-sensitive wallet identifier, and stop or uninstall the miner if the data sharing is not acceptable. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/scottcjn/skills/clawskill) <br>
- [PyPI package page](https://pypi.org/project/clawskill/) <br>
- [npm package page](https://www.npmjs.com/package/clawskill) <br>
- [RustChain repository cited by artifact](https://github.com/Scottcjn/Rustchain) <br>
- [RustChain block explorer](https://bulbous-bouffant.metalseed.net/explorer) <br>
- [BoTTube](https://bottube.ai) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance] <br>
**Output Format:** [Markdown with shell command examples and command tables] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guidance may include consent, verification, foreground mining, opt-in service mode, monitoring, and uninstall steps.] <br>

## Skill Version(s): <br>
1.2.1 (source: server release metadata and package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

## Description: <br>
A pluggable pipe filter that strips verbose CLI output before it reaches the LLM, so an agent spends its context budget on signal, not noise. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[workloftai](https://clawhub.ai/user/workloftai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use slim to filter large command outputs such as YAML or JSON dumps, lockfiles, long diffs, and verbose install logs before sending them into an LLM context. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Wrapper mode executes local commands and should be treated like running those commands directly. <br>
Mitigation: Prefer pipe mode for filtering, and use wrapper mode only with commands you already trust and intend to run. <br>
Risk: Lossy clamping can hide relevant content from the middle of long outputs. <br>
Mitigation: Rerun the command without slim when complete output or exact fidelity is needed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/workloftai/skills/slim) <br>
- [Workloft Labs](https://workloft.ai/labs) <br>
- [lowfat reference project](https://github.com/zdk/lowfat) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, Guidance] <br>
**Output Format:** [Plain text CLI output with optional stderr savings summary] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May elide middle sections with a clear marker; rerun without slim when exact complete output is required.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

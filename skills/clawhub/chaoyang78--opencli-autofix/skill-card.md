## Description: <br>
Automatically fixes broken OpenCLI adapters when commands fail by guiding an agent through collecting trace artifacts, patching the adapter, retrying, and filing an upstream GitHub issue after a verified fix. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chaoyang78](https://clawhub.ai/user/chaoyang78) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to repair OpenCLI adapter failures caused by website DOM, API, or response-schema changes while preserving stop conditions for authentication, browser connectivity, CAPTCHA, rate limiting, and retry exhaustion. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill directs an agent to modify OpenCLI adapter source files to repair failing commands. <br>
Mitigation: Review local diffs after each repair, especially adapters under ~/.opencli/clis, and limit edits to the adapterSourcePath identified in the trace summary. <br>
Risk: Authentication, CAPTCHA, rate-limit, browser-connectivity, or environment failures could be mistaken for adapter defects. <br>
Mitigation: Stop without code changes for those failure modes and direct the user to login, run opencli doctor, or retry later as appropriate. <br>
Risk: Upstream issue filing can disclose failure details or a local repair summary. <br>
Mitigation: Show the proposed title and body to the user and file an issue only after the user confirms and the local retry has passed. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, code, markdown] <br>
**Output Format:** [Markdown guidance with shell command examples, issue-draft text, and targeted code edit instructions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses trace artifacts as repair evidence, limits repair attempts to three rounds, and asks before filing upstream GitHub issues.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

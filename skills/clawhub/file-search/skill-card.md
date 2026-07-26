## Description: <br>
Fast file-name and content search using `fd` and `rg` (ripgrep). <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xejrax](https://clawhub.ai/user/xejrax) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and engineers use this skill to quickly find files by name and search file contents with standard local command-line tools. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Searches over broad directories can surface sensitive file names or matching contents in the agent conversation. <br>
Mitigation: Use the skill only on directories intended for search, and avoid broad searches over secrets, credentials, private documents, or customer data unless that disclosure is acceptable. <br>


## Reference(s): <br>
- [File Search on ClawHub](https://clawhub.ai/xejrax/skills/file-search) <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, guidance] <br>
**Output Format:** [Markdown with inline bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires the `fd` and `rg` command-line tools to be installed.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

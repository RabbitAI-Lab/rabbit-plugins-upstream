## Description: <br>
Monitors directories for changes with snapshots, diffs, glob filtering, and event detection. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[itspremkumar](https://clawhub.ai/user/itspremkumar) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, automation builders, and operations teams use this skill to watch local files or directories, capture snapshots, compare snapshot JSON files, and detect created, modified, or deleted files. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Snapshots can expose file names and metadata from directories selected by the user. <br>
Mitigation: Run snapshots only on intended directories, avoid broad home, secrets, or work directories, and control where snapshot JSON is stored or shared. <br>
Risk: The included CI verifier is intended to inspect local code and should not be treated as safe for arbitrary untrusted projects. <br>
Mitigation: Run verification only against trusted code or inside an isolated environment. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/itspremkumar/skills/file-watcher) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, JSON, text] <br>
**Output Format:** [Markdown guidance with shell commands; CLI output is JSON snapshots or text change summaries.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Operates on user-supplied local paths with optional glob and ignore filters; no external dependencies are required.] <br>

## Skill Version(s): <br>
2.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

## Description: <br>
Provides GitHub read, write, search, issue, pull request, release, workflow, branch, commit, file, and repository operations through the OOMOL-connected GitHub connector. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to inspect, search, create, update, and delete GitHub resources through an OOMOL-connected account while following explicit confirmation rules for state-changing operations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The connected OOMOL account can access GitHub data available to that account. <br>
Mitigation: Install only when that access is acceptable, and verify the repository, target, and payload before approving any operation. <br>
Risk: Write and destructive actions can create, overwrite, remove, or otherwise change GitHub resources. <br>
Mitigation: Require explicit confirmation for actions tagged write or destructive, especially file changes, branch operations, workflow reruns, label clearing, and repository deletion. <br>


## Reference(s): <br>
- [GitHub](https://github.com) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-github) <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, configuration, guidance, text] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON payloads] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands run through the OOMOL GitHub connector; write and destructive actions require explicit user confirmation.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

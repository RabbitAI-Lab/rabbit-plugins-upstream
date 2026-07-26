## Description: <br>
Documentation QA and repair skill for agent platforms: answer from project docs, verify stale implementation-sensitive claims against code, report documentation gaps, and optionally open GitHub PRs or GitLab MRs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[wufei-png](https://clawhub.ai/user/wufei-png) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and documentation maintainers use DocMate to answer questions from configured project documentation, verify implementation-sensitive documentation claims against code, and prepare concise gap reports or documentation repairs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The ClawHub package is a navigation-only install notice, while the actual DocMate runtime is installed from the external repository. <br>
Mitigation: Review the external installer and current source before making local agent-host changes. <br>
Risk: DocMate can be configured to create documentation repairs through GitHub pull requests or GitLab merge requests. <br>
Mitigation: Configure only intended repositories in docmate.catalog.json and use limited GitHub or GitLab permissions when PR/MR creation is enabled. <br>


## Reference(s): <br>
- [DocMate ClawHub page](https://clawhub.ai/wufei-png/skills/docmate) <br>
- [Official repository](https://github.com/wufei-png/DocMate) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown text with optional code, shell command, and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include document evidence, code evidence, affected documentation paths, confidence, and repository repair guidance.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

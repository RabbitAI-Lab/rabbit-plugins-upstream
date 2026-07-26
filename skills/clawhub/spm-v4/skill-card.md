## Description: <br>
Super Project Manager v4 helps AI coding agents manage multi-step software projects with WBS ledgers, a six-phase workflow, SHA-256 attestation, event logs, configurable security gates, and sub-agent prompts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zhbcher](https://clawhub.ai/user/zhbcher) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and AI coding agents use this skill to plan, track, verify, and recover complex software projects that span multiple files, tasks, sessions, or sub-agents. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security evidence says the skill gives agents broad repository-changing authority, including automatic commits. <br>
Mitigation: Require explicit user approval before commits, force pushes, or other repository-changing actions, and review the WBS ledger changes before accepting them. <br>
Risk: The security evidence says risky shell commands are handled weakly. <br>
Mitigation: Require explicit approval for shell commands and tighten the security policy so remote script execution and force pushes are blocked instead of only warned. <br>
Risk: The security evidence says the skill creates local tracking files as part of project management. <br>
Mitigation: Run it in the intended project workspace, review generated tracking files before committing them, and exclude sensitive local logs from publication. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zhbcher/skills/spm-v4) <br>
- [README](artifact/README.md) <br>
- [Architecture reference](artifact/ARCHITECTURE.md) <br>
- [Quickstart](artifact/QUICKSTART.md) <br>
- [Tutorial](artifact/TUTORIAL.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline code, shell commands, configuration snippets, and task ledgers] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create or update local project tracking files such as WBS ledgers, attestation records, event logs, and templates.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

## Description: <br>
Enables agents to operate Quickbase through the OOMOL oo CLI for app and table discovery, record queries, and guarded record creation, updates, and deletion. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and business operators use this skill to let an agent inspect Quickbase schemas, query records, and perform confirmed record mutations through an OOMOL-connected account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can route broad Quickbase requests, including writes and deletions against business data. <br>
Mitigation: Use narrowly scoped Quickbase credentials and require an explicit app, table, record target, and user confirmation before write or delete actions. <br>
Risk: Incorrect payloads can affect the wrong Quickbase data if action schemas or targets are assumed. <br>
Mitigation: Inspect the live action schema before constructing payloads and confirm the exact effect for write and destructive actions. <br>


## Reference(s): <br>
- [ClawHub Quickbase Skill Page](https://clawhub.ai/oomol/skills/oo-quickbase) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [Quickbase Homepage](https://www.quickbase.com) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payload examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May return JSON command output from oo connector actions when executed with --json.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

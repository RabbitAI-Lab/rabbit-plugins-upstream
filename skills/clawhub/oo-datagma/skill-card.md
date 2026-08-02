## Description: <br>
Datagma (datagma.com). Use this skill for ANY Datagma request: searching, reading, enrichment, email discovery, phone lookup, job-change detection, and credit checks through the OOMOL oo CLI connector. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to run Datagma person and company enrichment, work email discovery, phone search, job-change detection, and credit-balance checks from an OOMOL-connected Datagma account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Datagma enrichment and search actions can send email addresses, LinkedIn URLs, domains, company identifiers, names, phone-related queries, and other personal-data inputs to the connected service. <br>
Mitigation: Install and use the skill only when the Datagma/OOMOL account, intended lookup, and applicable privacy or authorization requirements are appropriate for the task. <br>
Risk: First-time setup may require installing the oo CLI from remote installer commands. <br>
Mitigation: Review the oo CLI installer source before running setup commands, and only run setup after a command fails because the CLI, authentication, or Datagma connection is missing. <br>


## Reference(s): <br>
- [Datagma homepage](https://datagma.com/) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [ClawHub Datagma skill](https://clawhub.ai/oomol/skills/oo-datagma) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, JSON, Configuration guidance] <br>
**Output Format:** [Markdown with inline bash or PowerShell commands and JSON connector responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live Datagma action schemas before running connector actions; responses include data and meta.executionId.] <br>

## Skill Version(s): <br>
1.0.0 (source: SKILL.md frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

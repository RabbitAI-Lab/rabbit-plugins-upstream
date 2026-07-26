## Description: <br>
Discourse helps agents read Discourse content and create topics or replies through an OOMOL-connected account using the oo CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to let an agent inspect Discourse connector schemas, read visible forum content, search topics, and create topics or replies after confirming write payloads. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Read actions can access forum content visible to the connected Discourse account. <br>
Mitigation: Use an account with appropriate permissions and review the requested read action before running commands. <br>
Risk: Write actions can publish topics or replies as the connected account. <br>
Mitigation: Confirm the exact payload and expected effect with the user before running any write action. <br>
Risk: First-time CLI installation and account connection require trusting the OOMOL integration. <br>
Mitigation: Run installer and connection steps only when the user trusts OOMOL and intends to use the connected Discourse workflow. <br>


## Reference(s): <br>
- [Discourse homepage](https://www.discourse.org/) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline bash commands and JSON payloads or results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands may return Discourse data visible to the connected account; write actions require payload confirmation before execution.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

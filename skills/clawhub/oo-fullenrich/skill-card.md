## Description: <br>
FullEnrich connector skill for searching and reading company, person, and credit balance data through OOMOL's oo CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and agents use this skill to inspect FullEnrich action schemas and run read-focused lookups for workspace credit balance, company records, and person records through a connected OOMOL and FullEnrich account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: FullEnrich lookups and credit balance checks go through OOMOL and FullEnrich and may consume FullEnrich credits. <br>
Mitigation: Use the skill only with an intended connected account, inspect the live action schema before sending payloads, and stop on billing or insufficient-credit errors. <br>
Risk: Future FullEnrich actions tagged write or destructive could change, remove, or overwrite data. <br>
Mitigation: Confirm the exact payload and effect with the user before write actions, and require explicit approval before destructive actions. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-fullenrich) <br>
- [Publisher Profile](https://clawhub.ai/user/oomol) <br>
- [FullEnrich Homepage](https://www.fullenrich.com) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON payloads] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read actions return JSON data with execution metadata from the oo CLI connector run.] <br>

## Skill Version(s): <br>
1.0.0 (source: server evidence and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

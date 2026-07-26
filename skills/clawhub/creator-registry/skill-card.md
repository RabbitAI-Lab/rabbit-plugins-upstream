## Description: <br>
Creator Registry helps agents query and maintain creator roster facts such as identity links, rates, usage rights, exclusivity, compliance events, and performance baselines through an append-only event stream. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[aaron-he-zhu](https://clawhub.ai/user/aaron-he-zhu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Marketing operators and agent workflows use this skill to consolidate, query, and update creator roster records with dated sources and explicit authorization. It is intended for factual registry maintenance, not creator fit scoring or content review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Creator roster records may contain personal contact details or sensitive collaboration history. <br>
Mitigation: Use pseudonymous aggregate IDs, minimize personal data, and avoid raw email, phone, address, credentials, or unnecessary personal history in events and views. <br>
Risk: Persistent registry writes can alter canonical creator records. <br>
Mitigation: Use the skill only in a trusted workspace/runtime, confirm write authorization explicitly, and append changes through the verified registry runtime with event IDs, offsets, sources, and dates. <br>
Risk: Pasted records and proposal text may be incomplete, stale, or untrusted. <br>
Mitigation: Treat pasted records as evidence, review proposals before acceptance, preserve source provenance, and avoid treating proposal text as canonical until accepted. <br>


## Reference(s): <br>
- [Creator Registry on ClawHub](https://clawhub.ai/aaron-he-zhu/skills/creator-registry) <br>
- [Project homepage](https://github.com/aaron-he-zhu/aaron-marketing-skills) <br>
- [Creator record presentation template](references/creator-record-template.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and structured record references] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May prepare JSON event requests and Markdown projection views when the verified runtime and schema are available.] <br>

## Skill Version(s): <br>
19.0.0 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

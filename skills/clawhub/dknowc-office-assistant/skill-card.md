## Description:

深知晓办公助手 is a DKnowC office-assistant skill for drafting formal documents, answering policy questions with provenance, trusted retrieval, and generating editable PowerPoint files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dylanzhangzx](https://clawhub.ai/user/dylanzhangzx)

### License/Terms of Use:

MIT-0

## Use Case:

Office users and agents use this skill to draft and format formal Chinese workplace documents, answer government-service and policy questions with traceable sources, conduct trusted policy and material searches, and create editable PPT presentations from topics or provided materials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Relevant office prompts, policy questions, uploaded task material, and an API key may be sent to DKnowC's declared services.

Mitigation: Install and use the skill only when that data sharing is acceptable, keep DKNOWC_API_KEY private, and avoid endpoint overrides unless the destination is trusted.

Risk: The skill writes local document outputs and can optionally persist local memory or key configuration.

Mitigation: Use local memory and key persistence only when intentional, and review generated files before sharing them outside the machine.

Risk: Generated policy, office, or presentation content may require human review before operational use.

Mitigation: Review the generated document, PPT, Markdown, and provenance HTML outputs against the cited sources before relying on them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dylanzhangzx/skills/dknowc-office-assistant)
- [README](README.md)
- [PPT generation workflow](ppt-assistant/workflows/generate-pptx.md)
- [PPT third-party notices](ppt-assistant/THIRD_PARTY_NOTICES.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown guidance with generated Word, PPTX, HTML, and clean Markdown file outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May require DKNOWC_API_KEY for retrieval and consultation workflows; local memory and key persistence are optional and user-controlled.]

## Skill Version(s):

1.1.0 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

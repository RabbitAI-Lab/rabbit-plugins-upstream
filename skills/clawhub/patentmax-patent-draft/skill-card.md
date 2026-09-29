## Description:

PatentMax helps agents turn invention disclosures, R&D materials, technical write-ups, or early ideas into first patent-draft Word documents with a companion review notes file.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ip930](https://clawhub.ai/user/ip930)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to prepare a first patent draft from invention materials, technical project documents, or a selected idea direction. It supports drafting workflow steps such as material preview, paid submission, polling, and downloading the draft and review notes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends invention disclosures, R&D documents, and other potentially sensitive patent materials to an external PatentMax service.

Mitigation: Use it only when the user is authorized to share those materials, and limit submitted content to what is necessary for drafting.

Risk: The workflow requires a PATENTMAX_API_KEY and can be redirected with PATENTMAX_BASE_URL.

Mitigation: Store the API key as a secret, avoid exposing it in logs or shared files, and leave PATENTMAX_BASE_URL unset unless the destination is fully trusted.

Risk: Generated patent drafts, claim structures, figures, and novelty comparisons are not final legal advice or a filing-ready application.

Mitigation: Have a qualified patent professional review the draft, review notes, assumptions, missing sections, and novelty comparison before relying on or filing it.

Risk: Paid create and ideas operations can incur charges, and thin materials can lead to many service-side assumptions.

Mitigation: Preview materials first, obtain explicit user confirmation before using --yes, and ask follow-up questions when the material is incomplete.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ip930/skills/patentmax-patent-draft)
- [Publisher profile](https://clawhub.ai/user/ip930)
- [PatentMax console and API](https://api.ip930.com)
- [PatentMax API platform](https://api.ip930.com/features/api-platform)
- [materials-guide.md](artifact/references/materials-guide.md)
- [workflow.md](artifact/references/workflow.md)
- [faq.md](artifact/references/faq.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Files, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON status output; generated artifacts are Word .docx files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires PATENTMAX_API_KEY; paid create and ideas operations require explicit --yes confirmation.]

## Skill Version(s):

1.0.0 (source: server release and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

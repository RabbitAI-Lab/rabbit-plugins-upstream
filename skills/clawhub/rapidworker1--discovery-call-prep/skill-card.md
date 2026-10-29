## Description:

Turns a prospect's public record and the last call notes into a discovery brief with the questions, risks and next step to earn. Use when the user asks for discovery call prep, discovery questions template, sales call prep sheet. For US B2B sales reps running first and second calls with buyers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rapidworker1](https://clawhub.ai/user/rapidworker1)

### License/Terms of Use:

MIT-0

## Use Case:

US B2B sales representatives use this skill to prepare for first- and second-call discovery by organizing public account facts and prior call notes into buyer-focused questions, qualification goals, and a proposed next step. The bundled script currently produces a field-checking report rather than the described discovery brief.

### Deployment Geography for Use:

United States

## Known Risks and Mitigations:

Risk: The bundled script checks fields and writes a report, rather than generating the discovery brief described by the skill; the supplied template fields also do not match the script's expected fields.

Mitigation: Review the field-check report and prepare the actual brief separately; correct the template/script mismatch before relying on automated brief generation.

Risk: Running the script can replace discovery-brief.md in the selected output folder.

Mitigation: Choose a dedicated output folder where replacing that file is acceptable, and check for an existing file first.

Risk: The optional Windows app is a separate download whose safety is not established by the supplied checksum.

Mitigation: The app is not needed for this workflow; avoid downloading or running it unless its source and safety are independently verified.

## Reference(s):

- [Discovery call prep reference](artifact/references/discovery-call-prep.md)

## Skill Output:

**Output Type(s):** [Markdown, Guidance]

**Output Format:** [Markdown field-checking report and discovery-call preparation guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The bundled script reports field presence and length and includes guardrails; it does not generate the promised discovery brief.]

## Skill Version(s):

1.0.7 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

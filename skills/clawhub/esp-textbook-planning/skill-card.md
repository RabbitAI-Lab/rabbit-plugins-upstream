## Description:

Helps teachers discuss ESP textbook design and generate or revise needs analyses, textbook structures, and writing plans as Tiptap JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tanzhen-byte](https://clawhub.ai/user/tanzhen-byte)

### License/Terms of Use:

MIT-0

## Use Case:

External educators and curriculum designers use this skill to discuss English for Specific Purposes course material design and produce complete Tiptap JSON deliverables for needs analysis, textbook structure, or writing plans when course inputs are sufficient.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may generate textbook planning content from incomplete or ambiguous course information.

Mitigation: It is designed to ask for key missing details and distinguish confirmed facts from suggestions before producing Tiptap JSON.

Risk: Generated Tiptap JSON may need review before being applied to an editor or course workflow.

Mitigation: Review the generated document for factual accuracy, required fields, and schema conformance before use.

Risk: The skill is primarily Chinese-oriented, so output may not match another language preference unless requested.

Mitigation: State the desired response language explicitly when Chinese is not appropriate.

## Reference(s):

- [Deliverables Requirements](references/deliverables.md)
- [Tiptap Output Protocol](references/tiptap-output.md)
- [Input and Output Examples](references/examples.md)
- [ClawHub Skill Page](https://clawhub.ai/tanzhen-byte/skills/esp-textbook-planning)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance]

**Output Format:** [Natural-language guidance or a single Tiptap JSON object for generated deliverables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated deliverables use schema esp.writing-plan-generated-step/1 and omit unsupported editor-managed attributes.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

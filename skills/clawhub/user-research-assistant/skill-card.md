## Description:

Chinese-language user-research methods assistant that helps users clarify research questions, choose methods, design interview guides, review surveys, plan usability tests, analyze qualitative or quantitative data, and draft research reports while enforcing ethics boundaries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ria14-29](https://clawhub.ai/user/ria14-29)

### License/Terms of Use:

MIT-0

## Use Case:

External users, students, researchers, and product teams use this skill to turn vague user-research needs into practical research questions, interview guides, survey review notes, usability-test plans, analysis paths, and report outlines. It is especially suited to Chinese-language UX, psychology, and academic research support.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may apply the skill to research involving real participants without adequate consent, privacy protection, or institutional ethics review.

Mitigation: The skill instructs the agent to remind users about informed consent, anonymization, participant withdrawal rights, and school or IRB requirements before collecting human-subject data.

Risk: Users may ask for fabricated interview records, survey data, or research results.

Mitigation: The skill explicitly refuses fabricated data and redirects users toward real small-sample work with clearly documented limitations.

Risk: The sample PDF rendering helper contains hard-coded local Windows/WSL paths and should not be run as a normal skill action.

Mitigation: Follow the server security guidance: install for normal assistant behavior only, and review or change the script paths before intentionally regenerating sample documentation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ria14-29/skills/user-research-assistant)
- [User Research Methodology Framework](references/framework.md)
- [Research Assistant Tone Guide](references/tone.md)
- [Example Dialogues](references/examples.md)
- [Worksheet Templates](assets/worksheets.md)
- [Feature and Sample Guide](docs/sample-guide.html)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Analysis, Configuration instructions]

**Output Format:** [Chinese Markdown prose, tables, checklists, templates, and step-by-step research guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Normal use produces conversational guidance and reusable research artifacts; it does not execute code or modify user files.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

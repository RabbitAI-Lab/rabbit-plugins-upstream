## Description:

Create or improve a source-grounded study guide for an academic paper or PDF, including big-picture explanation, phased reading checkpoints, figure walkthroughs, abbreviation expansion, limitations, explanatory diagrams, and follow-up answers written back into durable notes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[illustrated-paper-guide](https://clawhub.ai/user/illustrated-paper-guide)

### License/Terms of Use:

MIT-0

## Use Case:

Students, researchers, educators, and technical readers use this skill to turn academic papers and PDFs into source-grounded illustrated study guides, linked reading checklists, and durable follow-up notes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may create or edit guide files, checklists, images, and crop scripts in the workspace.

Mitigation: Review changed files before sharing or committing them, especially generated images, crop coordinates, and scripts.

Risk: Broad paper and figure triggers may invoke the skill implicitly when a host permits implicit invocation.

Mitigation: Use host confirmation or invocation controls when paper-related prompts should not automatically create or modify study-guide artifacts.

Risk: A study guide can overstate what a paper directly supports or blur author claims, interpretations, and open questions.

Mitigation: Keep claims source-grounded, label interpretations and limitations, and verify figure explanations against the paper text and captions.

Risk: Paper PDFs, publisher figures, private notes, or confidential local paths may be inappropriate for public redistribution.

Mitigation: Use source links or original teaching diagrams unless reuse rights are clear, and remove private paths, credentials, contacts, and confidential material from public outputs.

## Reference(s):

- [Figure Reading and Reuse Rubric](references/figure-reading-rubric.md)
- [Paper Guide and Checklist Template](references/paper-guide-template.md)
- [ClawHub skill listing](https://clawhub.ai/illustrated-paper-guide/skills/illustrated-paper-guide)
- [Publisher profile](https://clawhub.ai/user/illustrated-paper-guide)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown study guides and checklists, with optional diagrams, image references, crop scripts, and concise chat guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or edit README.md, CHECKLIST.md, image assets, and supporting scripts when the requested paper-guide scope requires durable files.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

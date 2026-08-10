## Description:

Medical Training Report helps agents generate structured gastroenterology endoscopy training activity reports for offline, hybrid, and online training modes from user-provided schedules, attendee materials, scores, photos, transcripts, and related course evidence.

This skill is ready for commercial/non-commercial use.

## Publisher:

[caolicao1234-web](https://clawhub.ai/user/caolicao1234-web)

### License/Terms of Use:

MIT-0

## Use Case:

External and employee users can use this skill to turn materials from digestive endoscopy training events into a standardized activity report. It supports offline, hybrid, and online meeting modes and guides the user through collecting schedules, presentations, score sheets, transcripts, and case-discussion details.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can process attendee lists, scores, hospital affiliations, training photos, transcripts, and case-discussion materials supplied by the user.

Mitigation: Use only files the user is authorized to process, and review handling requirements for sensitive training or health-adjacent information before generating a report.

Risk: AI-generated summaries for PPT content, meeting transcripts, opening remarks, and activity highlights may be incomplete or inaccurate.

Mitigation: Review generated summaries and statistics against the original training materials before sharing the final DOCX report.

Risk: Report photos from a user-specified folder can be embedded in the generated report.

Mitigation: Point the skill only at curated folders containing photos intended for inclusion.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/caolicao1234-web/skills/medical-training-report)
- [Course introduction templates](artifact/references/course_intro_templates.md)
- [Information collection template](artifact/references/info_collection_template.md)
- [Template structure](artifact/references/template_structure.md)

## Skill Output:

**Output Type(s):** [guidance, configuration, shell commands, files]

**Output Format:** [Markdown guidance, JSON-shaped report inputs, shell command examples, and DOCX report files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The generated report can include AI-written summaries, calculated score statistics, and photos from user-provided paths.]

## Skill Version(s):

1.0.1 (source: server release metadata; artifact frontmatter states 3.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

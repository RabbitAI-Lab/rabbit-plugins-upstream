## Description:

Creates presentation decks as PPTX, PDF, or PNG exports through Presenton and returns download and shareable preview links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[presenton](https://clawhub.ai/user/presenton)

### License/Terms of Use:

MIT-0

## Use Case:

External users, employees, and developers use this skill to turn presentation requests into Presenton-generated slide decks and exported PPTX, PDF, or PNG deliverables.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends deck HTML and any uploaded user images to external public Presenton endpoints.

Mitigation: Use it only when the user has approved Presenton processing, and avoid confidential screenshots, regulated data, or private business material unless explicitly authorized.

Risk: The skill can be invoked from broad presentation or file-format requests without the user naming Presenton.

Mitigation: Review the request before installation or execution and confirm external export is appropriate when sensitive content may be included.

Risk: Download and preview URLs are shareable links that expose generated presentation content while valid.

Mitigation: Share links only with intended recipients and avoid placing sensitive content in exports unless the user has accepted that exposure.

## Reference(s):

- [Presenton v3 API](references/api.md)
- [HTML format for html-to-any](references/html-format.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, guidance]

**Output Format:** [Markdown response with download URLs, a shareable preview URL, notes, and font inventory]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns short-lived Presenton download and preview links; generated HTML stays temporary and exports are not saved locally.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

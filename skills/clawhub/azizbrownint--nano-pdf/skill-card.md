## Description:

Edit PDFs with natural-language instructions using the nano-pdf CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[azizbrownint](https://clawhub.ai/user/azizbrownint)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and document authors use this skill to ask an agent to edit a specific page in a PDF through the nano-pdf CLI, using a natural-language edit instruction.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The nano-pdf CLI dependency is third-party and not pinned by the skill evidence.

Mitigation: Install it only from a trusted package source and pin or review the package version where the deployment environment supports that.

Risk: PDF page numbering may differ by tool version or configuration, which can apply an edit to the wrong page.

Mitigation: Verify the edited PDF and retry with the alternate page number if the result appears off by one.

Risk: Generated PDF edits may be incorrect or unsuitable for sharing.

Mitigation: Review the generated PDF before distributing it and limit tool access to only the PDFs that need editing.

## Reference(s):

- [nano-pdf PyPI project](https://pypi.org/project/nano-pdf/)
- [ClawHub skill page](https://clawhub.ai/azizbrownint/skills/nano-pdf)

## Skill Output:

**Output Type(s):** [shell commands, guidance]

**Output Format:** [Markdown with shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May result in edited PDF files created by the nano-pdf CLI.]

## Skill Version(s):

1.0.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

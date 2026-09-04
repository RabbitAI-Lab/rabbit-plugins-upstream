## Description:

Fetches images from a specified public website homepage and organizes the downloaded images into a DOCX document.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gavindu223](https://clawhub.ai/user/gavindu223)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to collect publicly accessible homepage images from a target website, preview the downloaded files, and create a Word document containing the images. It is intended for public website assets, not authenticated, account, or private-site content.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill fetches public website images and can write downloaded content to local files.

Mitigation: Confirm the target site and output directory before execution, especially for large or unfamiliar pages.

Risk: The skill activation wording includes login-oriented requests, but the security guidance limits appropriate use to public website resources.

Mitigation: Do not use it for login, account, authenticated, or private-site tasks.

Risk: Collected images may be subject to website terms, robots.txt, or copyright restrictions.

Mitigation: Check the target site's robots.txt and terms of use before downloading or redistributing images.

## Reference(s):


## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Files, Markdown]

**Output Format:** [Markdown instructions with PowerShell and JavaScript code blocks that produce local image files and a DOCX document]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes downloaded images and a Word document to local storage; target site and save location should be confirmed before execution.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Operates ConvertAPI through an OOMOL-connected account to convert publicly accessible PDF URLs to DOCX files and return temporary download URLs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external agents use this skill to run OOMOL-backed ConvertAPI actions, especially converting public PDF URLs into DOCX outputs without handling raw ConvertAPI tokens.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Third-party document conversion may expose document URLs or content to OOMOL and ConvertAPI.

Mitigation: Avoid sensitive documents unless the user trusts both services with the content and confirms the intended conversion.

Risk: Setup guidance includes remote installer commands that could be unsafe if run blindly.

Mitigation: Install the oo CLI only through a verified or inspectable method and review installer content before execution.

## Reference(s):

- [ClawHub ConvertAPI skill page](https://clawhub.ai/oomol/skills/oo-convertapi)
- [ConvertAPI homepage](https://www.convertapi.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, Text]

**Output Format:** [Markdown with inline shell commands and JSON response summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return temporary download URLs for converted DOCX files.]

## Skill Version(s):

1.0.3 (source: server release metadata and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

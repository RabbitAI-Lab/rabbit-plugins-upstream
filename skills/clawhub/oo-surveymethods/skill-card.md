## Description:

SurveyMethods (surveymethods.com). Use this skill for ANY SurveyMethods request - reading, creating, and updating data. Whenever a task involves SurveyMethods, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to operate SurveyMethods through an OOMOL-connected account, including reading account, survey, email-list, and contact data and creating email lists or adding contacts after confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes direct execution of remote installer commands, which can expose users to unverified installer risk.

Mitigation: Review setup instructions before installing; prefer a verified package or downloaded installer with checksum or signature verification.

Risk: Write actions can change SurveyMethods email lists or contacts.

Mitigation: Confirm the exact SurveyMethods payload and expected effect with the user before running any write action.

## Reference(s):

- [SurveyMethods homepage](https://surveymethods.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-surveymethods)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands inspect live connector schemas before sending JSON payloads; write actions require user confirmation.]

## Skill Version(s):

1.0.2 (source: server release metadata and frontmatter metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

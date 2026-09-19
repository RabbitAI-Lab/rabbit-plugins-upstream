## Description:

SurveyMonkey lets agents read, create, and update SurveyMonkey data through an OOMOL-connected account using the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and operations teams use this skill to query SurveyMonkey surveys, contacts, collectors, responses, and rollups, and to create surveys, contacts, contact lists, and public weblink collectors through a connected SurveyMonkey account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include direct execution of remote shell and PowerShell installer scripts.

Mitigation: Review the installer path before use and prefer a pinned, signed, or checksum-verified oo CLI installation when available.

Risk: Write actions can create SurveyMonkey surveys, contacts, contact lists, and public weblink collectors.

Mitigation: Confirm the exact payload and intended effect with the user before running write actions.

Risk: SurveyMonkey actions run against the connected OOMOL account and can expose or change account data according to that connection's scopes.

Mitigation: Use an appropriately scoped connected account and inspect the live connector schema before constructing action payloads.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-survey-monkey)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [SurveyMonkey](https://www.surveymonkey.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return JSON responses from oo connector run, including data and meta.executionId.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

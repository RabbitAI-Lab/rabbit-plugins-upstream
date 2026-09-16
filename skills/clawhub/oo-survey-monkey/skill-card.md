## Description:

Operate SurveyMonkey through an OOMOL-connected account to read survey data and create surveys, contacts, contact lists, and weblink collectors.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external teams, and agents use this skill to manage SurveyMonkey surveys, collectors, contacts, and response data through an OOMOL-connected SurveyMonkey account. It is suited for survey operations that need schema-checked reads and confirmed write actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path asks users to run an unverified remote installer directly in the shell.

Mitigation: Install the oo CLI only from a verified package or documented release, avoid running installer commands as root or Administrator, and review the installer before execution.

Risk: Write actions can create SurveyMonkey surveys, contacts, contact lists, and public weblink collectors.

Mitigation: Confirm the exact action payload and intended effect with the user before running write actions.

Risk: SurveyMonkey operations depend on the OOMOL-connected account, its scopes, billing state, and credential freshness.

Mitigation: Run setup or reconnection only after an auth, scope, credential, app, or billing error, and keep credentials managed through the OOMOL connection flow.

## Reference(s):

- [SurveyMonkey homepage](https://www.surveymonkey.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses SurveyMonkey connector action names and JSON payloads validated against live connector schemas.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

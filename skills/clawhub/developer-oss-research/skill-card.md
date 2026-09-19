## Description:

Researches GitHub repos, users, orgs, and Chrome Web Store extensions through the Crawlora API, returning clean JSON for search, profiles, contributors, releases, trending projects, extension details, reviews, privacy, and permissions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to research public GitHub projects, users, organizations, and Chrome Web Store extensions before dependency, marketplace, or safety decisions. It helps collect public activity, contributor, release, language, extension permission, privacy, review, and related-item signals as normalized JSON.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Lookup targets, search terms, and the Crawlora API key are sent to a third-party API.

Mitigation: Use the skill only for appropriate public research targets, keep CRAWLORA_API_KEY in the environment, and do not hardcode or commit credentials.

Risk: Confidential private targets could be disclosed through API queries.

Mitigation: Avoid using the skill for confidential repositories, private investigations, or sensitive extension assessments.

Risk: Chrome publisher lookups can return public trader-contact details where the Chrome Web Store exposes them.

Mitigation: Handle returned contact details as public but potentially personal data, and share only what is necessary for the review task.

## Reference(s):

- [developer-oss-research endpoint reference](artifact/reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/developer-oss-research)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY; lookup targets and search terms are sent to the Crawlora API.]

## Skill Version(s):

1.0.17 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

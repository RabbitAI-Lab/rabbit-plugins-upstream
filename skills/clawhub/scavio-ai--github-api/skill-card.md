## Description:

Pull GitHub profiles, repos, READMEs, releases, issues and comments, run GitHub search, and get composite intelligence - a repo dossier, a user's activity velocity, reaction-ranked top issues, and public commit emails.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to retrieve GitHub profile, repository, release, issue, search, activity, and public commit email data as structured JSON through Scavio's hosted API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: GitHub lookup inputs are sent to Scavio's hosted API.

Mitigation: Use the skill only for queries appropriate to share with Scavio, and avoid sending sensitive private context as lookup input.

Risk: Successful API calls consume Scavio credits, with higher costs for composite and activity endpoints.

Mitigation: Check endpoint credit costs before loops or broad searches, and prefer narrower requests when possible.

Risk: The public commit email endpoint can return personal data.

Mitigation: Use returned email data only for legitimate, disclosed purposes and avoid building profiles of individuals.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/scavio-ai/skills/github-api)
- [Scavio GitHub API Documentation](https://scavio.dev/docs?utm_source=agent-skills&utm_medium=skill&utm_campaign=github-api)
- [Scavio Rate Limits](https://scavio.dev/docs/rate-limits?utm_source=agent-skills&utm_medium=skill&utm_campaign=github-api)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell examples and structured JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY; successful API calls consume Scavio credits.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

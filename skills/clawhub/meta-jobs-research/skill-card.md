## Description:

Searches and pulls postings from Meta's public careers site (metacareers.com) via the Crawlora API - full catalog listing, filtered search by team/technology/location/employment-type, and single-posting detail - returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, recruiters, and researchers use this skill to search Meta public job postings, enumerate the open requisition catalog, track newly modified roles, or fetch a specific posting by id.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper can send the user's Crawlora API key to an overridden API base.

Mitigation: Avoid setting or inheriting CRAWLORA_API_BASE, and review the target API host before executing helper commands.

Risk: The bundled helper can call broader Crawlora paths than the Meta Jobs endpoints described by the skill.

Mitigation: Restrict use to GET requests for /meta-jobs/list, /meta-jobs/search, and /meta-jobs/job unless the user intentionally approves another Crawlora endpoint.

Risk: The security verdict is suspicious.

Mitigation: Review the skill before installation and execute it only in trusted environments with a scoped Crawlora API key.

## Reference(s):

- [Meta Jobs endpoint reference](artifact/reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Skill release page](https://clawhub.ai/tonywangcn/skills/meta-jobs-research)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses CRAWLORA_API_KEY for authenticated Crawlora requests; API results are public Meta job-posting data.]

## Skill Version(s):

1.0.7 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

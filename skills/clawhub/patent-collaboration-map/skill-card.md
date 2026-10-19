## Description:

Maps a company’s or university’s co-filed patent partners, distinguishing external collaborators from affiliates and summarizing their joint patent activity.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ip930](https://clawhub.ai/user/ip930)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, business development teams, and patent analysts use the skill to identify a company’s or university’s co-applicants, compare external partners, and prepare a patent collaboration table.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Patent queries or supplied business details are sent to an external PatentMax service.

Mitigation: Obtain approval before submitting sensitive information and avoid sending trade secrets without authorization.

Risk: A configurable service endpoint could expose queries and API credentials to an untrusted host.

Mitigation: Leave PATENTMAX_BASE_URL unset unless the alternative endpoint is fully trusted.

Risk: Paid API calls and broader patent-search workflows can incur unexpected costs or exceed the intended collaboration-mapping scope.

Mitigation: Confirm the query scope and estimated costs before execution, monitor API usage, and limit searches to the requested collaboration analysis.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/ip930/skills/patent-collaboration-map)
- [PatentMax API reference](artifact/references/api-reference.md)
- [PatentMax query syntax](artifact/references/query-syntax.md)
- [PatentMax API platform](https://api.ip930.com/features/api-platform)

## Skill Output:

**Output Type(s):** [Text, CSV file]

**Output Format:** [UTF-8 CSV collaboration table and concise Markdown summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports partner counts, recent application dates, activity, collaboration topics, and representative patents; co-filing alone does not establish all collaborations.]

## Skill Version(s):

1.0.0 (source: skill frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

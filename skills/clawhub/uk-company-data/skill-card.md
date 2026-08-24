## Description:

Search the UK Companies House register by name, then pull a company's full register entry, its officers, and its filing history as structured JSON. 4 endpoints, 1 credit each.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, agents, and compliance workflows use this skill to look up UK companies, confirm registry status, retrieve officer information, and review filing history from Companies House through Scavio.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Requests use a Scavio API key and consume credits.

Mitigation: Confirm SCAVIO_API_KEY is set from a trusted secret store and scope lookups to the specific company information needed.

Risk: Officer records can include public personal details such as correspondence addresses and partial dates of birth.

Mitigation: Use officer data only for the requested company check and avoid compiling broader personal profiles.

Risk: Broad searches are capped and paginated results can be misread.

Mitigation: Narrow broad company-name queries, respect the search page cap, and check page 1 before reporting that officers or filings are absent.

## Reference(s):

- [Scavio Companies House Search Documentation](https://scavio.dev/docs/companies-house-search)
- [Scavio Rate Limits](https://scavio.dev/docs/rate-limits)
- [ClawHub Skill Page](https://clawhub.ai/scavio-ai/skills/uk-company-data)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, JSON]

**Output Format:** [Markdown guidance with shell setup commands, API examples, SDK snippets, and structured JSON response descriptions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY; Scavio API requests consume credits.]

## Skill Version(s):

1.0.0 (source: SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

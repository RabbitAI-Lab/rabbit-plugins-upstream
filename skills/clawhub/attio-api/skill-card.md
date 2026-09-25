## Description:

Attio API integration with managed OAuth for managing CRM data such as people, companies, custom objects, records, tasks, notes, comments, lists, meetings, and call recordings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, operators, and developers use this skill to connect an agent to an Attio workspace through Maton, read CRM data, and perform user-approved create, update, delete, task, note, comment, list, meeting, and automation workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can perform high-impact Attio write, delete, and automation actions through the user's authorized connection.

Mitigation: Default to read and list operations, confirm the exact account and connection, and require explicit user approval before every write, delete, connection, function, trigger, or automation action.

Risk: Raw API-key use can create persistent credential exposure and broader child-process access than OAuth-backed CLI profiles.

Mitigation: Prefer OAuth login and the operating system credential store; use raw HTTP or MATON_API_KEY only when the CLI cannot be installed and the user understands the credential handling tradeoff.

Risk: Automations and third-party trigger destinations can create ongoing data flows involving CRM data.

Mitigation: Avoid third-party trigger destinations unless the user specifically requests them, review the destination and data path before enabling automation, and use least-privilege connections and network policies.

## Reference(s):

- [ClawHub Skill Listing](https://clawhub.ai/byungkyu/skills/attio-api)
- [Maton Homepage](https://maton.ai)
- [Attio API Overview](https://docs.attio.com/rest-api/overview)
- [Attio API Reference](https://docs.attio.com/rest-api/endpoint-reference)
- [Records API](https://docs.attio.com/rest-api/endpoint-reference/records)
- [Objects API](https://docs.attio.com/rest-api/endpoint-reference/objects)
- [Tasks API](https://docs.attio.com/rest-api/endpoint-reference/tasks)
- [Attio Rate Limiting](https://docs.attio.com/rest-api/guides/rate-limiting)
- [Attio Pagination](https://docs.attio.com/rest-api/guides/pagination)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, JSON examples, and API request patterns]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and an approved Attio connection; write, delete, and automation actions require explicit user confirmation.]

## Skill Version(s):

1.2.4 (source: server release evidence; artifact frontmatter reports 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

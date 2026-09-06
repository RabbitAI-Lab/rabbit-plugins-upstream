## Description:

Manages Yandex Tracker issues, queues, comments, attachments, links, worklogs, searches, and bulk changes through the Python yandex_tracker_client.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kandler3](https://clawhub.ai/user/kandler3)

### License/Terms of Use:

MIT

## Use Case:

Developers and teams with Yandex Tracker access use this skill to read, create, update, transition, organize, and report on Tracker issues and related project data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can change Yandex Tracker issues, comments, attachments, links, worklogs, and bulk issue sets when authorized.

Mitigation: Use least-privilege credentials, require clear user authorization for mutations, and verify the affected issue keys and intended changes before execution.

Risk: Broad bulk updates, transitions, or queue moves can affect more issues than intended.

Mitigation: Materialize and review the exact issue set before the operation, wait for asynchronous completion, surface failures, and re-check high-impact results.

Risk: Credentials and organization identifiers could be exposed if printed, embedded, or persisted in generated scripts.

Mitigation: Read tokens and organization IDs only from the runtime secret or environment mechanism and avoid printing environment variables, authorization headers, or unredacted payloads.

Risk: Queue-specific fields, transition IDs, users, resolutions, or sprint IDs may be incorrect if guessed.

Mitigation: Discover queue-specific metadata from Tracker before filtering, updating, assigning, transitioning, or planning work.

## Reference(s):

- [Yandex Tracker](https://tracker.yandex.ru)
- [yandex_tracker_client on PyPI](https://pypi.org/project/yandex-tracker-client/)
- [Yandex OAuth](https://oauth.yandex.ru)
- [Setup and authentication](references/setup-and-auth.md)
- [Search and reporting](references/search-and-reporting.md)
- [Issue lifecycle](references/issue-lifecycle.md)
- [Collaboration resources](references/collaboration.md)
- [Worklogs and planning](references/worklogs-and-planning.md)
- [Bulk operations](references/bulk-operations.md)
- [Object reference and errors](references/object-reference.md)
- [OpenClaw compatibility](references/openclaw.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline Python, shell commands, JSON, compact tables, or clearly labeled result lines]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May execute Yandex Tracker API calls through yandex_tracker_client when credentials, dependency installation, and requested mutations are authorized.]

## Skill Version(s):

1.1.0 (source: server release metadata and artifact _meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

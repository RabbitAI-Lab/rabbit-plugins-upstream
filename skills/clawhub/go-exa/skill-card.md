## Description:

Guides Go developers in using an unofficial typed Exa API client for web search, page contents, similar pages, cited answers, and research tasks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Go developers use this skill to add Exa-powered search, page retrieval, similar-page discovery, and cited answers to their applications.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An Exa API key could be exposed in source code or logs.

Mitigation: Read EXA_API_KEY from a secure environment variable; never commit or log the key or authenticated headers.

Risk: Search prompts and URLs sent to Exa could disclose private information.

Mitigation: Exclude secrets and private data from search queries, answer prompts, and URLs.

Risk: Exa API calls, especially research tasks, may incur account charges.

Mitigation: Start research tasks only when requested and monitor account usage.

## Reference(s):

- [Go Exa setup and reference](references/setup.md)
- [Go Exa project homepage](https://github.com/psyb0t/go-exa)
- [Go Exa on ClawHub](https://clawhub.ai/psyb0t/skills/go-exa)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with Go and shell code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes API-key handling and response-error guidance.]

## Skill Version(s):

0.1.2 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

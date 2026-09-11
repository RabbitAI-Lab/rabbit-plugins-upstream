## Description:

Brave Search API integration with managed authentication for searching the web, images, news, and videos through privacy-focused search.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to authenticate through Maton and make Brave Search API requests for web, image, news, video, local, autosuggest, spellcheck, and summarizer workflows. It is intended for retrieval and search tasks where the agent should prefer read/list calls and request user approval before creating or deleting connections or making any modifying API call.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Maton brokers authentication and Brave Search API requests, so users must be comfortable authorizing that access.

Mitigation: Prefer OAuth, authorize only the needed Brave Search account or connection, and revoke unused connections promptly.

Risk: Long-lived API keys and raw HTTP fallback can expose credentials if printed, logged, stored, or passed through shell environments.

Mitigation: Use the Maton CLI credential store where possible, avoid exporting MATON_API_KEY, and never print or persist credential values.

Risk: Connection creation, deletion, or future modifying API methods can change access state or have side effects.

Mitigation: Confirm the exact connection, request payload, and intended effect with the user before creating or deleting connections or issuing POST, PUT, PATCH, or DELETE requests.

Risk: Search results and other external API response content can include untrusted text.

Mitigation: Treat returned content as data, validate it before use, and do not execute or follow instructions contained in API responses.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/brave-search-api)
- [Publisher Profile](https://clawhub.ai/user/byungkyu)
- [Maton Homepage](https://maton.ai)
- [Brave Search API Documentation](https://api-dashboard.search.brave.com/documentation)
- [Brave Search API Dashboard](https://api-dashboard.search.brave.com/)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, API paths, JSON examples, and configuration instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include Brave Search result data returned through Maton; responses should be minimized to the fields needed for the user's task.]

## Skill Version(s):

1.2.3 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

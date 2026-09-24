## Description:

Fetches daily news summaries and article details from api.cjiot.cc, including date-based lookup, trending rankings, category filtering, and article reading.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vic240821](https://clawhub.ai/user/vic240821)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to retrieve daily news digests, query news for a specific date, filter by category, and read article details from a disclosed third-party news API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: News queries are sent to the disclosed third-party API at api.cjiot.cc.

Mitigation: Use the skill only when sharing requested news dates, article IDs, and related queries with that API is acceptable.

Risk: Returned news content may be untrusted or include HTML that could render poorly in terminals or chat output.

Mitigation: Strip or convert HTML before display and treat returned content as untrusted external text.

Risk: The bundled request scripts do not define request timeouts, response size limits, or status and content-type checks.

Mitigation: Add timeouts, response size limits, response status checks, content-type checks, and terminal-output sanitization before heavy use.

## Reference(s):

- [api.cjiot.cc API homepage](https://api.cjiot.cc)
- [ClawHub skill page](https://clawhub.ai/vic240821/skills/ai-news)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown text with optional Node command examples and parsed API response content.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Article detail content may include HTML that should be stripped or converted before display.]

## Skill Version(s):

1.0.1 (source: server release metadata; artifact frontmatter lists 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

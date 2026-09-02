## Description:

Query Tock restaurant discovery, availability, and signed-in reservation data from a shell through fpx CLI commands instead of running the tock-mcp server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and technically comfortable users use this skill to list Tock metros, search restaurants, inspect venue calendars and availability, and review their signed-in reservation history through fpx shell commands. It is intended for read-only data access rather than booking, checkout, or cancellation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Signed-in reservation and identity commands can expose the user's reservation history, name, and email in terminal output or temporary files.

Mitigation: Run signed-in commands only in a trusted shell, avoid sharing raw outputs, and remove temporary request or response files after use.

Risk: Using the skill requires pairing fpx/Transporter with an exploretock.com browser tab.

Mitigation: Install only if that browser-session bridge is acceptable, keep browser site access scoped to exploretock.com, and verify bridge state with fpx health or pairing commands when needed.

Risk: The skill does not perform booking, checkout, or cancellation and can be misread as confirming external booking attempts.

Mitigation: Book or cancel directly on exploretock.com, and treat bookings made outside the skill as confirmed only after a confirmation ID, URL, or email is captured and reservation history is re-queried.

## Reference(s):

- [Tock requests for fpx](references/requests.md)
- [Redux slice extractor](references/extract-redux-slice.mjs)
- [Tock](https://www.exploretock.com)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with shell command snippets, JSON bodies, and jq examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include commands that route requests through a paired browser session and may print signed-in reservation data.]

## Skill Version(s):

0.4.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

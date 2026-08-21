## Description:

urlgo is a browser-control CLI that connects to Chrome DevTools Protocol to open pages, capture screenshots, read page text or HTML, and execute JavaScript.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fslong520](https://clawhub.ai/user/fslong520)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use urlgo to inspect and interact with web pages through a dedicated browser session. It supports opening entry URLs, reading page text or HTML, taking screenshots, and performing page actions through selectors or JavaScript.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill gives an agent broad browser-control powers that may be unsafe on sensitive or authenticated sites.

Mitigation: Use it only with a dedicated browser session, avoid banking, admin, internal, or other sensitive authenticated sites unless each action is explicitly directed, and close the launched browser or clear the urlgo profile when finished.

Risk: The skill can execute JavaScript and perform clicks or typing in the active browser page.

Mitigation: Inspect the target page or source before interaction and constrain actions to user-approved selectors, pages, and inputs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/fslong520/skills/urlgo)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, files, guidance]

**Output Format:** [Markdown guidance with shell command examples; CLI responses may be plain text, HTML source, JSON-style JavaScript evaluation values, or PNG screenshot files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a running CDP browser session plus curl and the Python websockets package.]

## Skill Version(s):

6.5.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

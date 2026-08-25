## Description:

Headless browser automation CLI optimized for AI agents with accessibility tree snapshots and ref-based element selection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[terrycarter1985](https://clawhub.ai/user/terrycarter1985)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to operate browser sessions through the agent-browser CLI, including navigation, snapshots, ref-based interactions, session isolation, screenshots, PDFs, and saved state workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Browser automation can expose saved authentication state, cookies, localStorage, screenshots, or PDFs from logged-in sessions.

Mitigation: Treat browser state and captured artifacts as sensitive account data; do not commit or share them, and prefer test or low-privilege accounts for automation.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/terrycarter1985/skills/demo-resource-upload)
- [agent-browser Repository](https://github.com/vercel-labs/agent-browser)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, markdown]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance centers on the agent-browser CLI and browser session artifacts such as snapshots, screenshots, PDFs, cookies, and saved state files.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

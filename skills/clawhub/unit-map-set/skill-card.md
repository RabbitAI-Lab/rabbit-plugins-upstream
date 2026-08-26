## Description:

Turn user-supplied unit outline points into one still per unit mind map page.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Educators and classroom-content creators use this skill to turn confirmed unit or lesson outline points into a page-ordered set of classroom mind-map stills. It plans each page from supplied facts, confirms paid image generation, and reviews the returned stills against the approved page list.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The server security summary says the skill requests and manages broader Beatra account authority than the unit-map image purpose needs.

Mitigation: Install only when that shared Beatra device credential scope is acceptable, and prefer a narrower-scoped version if one becomes available.

Risk: Automatic updates are enabled by default and can replace package-owned files without a separate approval step.

Mitigation: Disable automatic updates before use in environments that require change review.

Risk: User-provided scans or classroom references may contain student or sensitive classroom information.

Mitigation: Avoid uploading sensitive classroom materials, or remove sensitive details before providing optional visual references.

Risk: Billable image generation can create duplicate charges if uncertain transport responses are retried incorrectly.

Mitigation: Use one opaque client_request_id per frozen page payload and retry only byte-identical requests with the same identity.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/unit-map-set)
- [Unit-map workflow](references/workflow.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Installation and authentication](references/installation-and-auth.md)
- [MCP connection](references/mcp-connection.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces page plans, confirmation cards, Beatra task details, generated image artifacts, billing summaries, and recovery guidance.]

## Skill Version(s):

0.1.1 (source: server release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

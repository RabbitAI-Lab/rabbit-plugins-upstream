## Description:

Turn a named product launch into three visual-tone stills, then one opening film clip for the stage screen.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External brand, marketing, and launch-event teams use this skill to plan a three-frame visual-tone board and generate one short stage-screen opening film for a named product or event launch.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security summary reports broad shared Beatra account authority covering media, wallet, artifact, and task access.

Mitigation: Review the requested authorization before use and install only when that shared credential scope is acceptable.

Risk: The security summary reports default-on automatic updates that use Beatra network services and local ~/.beatra state.

Mitigation: Disable automatic updates with `python3 scripts/mcp_client.py update --auto off` when explicit update control is required.

Risk: Brand references and generated media may include sensitive launch material.

Mitigation: Upload only files intentionally selected as brand references and inspect local files before sending them through the bundled client.

Risk: Billable image and video generation can create duplicate charges if uncertain requests are replayed with changed inputs.

Mitigation: Use one opaque `client_request_id` per unchanged paid request and recover uncertain responses with the same arguments before starting new work.

## Reference(s):

- [Product launch opening-film workflow](artifact/references/workflow.md)
- [Installation and authentication](artifact/references/installation-and-auth.md)
- [Billing, errors, and recovery](artifact/references/billing-errors-and-recovery.md)
- [Tasks and results](artifact/references/tasks-and-results.md)
- [MCP connection](artifact/references/mcp-connection.md)
- [Automatic updates and safety](artifact/references/automatic-updates-and-safety.md)
- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/product-launch-opening-film)
- [Beatra skill homepage](https://beatra.ai/skills/product-launch-opening-film)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a free visual-tone board first, then guides approved Beatra image and video generation requests through bundled scripts.]

## Skill Version(s):

0.1.2 (source: server release evidence and artifact manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

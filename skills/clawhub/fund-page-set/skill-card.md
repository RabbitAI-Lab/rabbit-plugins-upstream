## Description:

Turn user-supplied fund factsheet points into one still per page. This fund factsheet page studio lays out each prospectus page still from the supplied fund factsheet. Use it for factsheet page graphics, fund page set layouts, and page-by-page fund stills.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents in fund-content workflows use this skill to plan and generate one factsheet or prospectus-style still per supplied page from confirmed fund factsheet points, then review returned stills, task metadata, and billing details.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence reports a broad shared Beatra credential stored on disk.

Mitigation: Install only for users comfortable connecting a Beatra account, protect the local credential file, use an account with limited credits where practical, and revoke the device from the Beatra Console when finished.

Risk: Supplied fund content, optional reference files, and package telemetry are sent to Beatra.

Mitigation: Use only content the user is permitted to share with Beatra and avoid submitting sensitive or regulated material unless the deployment owner has approved that handling.

Risk: The security evidence reports silent package updates.

Mitigation: Disable automatic updates for controlled environments and run an explicit update check before planned use.

Risk: Image generation is billable and transport retries can duplicate work if request identity is mishandled.

Mitigation: Confirm the live price before paid calls, use one opaque request ID per page, and retry only unchanged requests with the same identity after uncertain delivery.

Risk: Generated factsheet stills can contain unreadable or incorrect text and are not certified disclosures.

Mitigation: Review visible text against the confirmed page list, report unreadable small type as a review item, and do not treat generated output as a performance forecast or official disclosure.

## Reference(s):

- [ClawHub Skill Listing](https://clawhub.ai/beatra-ai/skills/fund-page-set)
- [Beatra Skill Homepage](https://beatra.ai/skills/fund-page-set)
- [Fund-page workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [MCP connection](references/mcp-connection.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Image artifacts, Task metadata, Billing details]

**Output Format:** [Markdown guidance with inline shell commands, generated image artifacts, and returned task and billing JSON fields]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [One generated still is produced per approved page; returned details include task IDs, resolved models, observed dimensions, formats, and net charged credits when available.]

## Skill Version(s):

0.1.2 (source: server release and artifact manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

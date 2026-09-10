## Description:

Turn one product photo into a vertical product video with spoken narration, ready to post.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External merchants and commerce teams use this skill to turn a real product photo and merchant-supplied selling points into one narrated vertical product video for listings, launches, social posts, and storefront promotion.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The package requests broad Beatra generation, artifact, task, and spending authority through a shared credential.

Mitigation: Review the Beatra approval scopes before authorizing, require explicit confirmation before paid calls, and use the documented wallet and ledger reads when checking balance or charges.

Risk: The Beatra credential is persistent and shared across installed Beatra skills.

Mitigation: Use it only on devices where credential-file permissions are acceptable, avoid shared machines unless permissions are independently controlled, and revoke access through the documented disconnect flow or Beatra Console when it is no longer needed.

Risk: Silent package self-updates are enabled by default.

Mitigation: Disable automatic updates with the documented `python3 scripts/mcp_client.py update --auto off` command or use `--check` to inspect the available version before updating.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/product-video-studio)
- [Beatra Product Video Studio](https://beatra.ai/skills/product-video-studio)
- [The first frame](artifact/references/first-frame.md)
- [Writing the narration](artifact/references/copy-craft.md)
- [Commerce video workflow](artifact/references/workflow.md)
- [Installation and authentication](artifact/references/installation-and-auth.md)
- [Installation registration](artifact/references/installation-registration.md)
- [Tasks and results](artifact/references/tasks-and-results.md)
- [Billing, errors, and recovery](artifact/references/billing-errors-and-recovery.md)
- [MCP connection](artifact/references/mcp-connection.md)
- [Automatic updates and safety](artifact/references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](artifact/references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API Calls, Files]

**Output Format:** [Markdown guidance with inline shell commands, returned media artifacts, and task metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces one narrated vertical product video; remote generation may consume Beatra credits.]

## Skill Version(s):

0.1.5 (source: server release evidence and artifact manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

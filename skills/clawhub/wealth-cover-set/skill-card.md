## Description:

Turn user-supplied session names and themes into a four-to-eight still wealth cover set.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to plan and generate a consistent set of session-cover stills for investor education or wealth-session materials from user-confirmed session names, themes, language, destination, and optional brand references.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a shared Beatra device credential with broad media, task, artifact, and wallet-related authority.

Mitigation: Install only when those permissions are acceptable, review Beatra account permissions, and revoke or disconnect the device when access is no longer needed.

Risk: Automatic updates are enabled by default and can replace package-owned local files silently.

Mitigation: Review the package before installation and consider running the bundled update command to disable automatic updates after install.

Risk: Approved image generation consumes Beatra credits, and uncertain retries can duplicate paid work if request identity is not preserved.

Mitigation: Require the confirmation card before paid calls, preserve one client_request_id per still, and retry only identical uncertain requests with the original identity.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/wealth-cover-set)
- [Beatra skill homepage](https://beatra.ai/skills/wealth-cover-set)
- [Wealth cover pack workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Tasks and results](references/tasks-and-results.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance, API Calls]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a free pack plan before paid generation, then delivers generated stills with task IDs, dimensions, formats, resolved models, and net charged credits when approved.]

## Skill Version(s):

0.1.1 (source: server release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

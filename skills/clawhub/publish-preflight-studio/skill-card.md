## Description:

Checks social media copy before publication, flags advertising and regulated-claim wording, proposes replacements, reads the copy through likely audience profiles, scores reach signals, returns corrected copy, and can render a cover from approved wording.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Marketing teams, creators, agencies, and reviewers use this skill to preflight captions, titles, scripts, on-screen text, and tags before posting. It produces compliance findings with replacement wording, audience-profile reactions, reach scores, corrected copy, and optional cover-render instructions or results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The authoritative security evidence reports broad Beatra account access through a persistent shared device token.

Mitigation: Install only when that access is acceptable, keep the token out of chat, logs, command arguments, and environment variables, and use the bundled uninstall or Beatra Console revocation path when access is no longer needed.

Risk: The authoritative security evidence reports silent self-updates of installed package files.

Mitigation: Disable automatic updates with the bundled update control when explicit change control is required, and rely on the package's checksum-verified update path before accepting newer files.

Risk: Cover rendering is paid remote work and can create duplicate cost if retried incorrectly.

Mitigation: Confirm the exact wording, route, canvas, price estimate, and stable request ID before rendering; after submission, poll the recorded task rather than creating a replacement task.

Risk: The compliance and audience reads are structured guidance, not final legal clearance or measured audience research.

Mitigation: Use the findings and replacements as review inputs, keep substantiation and approval decisions with the user or responsible reviewer, and inspect generated cover wording before publication.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/beatra-ai/skills/publish-preflight-studio)
- [Beatra Skill Homepage](https://beatra.ai/skills/publish-preflight-studio)
- [Screening the copy](references/compliance-screen.md)
- [Reading it as the audience](references/audience-read.md)
- [Preflight workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Tasks and results](references/tasks-and-results.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with tables, pasteable text blocks, inline shell commands, and optional task metadata or artifact links for rendered covers.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include compliance flags, replacement copy, audience-profile findings, reach scores, change lists, Beatra task IDs, billing.net_charged_credits, and rendered-cover artifact links.]

## Skill Version(s):

0.1.1 (source: server release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

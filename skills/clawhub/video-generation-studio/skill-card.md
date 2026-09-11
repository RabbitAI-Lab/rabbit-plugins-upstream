## Description:

Video Generation Studio helps agents plan, generate, edit, extend, review, and iterate short AI video clips from text, supplied images, multimodal references, or existing footage.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and their agents use this skill to choose an appropriate Beatra video route, prepare media and prompt details, run paid image or video stages with confirmation, and review delivered clips for fit before further iteration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review reports broad Beatra account authority through a shared local device credential.

Mitigation: Install only after reviewing the requested scopes, keep the credential private, and reconnect or revoke access only through the documented authorization and uninstall flows.

Risk: The bundled client contacts Beatra services, stores local state under ~/.beatra, and silently self-updates package files by default.

Mitigation: Review the package before use and disable silent updates with the documented update command if automatic replacement is not acceptable.

Risk: Image and video generation stages are paid Beatra credit-consuming tasks, and final charges may differ from provisional estimates.

Mitigation: Require the admission card and user confirmation before each paid video stage, then report only terminal billing fields such as billing.net_charged_credits.

Risk: Generated video can drift from requested identity, product details, camera behavior, audio, or continuity even when the task succeeds.

Mitigation: Review delivered clips against the brief and recommend the smallest focused edit, extension, or new render rather than presenting an unreviewed result as final.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/beatra-ai/skills/video-generation-studio)
- [Beatra Skill Homepage](https://beatra.ai/skills/video-generation-studio)
- [Intent and Routing](references/intent-and-routing.md)
- [Shot Design](references/shot-design.md)
- [Image-assisted Video](references/image-assisted-video.md)
- [Video Recipes](references/video-recipes.md)
- [Review and Iteration](references/review-and-iteration.md)
- [Tasks and Results](references/tasks-and-results.md)
- [Billing, Errors, and Recovery](references/billing-errors-and-recovery.md)
- [Installation and Authentication](references/installation-and-auth.md)
- [MCP Connection](references/mcp-connection.md)
- [Installation Registration](references/installation-registration.md)
- [Automatic Updates and Safety](references/automatic-updates-and-safety.md)
- [Uninstall and Disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return Beatra task and artifact summaries, including terminal status, dimensions, duration, usage, and net charged credits when available.]

## Skill Version(s):

0.1.5 (source: server release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

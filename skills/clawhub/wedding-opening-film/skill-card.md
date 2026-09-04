## Description:

Turn couple-supplied ceremony facts into three wedding opening film storyboard keyframes, then one opening film.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External photo studios and wedding planners use this skill to turn known ceremony facts into a labeled three-keyframe storyboard and, after approval, a Beatra-generated wedding opening film.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The package uses a shared persistent Beatra device credential with broad media, task, artifact, wallet, speech, music, and voice scopes.

Mitigation: Authorize only if those scopes are acceptable, keep the token confined to ~/.beatra/credentials.json, and use the bundled uninstall or Beatra Console revocation flow when access should end.

Risk: Silent automatic updates are enabled by default and can change package files before ordinary Beatra commands.

Mitigation: Disable automatic checks with scripts/mcp_client.py update --auto off when deterministic local behavior is required, or use scripts/mcp_client.py update --check before updating.

Risk: Paid image and video generation can consume Beatra credits, and careless retries can create duplicate work.

Mitigation: Read live model pricing before each paid phase, require approval before submitting, use one opaque client_request_id per logical request, and retry only with byte-identical arguments when delivery is uncertain.

Risk: The upload helper can send local files to Beatra for optional reference workflows.

Mitigation: Avoid uploading sensitive files, inspect each file first, provide the exact MIME type, and pass only returned artifact IDs to remote generation tools.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/wedding-opening-film)
- [Beatra skill homepage](https://beatra.ai/skills/wedding-opening-film)
- [Wedding opening workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [MCP connection](references/mcp-connection.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Files, Guidance]

**Output Format:** [Markdown guidance with JSON and shell command snippets, plus generated image and video artifacts returned from Beatra tasks.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a free three-keyframe storyboard sheet before paid generation; approved paid work can return three still images and one 2-15 second opening film.]

## Skill Version(s):

0.1.1 (source: server release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

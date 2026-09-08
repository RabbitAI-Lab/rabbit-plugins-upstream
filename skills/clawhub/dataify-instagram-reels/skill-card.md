## Description:

Collect Instagram Reel records from a Reel URL, Reel-list URL, or website URL. Do not use for profile data, post comments, or Google Shopping products.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dataify-server](https://clawhub.ai/user/dataify-server)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to submit Dataify collection jobs for Instagram Reels by detail URL, list/profile URL, or website/list URL, then receive the resulting task status and collected output.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends target Instagram URLs, filters, file names, and the user's Dataify API token to Dataify.

Mitigation: Install and run it only when the user intends to use Dataify for Instagram Reels collection, has authority to collect the targets, and is comfortable sharing those inputs with Dataify.

Risk: Collection scope can affect Dataify credit usage and may involve private or sensitive targets.

Mitigation: Review target URLs, filters, and collection volume before submission; avoid private or sensitive targets unless collection is authorized.

## Reference(s):

- [Modes and parameters](references/modes-and-parameters.md)
- [Dataify dashboard login](https://dashboard.dataify.com/login?utm_source=skill)
- [ClawHub skill page](https://clawhub.ai/dataify-server/skills/dataify-instagram-reels)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, JSON]

**Output Format:** [Markdown guidance with shell commands and JSON task/result summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return a Dataify task ID, task status, normalized collection parameters, and the final collected result; API token values should not be exposed.]

## Skill Version(s):

1.3.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

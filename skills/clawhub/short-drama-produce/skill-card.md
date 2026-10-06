## Description:

Runs confirmed image, video, speech, and music production tasks for short-drama projects and records the resulting media and run status.

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT

## Use Case:

Short-drama creators and production teams use this skill to preview and explicitly approve bounded media-generation jobs, then save generated assets and audit records to their projects.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Paid generation or retries can incur unexpected charges.

Mitigation: Review the full job preview and require explicit confirmation for each submission or retry; check for unfinished provider jobs before resubmitting.

Risk: Project prompts and reference media are sent to external providers.

Mitigation: Use approved providers and avoid confidential project content unless those providers are authorized to receive it.

Risk: Provider credentials or destinations may be mishandled.

Mitigation: Keep adapter configuration outside the project, use approved provider URLs, and manage API keys through the runtime environment.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/worldwonderer/skills/short-drama-produce)
- [Adapter contract](references/adapter-contract.md)
- [GPT Image 2 model documentation](https://developers.openai.com/api/docs/models/gpt-image-2)
- [MiniMax music generation documentation](https://platform.minimax.io/docs/api-reference/music-generation)
- [MiniMax text-to-speech documentation](https://platform.minimax.io/docs/api-reference/speech-t2a-http)
- [Volcengine video generation documentation](https://www.volcengine.com/docs/82379/1520757)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration guidance]

**Output Format:** [Markdown with job previews, command examples, and run summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [After explicit approval, generated media and concise audit records are saved to the project.]

## Skill Version(s):

1.0.0 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

AI播客生成 converts public PDF URLs, pasted text, notes, and web links into multilingual two-host conversational podcast episodes through the MagicPodcast API and returns shareable podcast links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

External content creators, educators, researchers, and teams use this skill to turn public PDFs or supplied text into shareable audio programs for learning, content distribution, and knowledge sharing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: User-provided text, notes, or public PDF URLs are sent to MagicPodcast for processing.

Mitigation: Do not use confidential, regulated, or proprietary content unless the service privacy and retention terms have been reviewed and sharing is permitted.

Risk: API keys can be exposed if pasted into prompts, logs, or files.

Mitigation: Store MAGICPODCAST_API_KEY in an environment variable or secret store and avoid echoing or committing credentials.

Risk: Generated podcast audio may omit, simplify, or misstate details from the source material.

Mitigation: Review generated episodes before publishing, teaching from, or redistributing them.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/thcjp/skills/ai-podcast)
- [MagicPodcast Skill Platform](https://www.magicpodcast.app/skill-platform)
- [MagicPodcast Dashboard](https://www.magicpodcast.app/app)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, API calls, Guidance]

**Output Format:** [Markdown guidance with shell command snippets, API responses, dashboard links, and shareable podcast URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses asynchronous podcast generation; users may need to check task status before a share link is available.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

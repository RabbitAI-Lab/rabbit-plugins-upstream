## Description:

Summarize any web page by URL or by pasting text. Returns a concise structured summary with key points, entities, and action items.

This skill is ready for commercial/non-commercial use.

## Publisher:

[terrycarter1985](https://clawhub.ai/user/terrycarter1985)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to turn URLs or pasted long-form text into a concise digest with a TL;DR, key points, named entities, and applicable action items.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Web pages and pasted text can contain sensitive information or prompt-injection content.

Mitigation: Use the skill only with sources the user is comfortable having the agent fetch and summarize, and treat fetched or pasted content as untrusted source material rather than instructions.

Risk: Broad activation wording may cause the skill to be selected for loosely related summarization requests.

Mitigation: Confirm that the user wants a web page or pasted text summarized before fetching or processing content.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/terrycarter1985/skills/web-summarizer)
- [Publisher Profile](https://clawhub.ai/user/terrycarter1985)
- [Artifact SKILL.md](artifact/SKILL.md)
- [Artifact README.md](artifact/README.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown structured summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Summaries may include a one-sentence TL;DR, 3-5 key points, named entities, and action items when applicable.]

## Skill Version(s):

1.0.0 (source: server release metadata and artifact _meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

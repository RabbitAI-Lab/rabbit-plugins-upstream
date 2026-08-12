## Description:

Download and save Perplexity.ai conversations as individual Markdown files, supporting single-thread, URL-list, and full-history exports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[j3ffyang](https://clawhub.ai/user/j3ffyang)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to archive Perplexity.ai threads as local Markdown files from one thread URL, a provided URL list, or a full history export.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Full-history export can collect and save a large amount of private Perplexity conversation data.

Mitigation: Prefer explicit thread URLs or a limited URL list; paste full logged-in page content only after reviewing what it may reveal.

Risk: Exported Markdown files may contain sensitive prompts, answers, source links, or history metadata.

Mitigation: Store outputs in a controlled location, review files before sharing, and delete exports that are no longer needed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/j3ffyang/skills/perplexity-downloader)
- [Perplexity.ai](https://www.perplexity.ai/)

## Skill Output:

**Output Type(s):** [markdown, files, guidance]

**Output Format:** [Markdown files with optional Markdown index files and progress text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes one .md file per Perplexity thread under ~/perplexity-downloader/outputs/; bulk and history modes process threads sequentially.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

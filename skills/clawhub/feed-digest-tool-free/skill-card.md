## Description: <br>
A free RSS digest skill that helps an agent use the local feed CLI to fetch subscriptions, scan unread entries, apply basic keyword filtering, read Markdown article content, and produce concise reading summaries. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to manage personal RSS subscriptions, reduce information overload, and generate lightweight daily digests from unread feed entries. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses a third-party feed CLI to fetch configured RSS sources over the network. <br>
Mitigation: Install the feed CLI only from a trusted source and use feeds whose network access and content you are comfortable allowing in the agent environment. <br>
Risk: RSS article and feed text can contain untrusted content that may be summarized or shown to the agent. <br>
Mitigation: Treat feed content as data rather than instructions, and review generated digests before using them for decisions or follow-up automation. <br>
Risk: Bulk marking entries as read can change local reading state for multiple feed items. <br>
Mitigation: Review selected entry IDs before running read-status updates, especially after broad keyword filtering. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/feed-digest-tool-free) <br>
- [Publisher profile](https://clawhub.ai/user/thcjp) <br>
- [Detailed reference](references/detail.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and structured text with inline shell commands and Python examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Digest entries may include feed titles, source names, basic keyword scores, short summaries, command output, status, logs, and error messages.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata; artifact frontmatter says 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

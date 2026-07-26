## Description: <br>
Summarize recent emails, generate a thematic image, and send a formatted HTML email report with the summary and image. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[matthewxfz3](https://clawhub.ai/user/matthewxfz3) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Employees, external users, and developers can use this skill to turn recent Gmail messages into a concise HTML digest with a generated thematic image. It is suited to daily news digests, project updates, and email-based reporting workflows where recipients and source queries are explicitly controlled. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill accesses private Gmail content and sends outbound email. <br>
Mitigation: Use only trusted Gmail accounts and recipient lists, and review the generated digest before any send action. <br>
Risk: Broad Gmail queries may expose sensitive or unrelated messages. <br>
Mitigation: Use narrow Gmail search filters and avoid sensitive queries until explicit preview and confirmation safeguards are added. <br>
Risk: The current summarization behavior may not reflect the actual email content. <br>
Mitigation: Verify the digest content against the source email before sending or relying on it. <br>


## Reference(s): <br>
- [Email Filters Reference](references/email-filters.md) <br>
- [HTML Email Template](references/html-template.html) <br>
- [ClawHub Skill Page](https://clawhub.ai/matthewxfz3/skills/email-news-digest) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [JSON summary data, generated image file, and formatted HTML email sent through Gmail] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires recipient addresses, a Gmail search query, and an image prompt; the current summarization script uses placeholder summary content.] <br>

## Skill Version(s): <br>
1.0.0 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

## Description: <br>
Drafts LinkedIn replies to existing comment URLs, resolves the correct top-level parent comment for threaded replies, and prepares posting through Publora after approval. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sergebulaev](https://clawhub.ai/user/sergebulaev) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
People managing LinkedIn conversations use this skill to reply to a specific existing comment URL, continue an author thread, or re-engage a dormant conversation while preserving LinkedIn's parent-comment rules. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Approving a post action may publish both a LinkedIn reply and a reaction to the target comment. <br>
Mitigation: Review the approval card carefully before posting and approve only when both the reply and reaction are intended. <br>
Risk: The workflow may use LinkedIn, Publora, or Apify credentials for social posting and thread lookup. <br>
Mitigation: Use only credentials intended for this workflow and limit access to accounts authorized for the planned LinkedIn activity. <br>


## Reference(s): <br>
- [Reply Templates](references/reply-templates.md) <br>
- [Examples](references/examples.md) <br>
- [LinkedIn Comment Threading Rules](references/threading-rules.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, API calls, Guidance] <br>
**Output Format:** [Markdown approval card with reply drafts, reaction suggestion, and thread context summary] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Drafts are 150-300 characters; posting a reply and reaction requires user approval.] <br>

## Skill Version(s): <br>
1.0.9 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

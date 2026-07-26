## Description: <br>
Drafts LinkedIn comment variants for a supplied post URL, suggests a reaction, and supports posting after explicit user approval. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sergebulaev](https://clawhub.ai/user/sergebulaev) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
People managing LinkedIn engagement use this skill to turn a post URL into short, voice-matched comment drafts and reaction suggestions. It is best suited for reviewed, user-approved engagement rather than unattended posting. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The posting flow includes timing and prospect-warmup guidance that may conflict with LinkedIn or posting-provider rules if used for automated or scaled engagement. <br>
Mitigation: Review every draft and posting action, keep engagement manually approved, and check LinkedIn and posting-provider rules before using timing or outreach guidance. <br>
Risk: Generated comments may be inaccurate, off-brand, or inappropriate for the target post. <br>
Mitigation: Verify the post context and edit the final comment before approval; skip sponsored, deleted, or low-quality posts. <br>


## Reference(s): <br>
- [Comment templates](references/comment-templates.md) <br>
- [Examples](references/examples.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance] <br>
**Output Format:** [Markdown with draft comment variants, reaction suggestions, template labels, rationales, and an approval prompt] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces 1-3 concise comment drafts and should only proceed to public posting or reaction after explicit user approval.] <br>

## Skill Version(s): <br>
1.0.9 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

## Description: <br>
Agent Content Pipeline provides a human-in-the-loop social content workflow for drafting, reviewing, approving, and posting content to LinkedIn, X, and experimental Reddit. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[larsderidder](https://clawhub.ai/user/larsderidder) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers, creators, and agents use this skill to set up a draft-review-approve-post workflow for social posts while keeping approval and posting under human control. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Posting credentials and browser tokens could be exposed through chats, shared files, logs, or prompts. <br>
Mitigation: Enter X auth_token and ct0 values only into a trusted local CLI prompt, use secure initialization where possible, and avoid copying secrets into shared contexts. <br>
Risk: Social posts could be approved or published without the intended human review. <br>
Mitigation: Keep approval and posting as human-controlled steps, use dry runs before posting, and rely on the workflow directories to separate drafts, reviewed content, approved posts, and posted archives. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/larsderidder/skills/agent-content-pipeline) <br>
- [Project homepage](https://github.com/larsderidder/agent-content-pipeline) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown files with YAML frontmatter, concise guidance, and CLI commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Human approval is required before approved status or posting; dry-run posting is available.] <br>

## Skill Version(s): <br>
0.2.3 (source: server release metadata and skill.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

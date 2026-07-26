## Description: <br>
Provides a complete usage guide for the Article Review Platform, including article listing, content reading, article creation, status updates, platform publishing status sync, and review workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mayf3](https://clawhub.ai/user/mayf3) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, writers, reviewers, and publishing operators use this skill to coordinate an article workflow across drafting, review, approval, publishing, and publication status tracking. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Agents may create, update, publish, or delete live article workflow records. <br>
Mitigation: Verify the endpoint is a sandbox before testing, and require explicit human confirmation before any write, publication, or deletion. <br>
Risk: Publishing status updates may misrepresent platform outcomes if applied without checking each target platform. <br>
Mitigation: Review platform status and publish logs before marking a platform or article as published. <br>


## Reference(s): <br>
- [Writer Role Guide](references/role-writer.md) <br>
- [Reviewer Role Guide](references/role-reviewer.md) <br>
- [Publisher Role Guide](references/role-publisher.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/mayf3/skills/article-review-platform) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, API Calls, Configuration instructions] <br>
**Output Format:** [Markdown with inline bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Provides role-specific workflow guidance for local Article Review Platform API operations.] <br>

## Skill Version(s): <br>
1.0.0 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

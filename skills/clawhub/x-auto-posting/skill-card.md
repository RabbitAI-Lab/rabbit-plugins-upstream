## Description: <br>
X Auto Posting helps an agent collect keyword-driven X topics, extract style references, draft user-approved posts, publish through a logged-in browser session, and track 24-hour performance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[browseract-cli](https://clawhub.ai/user/browseract-cli) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and content operators use this skill to run an X content operations workflow from keyword rotation and topic selection through approved publishing and performance tracking. It is intended for accounts where the user can supervise posting decisions in an authenticated browser session. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can use a logged-in X session to publish posts and replies. <br>
Mitigation: Require structured user approval before publishing, replying, or confirming the pre-publish screenshot, and stop when approval is not provided. <br>
Risk: Local posting history, screenshots, drafts, and tracking files may contain sensitive account or campaign information. <br>
Mitigation: Store only necessary records in the local workspace and periodically delete tracking files when posting history is sensitive. <br>
Risk: Automated posting can trigger X account limits or platform controls. <br>
Mitigation: Keep the default daily quota and minimum interval, ask before force-continuing when limits are reached, and stop the run on 403 or 429 responses. <br>
Risk: Draft text, media, or links could publish unintended or noncompliant content. <br>
Mitigation: Run the content verification gate, enforce the 280-character and link/contact restrictions, verify media paths, and require final screenshot approval before clicking Post. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/browseract-cli/skills/x-auto-posting) <br>
- [Phase 1 Topic Collection](artifact/references/phase1-topic-collection.md) <br>
- [Phase 2 Case Collection](artifact/references/phase2-case-collection.md) <br>
- [Phase 4 Writing](artifact/references/phase4-writing.md) <br>
- [Phase 5 Publish](artifact/references/phase5-publish.md) <br>
- [Phase 6 Tracking](artifact/references/phase6-tracking.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with shell command snippets, JSON records, local files, screenshots, and tracking reports.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Creates local workspace state for keywords, selected topics, drafts, published posts, incidents, and tracking history.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

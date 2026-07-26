## Description: <br>
Converts a Claude Code session into a blog post, case study, or Reddit post. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineering teams use this skill to turn completed Claude Code coding sessions into publishable blog posts, case studies, social threads, or Reddit posts grounded in git history, file changes, test results, and conversation context. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Session context, git history, or changed files may contain secrets, private customer data, or internal details that should not be published. <br>
Mitigation: Review the source session material before drafting and remove sensitive details from any generated post. <br>
Risk: Generated drafts may be written under docs/posts/ and could be committed or published before review. <br>
Mitigation: Review every generated file under docs/posts/ before committing, sharing, or publishing it. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/athola/skills/nm-scribe-session-to-post) <br>
- [Homepage metadata: claude-night-market scribe plugin](https://github.com/athola/claude-night-market/tree/master/plugins/scribe) <br>
- [Artifact documentation: session extraction](artifact/modules/session-extraction.md) <br>
- [Artifact documentation: narrative structure](artifact/modules/narrative-structure.md) <br>
- [Artifact documentation: Reddit format](artifact/modules/reddit-format.md) <br>


## Skill Output: <br>
**Output Type(s):** [markdown, guidance, shell commands] <br>
**Output Format:** [Markdown with inline shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write publishable draft files under docs/posts/ when requested.] <br>

## Skill Version(s): <br>
1.9.16 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

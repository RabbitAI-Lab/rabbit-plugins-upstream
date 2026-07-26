## Description: <br>
Posts text, media, quote tweets, and long-form Markdown articles to X (Twitter) through browser-assisted workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jimliu](https://clawhub.ai/user/jimliu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to draft regular X posts, quote tweets, video posts, and X Articles from provided text, media, or Markdown while keeping the user in the review path before public publishing. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can control a real Chrome/X session and create externally visible posts. <br>
Mitigation: Require the user to review the exact post or article and give explicit final confirmation before clicking Post, Publish, or using --submit. <br>
Risk: The skill can manipulate clipboard contents and send paste keystrokes. <br>
Mitigation: Run the pre-flight permission check and keep browser actions visible so the user can verify copied content before submission. <br>
Risk: The CDP fallback can automatically terminate Chrome debugging processes. <br>
Mitigation: Use Chrome Computer Use or the requested Chrome Extension path when available, and avoid the automatic kill step unless the user accepts the impact on other Chrome debugging sessions. <br>
Risk: The skill stores and reuses X login state in a Chrome profile. <br>
Mitigation: Use only on trusted machines and review the selected profile before running workflows that interact with X. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/jimliu/skills/baoyu-post-to-x) <br>
- [Project homepage](https://github.com/JimLiu/baoyu-skills#baoyu-post-to-x) <br>
- [Regular posts guide](references/regular-posts.md) <br>
- [X Articles guide](references/articles.md) <br>
- [Codex Chrome Extension file upload guidance](https://developers.openai.com/codex/app/chrome-extension#upload-files) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Code, Configuration] <br>
**Output Format:** [Markdown with inline shell commands and browser workflow steps] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May prepare browser drafts, clipboard content, converted HTML, and media upload steps for user review before public posting.] <br>

## Skill Version(s): <br>
1.58.1 (source: frontmatter and release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

## Description:

Blogger Auto-Follow extracts blogger lists from images or text and guides an agent through local-browser workflows for bulk following on Douyin, Xiaohongshu, Bilibili, X/Twitter, and YouTube while maintaining a local creator archive.

This skill is ready for commercial/non-commercial use.

## Publisher:

[helloyxs](https://clawhub.ai/user/helloyxs)

### License/Terms of Use:

MIT

## Use Case:

External users and developers use this skill to convert screenshots or text lists of creators into reviewed platform-specific follow tasks, run the local browser workflow after login, and maintain a local archive of followed creator profiles.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can make real follow or subscribe changes from a logged-in social account.

Mitigation: Review the extracted target list and target platform before execution, and use an isolated browser profile when practical.

Risk: Bulk following and anti-detection automation may violate platform rules or trigger account restrictions.

Mitigation: Keep batches small, avoid broad prompts such as "follow everyone," and stop execution when platforms show rate-limit, CAPTCHA, or safety challenges.

Risk: Incorrect OCR or text extraction can target the wrong creator accounts.

Mitigation: Require a human review of the generated preview table before running browser automation.

## Reference(s):

- [Source repository](https://github.com/helloyxs/blogger-auto-follow)
- [ClawHub skill page](https://clawhub.ai/helloyxs/skills/blogger-auto-follow)
- [Anti-Bot & Anti-Ban Guidelines](references/anti_bot_guidelines.md)
- [Supported Platforms](references/supported_platforms.md)
- [FAQ and Best Practices](references/faq_and_best_practices.md)
- [Industry Categories Guide](references/industry_categories_guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON data files and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May open and control a logged-in local browser session and write local creator archive files.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

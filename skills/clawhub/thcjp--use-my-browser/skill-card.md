## Description:

Controls a user's Chrome browser to read pages, navigate, extract content, fill forms, interact with elements, capture screenshots, and run page JavaScript.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and operators use this skill to let an agent operate Chrome for page navigation, page text extraction, element interaction, form filling, screenshot capture, and browser-state checks. It is best suited to user-approved browser automation workflows where the user is comfortable granting access to the active browser session.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can operate a user's logged-in Chrome session and may read page content or perform browser actions as the user.

Mitigation: Use only on sites and accounts where the user explicitly approves agent access, and avoid sensitive accounts unless the task is narrowly scoped and user-approved.

Risk: The skill documents page JavaScript execution, which can broaden the impact of mistakes or malicious instructions on a page.

Mitigation: Prefer targeted element actions when possible, review JavaScript before execution, and avoid running scripts on pages containing sensitive data.

Risk: The server security summary rates the release as suspicious because scope and safety boundaries are broad and inconsistent.

Mitigation: Review the skill carefully before installation, verify the required browser extension or bridge separately, and keep browser automation constrained to explicit navigation, extraction, form filling, and script execution tasks.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/thcjp/skills/use-my-browser)
- [Publisher profile](https://clawhub.ai/user/thcjp)
- [Artifact SKILL.md](artifact/SKILL.md)
- [SkillHub homepage from artifact metadata](https://skillhub.cn/skill/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with JSON examples and browser automation guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include selectors, extracted page text, JSON-like tool call examples, troubleshooting steps, and browser-operation guidance.]

## Skill Version(s):

1.0.0 (source: server release metadata and target metadata; artifact frontmatter reports 1.0.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

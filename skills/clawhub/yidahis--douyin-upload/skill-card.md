## Description:

Generates Douyin article drafts and cover images from a topic, then can publish them through the sau command-line tool.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yidahis](https://clawhub.ai/user/yidahis)

### License/Terms of Use:

MIT-0

## Use Case:

Content creators and social media operators use this skill to turn a topic into a Douyin-ready article, cover image, and optional publish action. It supports article-oriented Douyin workflows, not video upload or editing existing posts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can publish to a real Douyin account without a final confirmation gate.

Mitigation: Use a test Douyin account and review generated content before allowing publish actions; use skip-publish mode when only content generation is needed.

Risk: Security evidence flags unsafe command and install behavior.

Mitigation: Avoid themes containing shell metacharacters, do not install the bundled sau.sh as a trusted sau command, and review install.sh before running it.

Risk: Dependency pinning and .env handling need review before installation.

Mitigation: Install in an isolated environment, verify dependencies, and manage OPENAI_API_KEY outside shared or committed files.

## Reference(s):

- [Douyin Upload README](references/README.md)
- [Douyin Upload Examples](references/examples.md)
- [ClawHub release page](https://clawhub.ai/yidahis/skills/douyin-upload)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration]

**Output Format:** [Markdown articles, JPG cover images, JSON logs, and shell command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can generate local files and can publish to a configured Douyin account through sau.]

## Skill Version(s):

1.0.0 (source: evidence release.version, artifact _meta.json, and scripts/config.py)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

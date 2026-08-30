## Description:

Miao Vision helps agents create local-first article infographics, HTML/PDF reports, browser decks, recurring reports, and spec validations from user-provided URLs, Markdown/text, and local structured data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[miaoshou.dev](https://clawhub.ai/user/miaoshou.dev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and agent users use this skill to turn user-provided articles, local text, and local tabular data into self-contained visual deliverables. It supports local-first report, infographic, deck, recurring-report, export, and spec-validation workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may ask the user to approve installation or use of the helper Miao Vision CLI.

Mitigation: Approve the installer only when the requested binary, path, and release source are expected; stricter environments should preinstall a reviewed compatible binary or set MIAO_VISION_HOME to a controlled location.

Risk: The shared CLI remains installed after plugin upgrades or uninstall.

Mitigation: Remove ~/.miao-vision when the shared CLI is no longer wanted.

Risk: The skill processes user-provided files, webpages, metadata, specs, and CLI output.

Mitigation: Treat those inputs as untrusted evidence and keep outputs grounded in the supplied sources.

## Reference(s):

- [Article Infographic Workflow](artifact/references/article.md)
- [Report Workflow](artifact/references/report.md)
- [Browser Deck Workflow](artifact/references/deck.md)
- [Outcome Brief Workflow](artifact/references/outcome-brief.md)
- [Miao Vision ClawHub Skill Page](https://clawhub.ai/miaoshou.dev/skills/miao-vision-skill)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and generated local artifact files such as HTML, PDF, PNG, and JSON/YAML specs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are local-first and grounded in user-provided inputs; PDF and PNG export may require optional browser dependencies.]

## Skill Version(s):

0.6.0 (source: server release evidence and install/README.md)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

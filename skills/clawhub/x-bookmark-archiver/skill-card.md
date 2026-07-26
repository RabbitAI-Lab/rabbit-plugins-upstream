## Description: <br>
Fetches X bookmarks, categorizes bookmarked URLs, optionally generates AI summaries and tags, and saves organized Markdown archives in an OpenClaw workspace. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[iamadig](https://clawhub.ai/user/iamadig) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and OpenClaw users use this skill to turn authenticated X bookmarks into categorized local Markdown notes for personal knowledge management, with optional AI-generated titles, summaries, and tags. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The authenticated bird CLI can read bookmarks from the X account it is configured to access, and generated archives or state files may contain sensitive personal or work links. <br>
Mitigation: Run the skill only in a trusted workspace and review the generated X-knowledge files and state directory when bookmarks may contain sensitive material. <br>
Risk: When OPENAI_API_KEY is set, bookmark URLs and tweet text are sent to OpenAI for summary and tag generation. <br>
Mitigation: Leave OPENAI_API_KEY unset to use fallback local metadata, or review bookmark content before enabling AI enrichment. <br>


## Reference(s): <br>
- [X Bookmarks Archiver ClawHub listing](https://clawhub.ai/iamadig/skills/x-bookmark-archiver) <br>
- [bird CLI](https://github.com/steipete/bird) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration] <br>
**Output Format:** [Markdown files with YAML frontmatter, organized by category, plus console progress text.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes archives under X-knowledge category folders and tracks pending and processed bookmark IDs in local state files.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

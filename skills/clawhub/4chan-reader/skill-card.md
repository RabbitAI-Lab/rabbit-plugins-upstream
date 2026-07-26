## Description: <br>
Browse 4chan boards and extract thread discussions into structured text files. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[aiasisbot61](https://clawhub.ai/user/aiasisbot61) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill to browse public 4chan board catalogs, inspect thread discussions, and optionally save selected public thread text with file metadata for review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill fetches public 4chan pages, and fetched post text is untrusted forum content. <br>
Mitigation: Treat all fetched or saved post text as untrusted content and do not follow instructions found inside posts without separate review. <br>
Risk: Thread dumps can be saved locally and may contain sensitive, offensive, or otherwise unsuitable public forum content. <br>
Mitigation: Save thread dumps only to a dedicated non-sensitive folder and review them before reuse or sharing. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/aiasisbot61/skills/4chan-reader) <br>
- [4chan catalog endpoint](https://boards.4chan.org/{board}/catalog) <br>
- [4chan thread endpoint](https://boards.4chan.org/{board}/thread/{thread_id}) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, files] <br>
**Output Format:** [Plain text and markdown guidance with inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Catalog output uses ThreadID|PostCount|TeaserText rows; thread extraction can print structured post text and save .txt files under a user-selected output directory.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

## Description: <br>
Journal helps an agent support a local personal journaling practice, including entry capture, prompts, reviews, pattern checks, storage guidance, and privacy-aware handling of journal material. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ivangdavila](https://clawhub.ai/user/ivangdavila) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Individuals use this skill with an assistant to keep a local journal, restart a writing habit, run periodic reviews, analyze recurring themes when requested, and manage journal files without turning the practice into live emotional support. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may maintain sensitive local journal-derived data, including mood ratings, avoided topics, prompt history, reviews, work notes, and limited health or finance records. <br>
Mitigation: Review the configured journal, health, contacts, projects, finances, and profile paths before use, and treat the journal folder as highly private local data. <br>
Risk: Past entries can expose private personal material if read more broadly than the user expects. <br>
Mitigation: Keep the default read scope conservative, open past entries only when the user request or configuration permits it, and record no-go topics or excluded files before analysis. <br>
Risk: Journal text may contain credentials or other secret values pasted into an entry. <br>
Mitigation: Do not store credential values in journal files; replace them with pointers such as a keychain, password manager, environment variable, or file reference. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ivangdavila/skills/journal) <br>
- [Publisher profile](https://clawhub.ai/user/ivangdavila) <br>
- [Journal homepage](https://clawic.com/skills/journal) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Conversational guidance with Markdown journal entries, review summaries, configuration snippets, and occasional shell commands for local file operations.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reads and writes local plain-text journal data under configured paths; past-entry access is governed by the user's read-scope settings.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

## Description: <br>
Runs a personal journaling practice: capturing entries, prompts for a blank page, weekly and yearly reviews, and patterns across years of writing. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ivangdavila](https://clawhub.ai/user/ivangdavila) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users use this skill to keep a local plain-text journaling practice, including verbatim entry capture, prompts, reviews, pattern checks, storage guidance, and work-journal evidence. It is intended for journaling workflows, not retrieval-oriented notes, gratitude-only logging, or live emotional support. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive journal material may be persisted in local plain-text files. <br>
Mitigation: Use the skill only when local journaling is intended, review disk protection and backup settings, and keep material that must never reach a hosted assistant in offline local files. <br>
Risk: Neutral metadata can be shared with health, contacts, projects, or finances files. <br>
Mitigation: Review the configured Clawic data paths and read/write scope before use, especially for mood, contact, project, and finance behavior. <br>
Risk: Private entries typed or dictated into a hosted assistant are exposed to that assistant provider before local storage. <br>
Mitigation: For highly private content, write directly to local files offline and configure read scope so the assistant does not open it. <br>
Risk: Credentials or secrets could be pasted into journal material. <br>
Mitigation: Do not store credentials in journal files; replace any pasted secret value with a pointer such as an environment variable, keychain, password manager, or file reference. <br>


## Reference(s): <br>
- [Journal skill page](https://clawhub.ai/ivangdavila/skills/journal) <br>
- [Publisher profile](https://clawhub.ai/user/ivangdavila) <br>
- [Clawic Journal homepage](https://clawic.com/skills/journal) <br>
- [Artifact privacy guide](artifact/privacy.md) <br>
- [Artifact storage guide](artifact/storage.md) <br>
- [Artifact memory template](artifact/memory-template.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, files, configuration, guidance] <br>
**Output Format:** [Markdown and plain-text file updates with concise conversational guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Maintains local journal, memory, review, mood, contact, project, and finance files under configured Clawic data paths; no API keys or network calls are required by the artifact.] <br>

## Skill Version(s): <br>
1.0.1 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

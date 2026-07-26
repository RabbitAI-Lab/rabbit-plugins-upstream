## Description: <br>
Save, list, search, and manage Telegram message bookmarks via /save commands. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[space-cadet](https://clawhub.ai/user/space-cadet) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to save Telegram messages or assistant replies as searchable bookmarks, then list, show, search, remove, count, and review tags for saved entries. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: /save can store complete assistant replies from session history on disk. <br>
Mitigation: Review saved content before using the skill with sensitive conversations, and avoid saving private or regulated content unless the storage path and access controls are acceptable. <br>
Risk: The evidence identifies a missing external bookmark.py implementation and storage location dependency. <br>
Mitigation: Verify the bookmark.py implementation and the final bookmark storage path before relying on save, search, show, remove, count, or tag operations. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/space-cadet/skills/bookmarks) <br>
- [Publisher Profile](https://clawhub.ai/user/space-cadet) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Guidance] <br>
**Output Format:** [Plain text command responses and append-only Markdown bookmark entries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Bookmark entries are intended for memory/bookmarks.md when the required bookmark CLI is present.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence and target metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

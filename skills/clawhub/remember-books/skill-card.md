## Description: <br>
A personal reading journal that keeps the books you have read, the ideas worth keeping, and the next book worth picking up. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[bluecolumnconsulting-lgtm](https://clawhub.ai/user/bluecolumnconsulting-lgtm) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to log books, recall stored takeaways during conversation, and ask for reading recommendations based on prior notes and tags. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Book notes, tags, and recall queries are sent to BlueColumn using the user's API key. <br>
Mitigation: Install only if the user trusts BlueColumn's handling of that data, and avoid storing secrets or highly sensitive personal information in journal entries. <br>
Risk: The skill requires a BlueColumn API key for integration and usage. <br>
Mitigation: Store the key in a secrets manager or environment variable and avoid embedding it directly in prompts, notes, shared files, or logs. <br>


## Reference(s): <br>
- [BlueColumn API documentation](https://bluecolumn.ai/docs) <br>
- [ClawHub skill page](https://clawhub.ai/bluecolumnconsulting-lgtm/skills/remember-books) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown with inline bash command examples and concise natural-language guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses a BlueColumn API key and sends book notes, tags, and recall queries to the BlueColumn service.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

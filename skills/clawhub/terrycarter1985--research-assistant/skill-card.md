## Description: <br>
Auto-illustrate research notes by reading Bear notes tagged 「待整理」, matching a topic-relevant GIF to each note's content, and inserting it inline. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[terrycarter1985](https://clawhub.ai/user/terrycarter1985) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and Bear users on macOS use this skill to scan tagged research notes, derive simple GIF search topics, and insert one matching GIF into each note. Dry-run and batch limits support review before modifying notes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Tagged Bear note content is used to form GIF search queries, which can expose sensitive note topics to the GIF search workflow. <br>
Mitigation: Run --dry-run first and avoid using the skill on tags containing confidential research, client data, credentials, medical, legal, or private personal material. <br>
Risk: Real runs modify Bear notes by inserting GIF Markdown. <br>
Mitigation: Use --max for small batches, confirm the tag scope before a real run, and review dry-run output before allowing note changes. <br>
Risk: The skill depends on local macOS tools and Bear x-callback behavior. <br>
Mitigation: Use it only on macOS with Bear running and the required grizzly, gifgrep, and jq commands installed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/terrycarter1985/research-assistant) <br>
- [Publisher profile](https://clawhub.ai/user/terrycarter1985) <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, markdown, guidance] <br>
**Output Format:** [Terminal status text and Markdown image links inserted into Bear notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May modify Bear notes unless --dry-run is used; processes notes selected by tag and optional max limit.] <br>

## Skill Version(s): <br>
0.1.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

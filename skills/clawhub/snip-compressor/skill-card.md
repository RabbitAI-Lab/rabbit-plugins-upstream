## Description: <br>
Semantic conversation compressor that summarizes long chat history while preserving key decisions, facts, tool context, and active thread continuity. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chen6896qqwee](https://clawhub.ai/user/chen6896qqwee) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to compress long conversation histories before context compaction, continuation, or session handoff while retaining decisions, facts, and current work. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill processes conversation history, which may include secrets, personal data, or sensitive project context. <br>
Mitigation: Prefer stdin/stdout for sensitive chats and avoid using --output on conversations containing secrets or personal data unless the destination file is controlled. <br>
Risk: Broad continuation prompts can trigger context summarization and may include more conversation history than expected. <br>
Mitigation: Review the input conversation before compression and inspect the generated Markdown before using it for handoff or compaction. <br>


## Reference(s): <br>
- [Snip Compressor on ClawHub](https://clawhub.ai/chen6896qqwee/skills/snip-compressor) <br>
- [Publisher profile](https://clawhub.ai/user/chen6896qqwee) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Text] <br>
**Output Format:** [Markdown report with summary, key decisions, active context, compressed transcript, and compression statistics] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can read conversation JSON from a file or stdin and can write the compressed report to stdout or an optional output file.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

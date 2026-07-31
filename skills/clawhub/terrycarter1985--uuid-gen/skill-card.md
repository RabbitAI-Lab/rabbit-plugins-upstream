## Description: <br>
Generate UUID v4 values or short random base36 identifiers on demand. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[terrycarter1985](https://clawhub.ai/user/terrycarter1985) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to generate unique identifiers for records, filenames, test data, primary keys, slugs, tokens, invite codes, and similar workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Short human-friendly IDs may not provide enough collision resistance or secrecy for high-value uses if generated with too little length. <br>
Mitigation: Use UUID v4 for strong uniqueness requirements, increase --length for short IDs, and check entropy needs before treating short IDs as secrets. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/terrycarter1985/skills/uuid-gen) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, guidance] <br>
**Output Format:** [Plain text identifiers with Markdown usage examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Emits one or more newline-delimited IDs; short IDs support configurable length.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

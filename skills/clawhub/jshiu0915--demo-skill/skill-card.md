## Description: <br>
Reviews a short product idea and returns structured feedback. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jshiu0915](https://clawhub.ai/user/jshiu0915) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, product builders, and developers use this skill to get a lightweight critique of a short product idea, including target-user summary, core value, practical suggestions, and one validation risk. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill's manifest includes file Read capability even though the intended task only needs the user's provided product idea. <br>
Mitigation: Provide only the idea to be reviewed and do not grant access to private files or unrelated workspace content when using this skill. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/jshiu0915/skills/demo-skill) <br>
- [Product idea example](examples/product-idea.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown with a summary, three suggestions, and one validation risk] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Concise critique based only on the user's provided idea] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence and target metadata; artifact frontmatter lists 0.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

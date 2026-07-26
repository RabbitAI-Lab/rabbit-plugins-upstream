## Description: <br>
Automatically recommends and ranks relevant skills to load based on the user message's implied domain or workflow, with an opt-in trigger. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[fvegiard](https://clawhub.ai/user/fvegiard) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to decide which available skills are relevant to a user turn, especially when the message implies a domain or workflow but no specific skill has been loaded. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Recommendations could cause an agent to load an irrelevant or overly broad skill for the user turn. <br>
Mitigation: Review the ranked recommendations and reasons before loading skills; keep the invoking agent's judgment as the final decision. <br>
Risk: The scanner evidence reports no concerns but notes the artifacts were not independently inspectable in that run. <br>
Mitigation: Review the skill instructions, install metadata, and file hash evidence before granting access to private files, credentials, or account-changing tools. <br>


## Reference(s): <br>
- [Server-resolved GitHub provenance: fvegiard/autoselect-skill](https://github.com/fvegiard/autoselect-skill) <br>
- [ClawHub skill page](https://clawhub.ai/fvegiard/skills/autoselect-skill) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, text] <br>
**Output Format:** [Markdown autoselect block with ranked recommendations and one-line reasons] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Caps recommendations at the top three skills with score at least 1; recommendations are advisory and the invoking agent remains in control.] <br>

## Skill Version(s): <br>
0.1.0 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

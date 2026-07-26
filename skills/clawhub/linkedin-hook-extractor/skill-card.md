## Description: <br>
Reverse-engineer the hook formula, structure, and reuse template from a LinkedIn post URL. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sergebulaev](https://clawhub.ai/user/sergebulaev) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Content strategists, marketers, and creators use this skill to study high-performing LinkedIn posts, identify their hook formula and structure, and produce a blank template for adapting the pattern in their own voice. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may call Apify with an existing APIFY_TOKEN to fetch a LinkedIn post. <br>
Mitigation: Use public or shareable post URLs, or paste the post text manually to avoid an external Apify fetch. <br>
Risk: The analysis can encourage close replication of another creator's post pattern. <br>
Mitigation: Use the generated blank template as structural guidance and rewrite it in the user's own voice instead of copying source language. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/sergebulaev/skills/linkedin-hook-extractor) <br>
- [Classification Rules](artifact/references/classification-rules.md) <br>
- [Examples](artifact/references/examples.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance] <br>
**Output Format:** [Markdown with structured bullets and template text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes formula confidence, structural breakdown, psychological rationale, a blank template, and cautions from the analyzed source post.] <br>

## Skill Version(s): <br>
1.0.9 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
